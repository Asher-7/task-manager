from datetime import datetime
from .database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    tasks = db.relationship("Task", backref="assignee", lazy=True, foreign_keys="Task.assigned_to")
    owned_tasks = db.relationship("Task", backref="creator", lazy=True, foreign_keys="Task.created_by")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    color = db.Column(db.String(7), default="#6366f1")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    tasks = db.relationship("Task", backref="project", lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "color": self.color,
            "task_count": len(self.tasks),
            "created_at": self.created_at.isoformat()
        }


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default="todo")        # todo, in_progress, done
    priority = db.Column(db.String(10), default="medium")    # low, medium, high, urgent
    due_date = db.Column(db.DateTime, nullable=True)

    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)

    def is_overdue(self):
        if self.due_date and self.status != "done":
            return datetime.utcnow() > self.due_date
        return False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "is_overdue": self.is_overdue(),
            "project_id": self.project_id,
            "created_by": self.created_by,
            "assigned_to": self.assigned_to,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "completed_at": self.completed_at.isoformat() if self.completed_at else None
        }


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    task = db.relationship("Task", backref=db.backref("comments", lazy=True, cascade="all, delete-orphan"))
    user = db.relationship("User", backref=db.backref("comments", lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "task_id": self.task_id,
            "user_id": self.user_id,
            "username": self.user.username if self.user else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class ActivityLog(db.Model):
    __tablename__ = "activity_logs"

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    action = db.Column(db.String(50), nullable=False)  # created, updated, status_changed, etc.
    field_name = db.Column(db.String(50), nullable=True)  # which field was changed
    old_value = db.Column(db.Text, nullable=True)
    new_value = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    task = db.relationship("Task", backref=db.backref("activity_logs", lazy=True, cascade="all, delete-orphan"))
    user = db.relationship("User", backref=db.backref("activity_logs", lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "task_id": self.task_id,
            "user_id": self.user_id,
            "username": self.user.username if self.user else None,
            "action": self.action,
            "field_name": self.field_name,
            "old_value": self.old_value,
            "new_value": self.new_value,
            "created_at": self.created_at.isoformat()
        }