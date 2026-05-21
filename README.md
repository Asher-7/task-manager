# 📋 Task Manager

A full-stack task management application built with Flask and vanilla JavaScript. Organize your work with projects, track progress, collaborate with comments, and monitor productivity with built-in analytics.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

### 🔐 User Management
- Secure user registration and authentication
- Password hashing with Werkzeug
- Session-based authentication
- User profile management

### 📝 Task Management
- **Create, Read, Update, Delete** tasks
- **Status Tracking**: Todo → In Progress → Done
- **Priority Levels**: Low, Medium, High, Urgent
- **Due Dates** with automatic overdue detection
- **Task Assignment** to team members
- **Filtering** by status, priority, project, or assignment

### 📁 Project Organization
- Group tasks into projects
- Color-coded projects for visual organization
- Track task counts per project
- Cascade delete protection

### 💬 Collaboration
- Comment on tasks
- Activity logging for all changes
- Audit trail with user attribution
- Track field-level changes (what changed, when, by whom)

### 📊 Analytics & Reporting
- Task statistics dashboard
- Status distribution (todo/in progress/done)
- Priority breakdown
- Completion rate calculation
- Overdue task tracking

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Asher-7/task-manager.git
   cd task-manager
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On macOS/Linux
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Open your browser**
   ```
   http://localhost:5000
   ```

The application will automatically create the SQLite database (`tasks.db`) on first run.

## 📖 Usage Guide

### Getting Started

1. **Register an Account**
   - Navigate to http://localhost:5000
   - Fill in the registration form with username, email, and password
   - Click "Register" to create your account

2. **Create Your First Project**
   - Click "Create Project"
   - Enter project name, description, and choose a color
   - Projects help organize related tasks

3. **Add Tasks**
   - Click "Create Task"
   - Fill in task details:
     - **Title**: Brief description of the task
     - **Description**: Detailed information (optional)
     - **Status**: todo, in_progress, or done
     - **Priority**: low, medium, high, or urgent
     - **Due Date**: When the task should be completed
     - **Project**: Assign to a project (optional)
     - **Assign To**: Assign to a user (optional)

4. **Manage Tasks**
   - **Update**: Click on a task to edit details
   - **Change Status**: Move tasks through workflow stages
   - **Add Comments**: Collaborate with team members
   - **Delete**: Remove completed or cancelled tasks

5. **Track Progress**
   - View statistics on the dashboard
   - Monitor completion rates
   - Identify overdue tasks
   - Review activity logs

## 🏗️ Project Structure

```
task-manager/
├── app/
│   ├── __init__.py          # Application factory
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   └── routes/
│       ├── __init__.py
│       ├── auth.py          # Authentication endpoints
│       ├── tasks.py         # Task management endpoints
│       ├── projects.py      # Project management endpoints
│       └── comments.py      # Comment endpoints
├── static/
│   └── index.html           # Frontend application
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── ARCHITECTURE.md          # Detailed architecture documentation
└── README.md               # This file
```

## 🔌 API Documentation

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
  "title": "Implement user authentication",
  "description": "Add JWT-based authentication",
  "status": "todo",
  "priority": "high",
  "due_date": "2026-06-01T00:00:00",
  "project_id": 1,
  "assigned_to": 2
}
```

#### Get Task
```http
GET /tasks/{id}
```

#### Update Task
```http
PUT /tasks/{id}
Content-Type: application/json

{
  "status": "in_progress",
  "priority": "urgent"
}
```

#### Delete Task
```http
DELETE /tasks/{id}
```

#### Get Statistics
```http
GET /tasks/stats
```

**Response:**
```json
{
  "total": 25,
  "by_status": {
    "todo": 10,
    "in_progress": 8,
    "done": 7
  },
  "by_priority": {
    "low": 5,
    "medium": 12,
    "high": 6,
    "urgent": 2
  },
  "overdue": 3,
  "completion_rate": 28.0
}
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
  "description": "Complete overhaul of company website",
  "color": "#6366f1"
}
```

#### Get Project with Tasks
```http
GET /projects/{id}
```

#### Update Project
```http
PUT /projects/{id}
Content-Type: application/json

