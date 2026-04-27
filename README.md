# Task Manager

A full-featured task management application built with Flask and vanilla JavaScript.

## Features

- **User Authentication**: Register and login with secure password hashing
- **Task Management**: Create, update, delete, and track tasks
- **Project Organization**: Group tasks into projects
- **Priority Levels**: Set task priorities (low, medium, high, urgent)
- **Status Tracking**: Track task status (todo, in_progress, done)
- **Comments**: Add comments to tasks for collaboration
- **Activity Logging**: Track all changes made to tasks
- **Statistics Dashboard**: View task completion rates and statistics
- **Responsive UI**: Modern, gradient-styled interface

## Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Database**: SQLite
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Authentication**: Session-based with Werkzeug password hashing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Asher-7/task-manager.git
cd task-manager
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

5. Open your browser and navigate to `http://localhost:5000`

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login user
- `POST /auth/logout` - Logout user
- `GET /auth/me` - Get current user info

### Tasks
- `GET /tasks/` - List all tasks
- `POST /tasks/` - Create a new task
- `GET /tasks/<id>` - Get task details
- `PUT /tasks/<id>` - Update a task
- `DELETE /tasks/<id>` - Delete a task
- `GET /tasks/stats` - Get task statistics

### Projects
- `GET /projects/` - List all projects
- `POST /projects/` - Create a new project
- `GET /projects/<id>` - Get project details
- `PUT /projects/<id>` - Update a project
- `DELETE /projects/<id>` - Delete a project

### Comments
- `GET /api/task/<id>/comments` - Get task comments
- `POST /api/task/<id>/comments` - Add a comment
- `PUT /api/comments/<id>` - Update a comment
- `DELETE /api/comments/<id>` - Delete a comment
- `GET /api/task/<id>/activity` - Get task activity log

## Project Structure

```
task-manager/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   └── routes/
│       ├── __init__.py
│       ├── auth.py          # Authentication routes
│       ├── tasks.py         # Task management routes
│       ├── projects.py      # Project management routes
│       └── comments.py      # Comments and activity routes
├── static/
│   └── index.html           # Frontend application
├── instance/
│   └── tasks.db             # SQLite database (created on first run)
├── tests/
│   └── test_tasks.py        # Unit tests
├── .gitignore
├── requirements.txt
├── run.py                   # Application entry point
└── README.md
```

## Usage

1. **Register/Login**: Create an account or login with existing credentials
2. **Create Tasks**: Add new tasks with title, description, priority, and status
3. **Manage Tasks**: Click on any task to view details, add comments, and see activity history
4. **Track Progress**: View statistics dashboard to monitor your task completion rate
5. **Organize**: Create projects to group related tasks together

## Development

Run tests:
```bash
pytest tests/
```

## License

MIT License

## Author

Created with ❤️ by Asher-7