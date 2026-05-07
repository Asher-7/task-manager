# Task Manager Application

A full-stack web application for managing tasks, projects, and team collaboration built with Flask and SQLite.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.1.1-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Features

### Core Functionality
- ✅ **User Authentication** - Secure registration, login/logout with session management
- ✅ **Task Management** - Create, read, update, and delete tasks with rich metadata
- ✅ **Project Organization** - Group related tasks into color-coded projects
- ✅ **Comments & Collaboration** - Add, edit, and delete comments on tasks
- ✅ **Activity Tracking** - Complete audit trail of all task changes
- ✅ **Task Statistics** - Dashboard with completion rates and analytics

### Task Features
- **Status Tracking**: Todo → In Progress → Done
- **Priority Levels**: Low, Medium, High, Urgent
- **Due Dates**: Set deadlines with automatic overdue detection
- **Task Assignment**: Assign tasks to team members
- **Filtering**: Filter by status, priority, project, or assignment
- **Search**: Find tasks quickly (basic implementation)

### Project Features
- Create unlimited projects
- Color-coded organization
- View all tasks within a project
- Track task counts per project

### Collaboration
- Comment on tasks for team communication
- Activity log shows who changed what and when
- Track field-level changes (old value → new value)

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)
- [Architecture](#architecture)
- [Database Schema](#database-schema)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Future Features](#future-features)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd task-manager
```

2. **Create and activate virtual environment**
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Initialize the database**
The database will be automatically created when you first run the application.

## 🚀 Quick Start

### Running the Application

```bash
python run.py
```

The application will start on `http://localhost:5000`

### First Steps

1. **Register a new account**
   - Navigate to `http://localhost:5000`
   - Click "Register" and create your account

2. **Create your first project**
   - Use the Projects section to create a project
   - Give it a name, description, and color

3. **Add tasks**
   - Create tasks with titles, descriptions, priorities, and due dates
   - Assign tasks to projects
   - Set status and priority levels

4. **Collaborate**
   - Add comments to tasks
   - View activity logs to see changes
   - Track task completion

## 📚 API Documentation

### Authentication Endpoints

#### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "secure_password"
}
```

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "username": "john_doe",
  "password": "secure_password"
}
```

#### Logout
```http
POST /auth/logout
```

#### Get Current User
```http
GET /auth/me
```

### Task Endpoints

#### List Tasks
```http
GET /tasks/?status=todo&priority=high&project_id=1&assigned_to_me=true
```

#### Create Task
```http
POST /tasks/
Content-Type: application/json

{
  "title": "Implement login feature",
  "description": "Add user authentication",
  "status": "todo",
  "priority": "high",
  "due_date": "2024-12-31T23:59:59",
  "project_id": 1,
  "assigned_to": 2
}
```

#### Get Task
```http
GET /tasks/{task_id}
```

#### Update Task
```http
PUT /tasks/{task_id}
Content-Type: application/json

{
  "status": "in_progress",
  "priority": "urgent"
}
```

#### Delete Task
```http
DELETE /tasks/{task_id}
```

#### Get Task Statistics
```http
GET /tasks/stats
```

### Project Endpoints

#### List Projects
```http
GET /projects/
```

#### Create Project
```http
POST /projects/
Content-Type: application/json

{
  "name": "Website Redesign",
  "description": "Q4 2024 website refresh",
  "color": "#6366f1"
}
```

#### Get Project with Tasks
```http
GET /projects/{project_id}
```

#### Update Project
```http
PUT /projects/{project_id}
Content-Type: application/json

{
  "name": "Updated Project Name",
  "color": "#ef4444"
}
```

#### Delete Project
```http
DELETE /projects/{project_id}
```

### Comment Endpoints

#### Get Task Comments
```http
GET /api/task/{task_id}/comments
```

#### Create Comment
```http
POST /api/task/{task_id}/comments
Content-Type: application/json

{
  "content": "This looks good, let's proceed!"
}
```

#### Update Comment
```http
PUT /api/comments/{comment_id}
Content-Type: application/json

{
  "content": "Updated comment text"
}
```

#### Delete Comment
```http
DELETE /api/comments/{comment_id}
```

#### Get Task Activity Log
```http
GET /api/task/{task_id}/activity
```

## 🏗️ Architecture

The application follows a three-tier architecture:

```
┌─────────────────┐
│   Frontend      │  HTML/CSS/JavaScript (SPA)
│   (Static)      │
└────────┬────────┘
         │ HTTP/JSON
┌────────▼────────┐
│   Application   │  Flask + Blueprints
│   Layer         │  - Authentication
│                 │  - Task Management
│                 │  - Projects
│                 │  - Comments
└────────┬────────┘
         │ SQLAlchemy ORM
┌────────▼────────┐
│   Data Layer    │  SQLite Database
│                 │  - Users
│                 │  - Tasks
│                 │  - Projects
│                 │  - Comments
│                 │  - Activity Logs
└─────────────────┘
```

For detailed architecture documentation, see [ARCHITECTURE.md](ARCHITECTURE.md)

## 🗄️ Database Schema

### Users Table
- `id` (Primary Key)
- `username` (Unique)
- `email` (Unique)
- `password_hash`
- `created_at`

### Projects Table
- `id` (Primary Key)
- `name`
- `description`
- `color`
- `created_at`

### Tasks Table
- `id` (Primary Key)
- `title`
- `description`
- `status` (todo/in_progress/done)
- `priority` (low/medium/high/urgent)
- `due_date`
- `project_id` (Foreign Key → projects)
- `created_by` (Foreign Key → users)
- `assigned_to` (Foreign Key → users)
- `created_at`
- `updated_at`
- `completed_at`

### Comments Table
- `id` (Primary Key)
- `content`
- `task_id` (Foreign Key → tasks)
- `user_id` (Foreign Key → users)
- `created_at`
- `updated_at`

### Activity Logs Table
- `id` (Primary Key)
- `task_id` (Foreign Key → tasks)
- `user_id` (Foreign Key → users)
- `action` (created/updated/commented/etc.)
- `field_name`
- `old_value`
- `new_value`
- `created_at`

## 💻 Development

### Project Structure
```
task-manager/
├── app/
│   ├── __init__.py          # Application factory
│   ├── database.py          # Database initialization
│   ├── models.py            # SQLAlchemy models
│   └── routes/
│       ├── __init__.py
│       ├── auth.py          # Authentication routes
│       ├── tasks.py         # Task management routes
│       ├── projects.py      # Project routes
│       └── comments.py      # Comments & activity routes
├── static/
│   └── index.html           # Frontend SPA
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── ARCHITECTURE.md         # Detailed architecture docs
└── FEATURE_ROADMAP.md      # Future feature plans
```

### Adding New Features

1. **Create/Update Models** in `app/models.py`
2. **Add Routes** in appropriate blueprint file
3. **Update Frontend** in `static/index.html`
4. **Test** your changes
5. **Document** in relevant files

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions
- Keep functions focused and small

## 🧪 Testing

### Running Tests
```bash
pytest
```

### Test Coverage
```bash
pytest --cov=app tests/
```

### Writing Tests
Tests should be placed in a `tests/` directory (to be created):
```
tests/
├── test_auth.py
├── test_tasks.py
├── test_projects.py
└── test_comments.py
```

## 🚀 Deployment

### Production Considerations

1. **Change Secret Key**
   ```python
   # In app/__init__.py
   app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
   ```

2. **Use Production Database**
   - Migrate from SQLite to PostgreSQL or MySQL
   - Update `SQLALCHEMY_DATABASE_URI`

3. **Disable Debug Mode**
   ```python
   # In run.py
   app.run(debug=False)
   ```

4. **Use Production Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

5. **Set Environment Variables**
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-secret-key
   export DATABASE_URL=postgresql://user:pass@localhost/dbname
   ```

### Docker Deployment (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
```

## 🔮 Future Features

We have an extensive roadmap of features planned! See [FEATURE_ROADMAP.md](FEATURE_ROADMAP.md) for details.

### Upcoming Features (High Priority)
- 🔗 Task Dependencies & Subtasks
- 🔔 Real-time Notifications
- 📎 File Attachments
- 📋 Task Templates
- 🔍 Advanced Search & Filtering

### Medium Priority
- 🏷️ Task Tags/Labels
- ⏱️ Time Tracking
- 🔄 Recurring Tasks
- 👥 Team Workspaces
- 📊 Kanban Board View

See the full roadmap for 25+ planned features!

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Write clear commit messages
- Add tests for new features
- Update documentation
- Follow existing code style
- Keep PRs focused on a single feature/fix

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Initial development by [Your Name]

## 🙏 Acknowledgments

- Flask framework and community
- SQLAlchemy ORM
- All contributors and users

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [your-email@example.com]

## 📊 Project Status

**Current Version:** 1.0.0  
**Status:** Active Development  
**Last Updated:** 2024

---

**Made with ❤️ using Flask and Python**