{
  "name": "Updated Project Name",
  "color": "#ef4444"
}
```

#### Delete Project
```http
DELETE /projects/{id}
```

### Comment Endpoints

```http
GET /api/comments?task_id={id}
POST /api/comments
PUT /api/comments/{id}
DELETE /api/comments/{id}
```

## 🗄️ Database Schema

### User Model
```python
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- created_at
```

### Project Model
```python
- id (Primary Key)
- name
- description
- color (Hex color code)
- created_at
```

### Task Model
```python
- id (Primary Key)
- title
- description
- status (todo, in_progress, done)
- priority (low, medium, high, urgent)
- due_date
- project_id (Foreign Key → Project)
- created_by (Foreign Key → User)
- assigned_to (Foreign Key → User)
- created_at
- updated_at
- completed_at
```

### Comment Model
```python
- id (Primary Key)
- content
- task_id (Foreign Key → Task)
- user_id (Foreign Key → User)
- created_at
- updated_at
```

### ActivityLog Model
```python
- id (Primary Key)
- task_id (Foreign Key → Task)
- user_id (Foreign Key → User)
- action (created, updated, status_changed, etc.)
- field_name
- old_value
- new_value
- created_at
```

## 🔒 Security Features

- **Password Hashing**: Werkzeug PBKDF2 with salt
- **Session Management**: Secure session cookies
- **SQL Injection Prevention**: SQLAlchemy ORM with parameterized queries
- **Input Validation**: Server-side validation for all inputs
- **Authorization**: User ownership verification for all operations
- **Audit Trail**: Complete activity logging for compliance

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app --cov-report=html
```

## 🛠️ Development

### Running in Development Mode

The application runs in debug mode by default:

```bash
python run.py
```

Features in debug mode:
- Auto-reload on code changes
- Detailed error pages
- Debug toolbar (if installed)

### Database Management

**Reset the database:**
```bash
rm tasks.db
python run.py  # Will recreate tables
```

**Access SQLite database:**
```bash
sqlite3 tasks.db
.tables
.schema tasks
SELECT * FROM tasks;
```

### Code Style

This project follows PEP 8 style guidelines. Format code with:

```bash
black app/
flake8 app/
```

## 📦 Dependencies

### Core Dependencies
- **Flask 3.0.0** - Web framework
- **Flask-SQLAlchemy 3.1.1** - ORM for database operations
- **Werkzeug 3.0.1** - Security utilities (password hashing)

### Development Dependencies
- **pytest 8.0.0** - Testing framework

See `requirements.txt` for complete list.

## 🚀 Deployment

### Production Considerations

1. **Use a Production WSGI Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
   ```

2. **Use PostgreSQL Instead of SQLite**
   ```python
   app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@localhost/taskdb"
   ```

3. **Set Secure Secret Key**
   ```python
   app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
   ```

4. **Enable HTTPS**
   - Use reverse proxy (Nginx/Apache)
   - Configure SSL certificates

5. **Environment Variables**
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-secret-key
   export DATABASE_URL=postgresql://...
   ```

### Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:create_app()"]
```

Build and run:
```bash
docker build -t task-manager .
docker run -p 8000:8000 task-manager
```

## 🗺️ Roadmap

See our [prioritized feature roadmap](ARCHITECTURE.md#scalability-considerations) for upcoming features:

### Phase 1 (Critical)
- Real-time notifications
- File attachments
- Task dependencies
- Advanced search

### Phase 2 (Collaboration)
- Team workspaces
- @Mentions
- Task templates
- Subtasks

### Phase 3 (Productivity)
- Kanban board view
- Calendar view
- Time tracking
- Recurring tasks

### Phase 4 (Intelligence)
- Email integration
- Smart reminders
- Automation rules
- Analytics dashboard

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
- Follow PEP 8 style guide
- Ensure all tests pass

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Asher-7** - [GitHub Profile](https://github.com/Asher-7)

## 🙏 Acknowledgments

- Flask documentation and community
- SQLAlchemy for excellent ORM
- All contributors and users

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Asher-7/task-manager/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Asher-7/task-manager/discussions)
- **Email**: support@example.com

## 📚 Additional Resources

- [Architecture Documentation](ARCHITECTURE.md) - Detailed system architecture
- [API Documentation](#api-documentation) - Complete API reference
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

**Built with ❤️ using Flask and Python**

*Last Updated: May 2026*