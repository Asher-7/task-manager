from flask import Flask, send_from_directory
from .database import db
from .routes.auth import auth_bp
from .routes.tasks import tasks_bp
from .routes.projects import projects_bp
from .routes.comments import comments_bp
import os


def create_app(config=None):
    app = Flask(__name__, static_folder='../static')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev-secret-key"

    if config:
        app.config.update(config)

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(tasks_bp, url_prefix="/tasks")
    app.register_blueprint(projects_bp, url_prefix="/projects")
    app.register_blueprint(comments_bp, url_prefix="/api")

    @app.route('/')
    def index():
        static_folder = app.static_folder or '../static'
        return send_from_directory(static_folder, 'index.html')

    with app.app_context():
        db.create_all()

    return app