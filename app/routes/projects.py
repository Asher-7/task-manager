from flask import Blueprint, request, jsonify, session
from ..models import Project, Task
from ..database import db

projects_bp = Blueprint("projects", __name__)


def current_user_id():
    return session.get("user_id")


@projects_bp.route("/", methods=["GET"])
def list_projects():
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401
    projects = Project.query.all()
    return jsonify({"projects": [p.to_dict() for p in projects]}), 200


@projects_bp.route("/", methods=["POST"])
def create_project():
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    data = request.get_json()
    if not data or not data.get("name"):
        return jsonify({"error": "name is required"}), 400

    project = Project(
        name=data["name"],
        description=data.get("description"),
        color=data.get("color", "#6366f1")
    )
    db.session.add(project)
    db.session.commit()
    return jsonify(project.to_dict()), 201


@projects_bp.route("/<int:project_id>", methods=["GET"])
def get_project(project_id):
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401
    project = Project.query.get_or_404(project_id)
    tasks = Task.query.filter_by(project_id=project_id).all()
    data = project.to_dict()
    data["tasks"] = [t.to_dict() for t in tasks]
    return jsonify(data), 200


@projects_bp.route("/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    project = Project.query.get_or_404(project_id)
    data = request.get_json()

    if data.get("name"):
        project.name = data["name"]
    if data.get("description") is not None:
        project.description = data["description"]
    if data.get("color"):
        project.color = data["color"]

    db.session.commit()
    return jsonify(project.to_dict()), 200


@projects_bp.route("/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({"message": "Project deleted"}), 200