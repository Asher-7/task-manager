from flask import Blueprint, request, jsonify, session
from ..models import Comment, Task, ActivityLog
from ..database import db

comments_bp = Blueprint("comments", __name__)


def current_user_id():
    return session.get("user_id")


@comments_bp.route("/task/<int:task_id>/comments", methods=["GET"])
def get_task_comments(task_id):
    """Get all comments for a specific task"""
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    # Verify user has access to this task
    task = Task.query.filter_by(id=task_id, created_by=user_id).first_or_404()
    
    comments = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.desc()).all()
    return jsonify({"comments": [c.to_dict() for c in comments]}), 200


@comments_bp.route("/task/<int:task_id>/comments", methods=["POST"])
def create_comment(task_id):
    """Create a new comment on a task"""
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    # Verify user has access to this task
    task = Task.query.filter_by(id=task_id, created_by=user_id).first_or_404()
    
    data = request.get_json()
    if not data or not data.get("content"):
        return jsonify({"error": "content is required"}), 400

    comment = Comment(
        content=data["content"],
        task_id=task_id,
        user_id=user_id
    )
    db.session.add(comment)
    
    # Log activity
    activity = ActivityLog(
        task_id=task_id,
        user_id=user_id,
        action="commented",
        new_value=data["content"][:100]  # Store first 100 chars
    )
    db.session.add(activity)
    
    db.session.commit()
    return jsonify(comment.to_dict()), 201


@comments_bp.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    """Update an existing comment"""
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    comment = Comment.query.filter_by(id=comment_id, user_id=user_id).first_or_404()
    
    data = request.get_json()
    if not data or not data.get("content"):
        return jsonify({"error": "content is required"}), 400

    old_content = comment.content
    comment.content = data["content"]
    
    # Log activity
    activity = ActivityLog(
        task_id=comment.task_id,
        user_id=user_id,
        action="comment_updated",
        old_value=old_content[:100],
        new_value=data["content"][:100]
    )
    db.session.add(activity)
    
    db.session.commit()
    return jsonify(comment.to_dict()), 200


@comments_bp.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    """Delete a comment"""
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    comment = Comment.query.filter_by(id=comment_id, user_id=user_id).first_or_404()
    
    # Log activity
    activity = ActivityLog(
        task_id=comment.task_id,
        user_id=user_id,
        action="comment_deleted",
        old_value=comment.content[:100]
    )
    db.session.add(activity)
    
    db.session.delete(comment)
    db.session.commit()
    return jsonify({"message": "Comment deleted"}), 200


@comments_bp.route("/task/<int:task_id>/activity", methods=["GET"])
def get_task_activity(task_id):
    """Get activity log for a specific task"""
    user_id = current_user_id()
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    # Verify user has access to this task
    task = Task.query.filter_by(id=task_id, created_by=user_id).first_or_404()
    
    activities = ActivityLog.query.filter_by(task_id=task_id).order_by(ActivityLog.created_at.desc()).all()
    return jsonify({"activities": [a.to_dict() for a in activities]}), 200

# Made with Bob