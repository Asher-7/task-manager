# 📋 Task Manager

A modern full-stack task management application built with Flask, SQLAlchemy, SQLite, and vanilla JavaScript. It helps users manage personal work by organizing tasks into projects, tracking progress, collaborating through comments, and reviewing change history through activity logs.

## Overview

[`task-manager/`](task-manager) is a monolithic web application with a simple three-layer architecture:

- **Frontend**: browser UI served from [`static/index.html`](task-manager/static/index.html)
- **Backend**: Flask application created by [`create_app()`](task-manager/app/__init__.py:1)
- **Database**: SQLAlchemy models persisted to SQLite in [`models.py`](task-manager/app/models.py)

The application is designed to be lightweight, easy to run locally, and straightforward to extend.

## Features

### Authentication
- User registration
- User login/logout
- Password hashing with Werkzeug
- Session-based authentication
- User-level data isolation

### Task Management
- Create, read, update, and delete tasks
- Status tracking: todo, in progress, done
- Priority levels: low, medium, high, urgent
- Due date support
- Task descriptions
- Task assignment

### Project Organization
- Group tasks by project
- Project color coding
- Project-level task visibility
- Cascade delete behavior for project cleanup

### Collaboration
- Comments on tasks
- Activity log / audit trail
- Change tracking across task updates

### Dashboard & Analytics
- Task statistics
- Completion tracking
- Status and priority summaries
- Overdue task visibility

## Technology Stack

### Backend
- [`Flask`](task-manager/requirements.txt)
- [`Flask-SQLAlchemy`](task-manager/requirements.txt)
- [`Werkzeug`](task-manager/requirements.txt)
- SQLite

### Frontend
- HTML
- CSS
- Vanilla JavaScript
- Fetch API

### Testing
- [`pytest`](task-manager/requirements.txt)

## Project Structure

```text
task-manager/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   └── routes/
│       ├── auth.py
│       ├── comments.py
│       ├── projects.py
│       └── tasks.py
├── static/
│   └── index.html
├── ARCHITECTURE.md
├── README.md
├── requirements.txt
└── run.py
```

## Architecture

The application follows a monolithic Flask architecture.

```mermaid
flowchart TB
    U[User Browser]
    FE[Frontend<br/>[`static/index.html`](task-manager/static/index.html)]
    APP[Flask App<br/>[`create_app()`](task-manager/app/__init__.py:1)]
    AUTH[Auth Routes<br/>[`auth.py`](task-manager/app/routes/auth.py)]
    TASKS[Task Routes<br/>[`tasks.py`](task-manager/app/routes/tasks.py)]
    PROJECTS[Project Routes<br/>[`projects.py`](task-manager/app/routes/projects.py)]
    COMMENTS[Comments Routes<br/>[`comments.py`](task-manager/app/routes/comments.py)]
    MODELS[SQLAlchemy Models<br/>[`models.py`](task-manager/app/models.py)]
    DB[(SQLite)]

    U --> FE
    FE -->|HTTP / Fetch| APP
    APP --> AUTH
    APP --> TASKS
    APP --> PROJECTS
    APP --> COMMENTS
    AUTH --> MODELS
    TASKS --> MODELS
    PROJECTS --> MODELS
    COMMENTS --> MODELS
    MODELS --> DB
```

For more detail, see [`ARCHITECTURE.md`](task-manager/ARCHITECTURE.md).

## API Overview

### Authentication
- `POST /auth/register`
- `POST /auth/login`
- `POST /auth/logout`
- `GET /auth/me`

### Tasks
- `GET /tasks/`
- `POST /tasks/`
- `GET /tasks/:id`
- `PUT /tasks/:id`
- `DELETE /tasks/:id`
- `GET /tasks/stats`

### Projects
- `GET /projects/`
- `POST /projects/`
- `GET /projects/:id`
- `PUT /projects/:id`
- `DELETE /projects/:id`

### Comments & Activity
- `GET /api/task/:id/comments`
- `POST /api/task/:id/comments`
- `PUT /api/comments/:id`
- `DELETE /api/comments/:id`
- `GET /api/task/:id/activity`

## Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Asher-7/task-manager.git
   cd task-manager
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   python run.py
   ```

6. Open in browser:
   ```text
   http://localhost:5000
   ```

## Running Tests

Run all tests with:

```bash
pytest
```

## Local Development

The local entry point is [`run.py`](task-manager/run.py), which starts the Flask development server on port `5000`.

Main backend modules:
- [`app/__init__.py`](task-manager/app/__init__.py)
- [`app/database.py`](task-manager/app/database.py)
- [`app/models.py`](task-manager/app/models.py)
- [`app/routes/auth.py`](task-manager/app/routes/auth.py)
- [`app/routes/tasks.py`](task-manager/app/routes/tasks.py)
- [`app/routes/projects.py`](task-manager/app/routes/projects.py)
- [`app/routes/comments.py`](task-manager/app/routes/comments.py)

Frontend:
- [`static/index.html`](task-manager/static/index.html)

## Security Notes

This application includes:
- Password hashing with Werkzeug
- Session-based authentication
- ORM-based database access
- User-level task isolation
- Backend-side input validation

For production, you should:
- set a strong secret key
- disable debug mode
- move to PostgreSQL or another production database
- run behind Gunicorn or another production WSGI server
- load secrets from environment variables

## Future Improvements

Potential next steps:
- Add Alembic migrations
- Add pagination to task lists
- Split frontend assets into dedicated JS/CSS files
- Add more automated tests
- Add email reminders and recurring tasks
- Upgrade database for production workloads

## Documentation

- Architecture details: [`ARCHITECTURE.md`](task-manager/ARCHITECTURE.md)

## Author

- GitHub: [`@Asher-7`](https://github.com/Asher-7)
- Repository: [`Asher-7/task-manager`](https://github.com/Asher-7/task-manager)

## License

This project is licensed under the MIT License.
