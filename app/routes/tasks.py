from flask import Blueprint, request, jsonify, session
from datetime import datetime
from ..models import Task, Project, ActivityLog
from ..database import db
# Activity logging enabled

tasks_bp = Blueprint("tasks", __name__)

VALID_STATUSES = {"todo", "in_progress", "done"}
VALID_PRIORITIES = {"low", "medium", "high", "urgent"}


def current_user_id():
    return session.get("user_id")


@tasks_bp.route("/", methods=["GET"])
def list_tasks():
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    status = request.args.get("status")
    priority = request.args.get("priority")
    project_id = request.args.get("project_id", type=int)
    assigned_to_me = request.args.get("assigned_to_me", "false").lower() == "true"

    query = Task.query.filter_by(created_by=user_id)

    if assigned_to_me:
        query = Task.query.filter_by(assigned_to=user_id)
    if status:
        query = query.filter_by(status=status)
    if priority:
        query = query.filter_by(priority=priority)
    if project_id:
        query = query.filter_by(project_id=project_id)

    tasks = query.order_by(Task.created_at.desc()).all()
    return jsonify({"total": len(tasks), "tasks": [t.to_dict() for t in tasks]}), 200


@tasks_bp.route("/", methods=["POST"])
def create_task():
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "title is required"}), 400

    if data.get("status") and data["status"] not in VALID_STATUSES:
        return jsonify({"error": f"status must be one of {VALID_STATUSES}"}), 400

    if data.get("priority") and data["priority"] not in VALID_PRIORITIES:
        return jsonify({"error": f"priority must be one of {VALID_PRIORITIES}"}), 400

    task = Task(
        title=data["title"],
        description=data.get("description"),
        status=data.get("status", "todo"),
        priority=data.get("priority", "medium"),
        due_date=datetime.fromisoformat(data["due_date"]) if data.get("due_date") else None,
        project_id=data.get("project_id"),
        created_by=user_id,
        assigned_to=data.get("assigned_to")
    )
    db.session.add(task)
    db.session.flush()  # Get task ID before commit
    
    # Log activity
    activity = ActivityLog(
        task_id=task.id,
        user_id=user_id,
        action="created",
        new_value=data["title"]
    )
    db.session.add(activity)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@tasks_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401
    task = Task.query.filter_by(id=task_id, created_by=user_id).first_or_404()
    return jsonify(task.to_dict()), 200


@tasks_bp.route("/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    task = Task.query.filter_by(id=task_id, created_by=user_id).first_or_404()
    data = request.get_json()

    # Track changes for activity log
    changes = []

    if data.get("title") and task.title != data["title"]:
        changes.append(("title", task.title, data["title"]))
        task.title = data["title"]
    if data.get("description") is not None and task.description != data.get("description"):
        changes.append(("description", task.description, data["description"]))
        task.description = data["description"]
    if data.get("priority") and data["priority"] in VALID_PRIORITIES and task.priority != data["priority"]:
        changes.append(("priority", task.priority, data["priority"]))
        task.priority = data["priority"]
    if data.get("due_date") is not None:
        new_due_date = datetime.fromisoformat(data["due_date"]) if data["due_date"] else None
        if task.due_date != new_due_date:
            changes.append(("due_date", str(task.due_date) if task.due_date else None, str(new_due_date) if new_due_date else None))
            task.due_date = new_due_date
    if data.get("assigned_to") is not None and task.assigned_to != data.get("assigned_to"):
        changes.append(("assigned_to", str(task.assigned_to), str(data["assigned_to"])))
        task.assigned_to = data["assigned_to"]
    if data.get("project_id") is not None and task.project_id != data.get("project_id"):
        changes.append(("project_id", str(task.project_id), str(data["project_id"])))
        task.project_id = data["project_id"]

    if data.get("status") and data["status"] in VALID_STATUSES and task.status != data["status"]:
        changes.append(("status", task.status, data["status"]))
        task.status = data["status"]
        if data["status"] == "done" and not task.completed_at:
            task.completed_at = datetime.utcnow()
        elif data["status"] != "done":
            task.completed_at = None

    # Log all changes
    for field_name, old_value, new_value in changes:
        activity = ActivityLog(
            task_id=task_id,
            user_id=user_id,
            action="updated",
            field_name=field_name,
            old_value=str(old_value) if old_value else None,
            new_value=str(new_value) if new_value else None
        )
        db.session.add(activity)

    db.session.commit()
    return jsonify(task.to_dict()), 200


@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401
    task = Task.query.filter_by(id=task_id, created_by=user_id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200


@tasks_bp.route("/stats", methods=["GET"])
def get_stats():
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    tasks = Task.query.filter_by(created_by=user_id).all()

    by_status = {"todo": 0, "in_progress": 0, "done": 0}
    by_priority = {"low": 0, "medium": 0, "high": 0, "urgent": 0}
    overdue = 0

    for t in tasks:
        by_status[t.status] = by_status.get(t.status, 0) + 1
        by_priority[t.priority] = by_priority.get(t.priority, 0) + 1
        if t.is_overdue():
            overdue += 1

    completion_rate = 0
    if tasks:
        completion_rate = round((by_status["done"] / len(tasks)) * 100, 1)

    return jsonify({
        "total": len(tasks),
        "by_status": by_status,
        "by_priority": by_priority,
        "overdue": overdue,
        "completion_rate": completion_rate
    }), 200