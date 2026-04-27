# 📋 Task Manager

A modern, full-stack task management application built with Flask and vanilla JavaScript. Organize your tasks, track progress, collaborate with comments, and maintain a complete activity history.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🔐 User Management
- **Secure Authentication**: Register and login with password hashing
- **Session Management**: Persistent sessions across browser refreshes
- **User Isolation**: Each user sees only their own tasks

### 📝 Task Management
- **CRUD Operations**: Create, read, update, and delete tasks
- **Status Tracking**: Todo, In Progress, Done
- **Priority Levels**: Low, Medium, High, Urgent
- **Due Dates**: Set deadlines and track overdue tasks
- **Rich Descriptions**: Add detailed task descriptions
- **Task Assignment**: Assign tasks to users

### 📊 Project Organization
- **Project Grouping**: Organize tasks into projects
- **Color Coding**: Customize project colors
- **Project Statistics**: Track task counts per project
- **Cascade Delete**: Removing a project removes all its tasks

### 💬 Collaboration
- **Comments**: Add comments to tasks for discussion
- **Activity Log**: Complete audit trail of all changes
- **Change Tracking**: See who changed what and when
- **Comment History**: View all comments chronologically

### 📈 Analytics
- **Dashboard Statistics**: Total tasks, completion rate, overdue count
- **Status Breakdown**: Tasks by status (todo, in progress, done)
- **Priority Distribution**: Tasks by priority level
- **Real-time Updates**: Statistics update automatically

### 🎨 User Interface
- **Modern Design**: Clean, gradient-based UI
- **Responsive Layout**: Works on desktop and mobile
- **Modal Details**: View task details without page reload
- **Color-coded Badges**: Visual status and priority indicators
- **Toast Notifications**: Success and error messages

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
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
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

The database will be created automatically on first run.

## 📖 Usage

### Getting Started

1. **Register an Account**
   - Enter username, email, and password
   - Click "Register"

2. **Create Your First Task**
   - Fill in the task title (required)
   - Add description, priority, and status
   - Click "Create Task"

3. **View Task Details**
   - Click on any task card
   - View full details, comments, and activity history
   - Add comments for collaboration

4. **Track Progress**
   - Update task status as you work
   - View statistics on your dashboard
   - Monitor overdue tasks

### API Endpoints

#### Authentication
```
POST   /auth/register    - Register new user
POST   /auth/login       - Login user
POST   /auth/logout      - Logout user
GET    /auth/me          - Get current user
```

#### Tasks
```
GET    /tasks/           - List all tasks (with filters)
POST   /tasks/           - Create new task
GET    /tasks/:id        - Get task details
PUT    /tasks/:id        - Update task
DELETE /tasks/:id        - Delete task
GET    /tasks/stats      - Get task statistics
```

#### Projects
```
GET    /projects/        - List all projects
POST   /projects/        - Create new project
GET    /projects/:id     - Get project with tasks
PUT    /projects/:id     - Update project
DELETE /projects/:id     - Delete project
```

#### Comments & Activity
```
GET    /api/task/:id/comments     - Get task comments
POST   /api/task/:id/comments     - Add comment
PUT    /api/comments/:id          - Update comment
DELETE /api/comments/:id          - Delete comment
GET    /api/task/:id/activity     - Get activity log
```

### Query Parameters

**List Tasks** (`GET /tasks/`)
- `status` - Filter by status (todo, in_progress, done)
- `priority` - Filter by priority (low, medium, high, urgent)
- `project_id` - Filter by project ID
- `assigned_to_me` - Show only assigned tasks (true/false)

Example:
```
GET /tasks/?status=in_progress&priority=high
```

## 🏗️ Architecture

### Technology Stack

**Backend:**
- Flask 3.0.0 - Web framework
- SQLAlchemy 3.1.1 - ORM for database operations
- Werkzeug 3.0.1 - Password hashing and security
- SQLite - Database (easily replaceable with PostgreSQL/MySQL)

**Frontend:**
- HTML5 - Structure
- CSS3 - Styling (inline, gradient design)
- Vanilla JavaScript - Interactivity
- Fetch API - HTTP requests

**Testing:**
- pytest 8.0.0 - Testing framework

### Project Structure

```
task-manager/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── database.py          # Database instance
│   ├── models.py            # Data models
│   └── routes/              # API endpoints
│       ├── auth.py          # Authentication
│       ├── tasks.py         # Task management
│       ├── projects.py      # Project management
│       └── comments.py      # Comments & activity
├── static/
│   └── index.html           # Frontend SPA
├── requirements.txt         # Dependencies
└── run.py                   # Entry point
```

### Database Schema

**Users**
- id, username, email, password_hash, created_at

**Projects**
- id, name, description, color, created_at

**Tasks**
- id, title, description, status, priority, due_date
- project_id (FK), created_by (FK), assigned_to (FK)
- created_at, updated_at, completed_at

**Comments**
- id, content, task_id (FK), user_id (FK)
- created_at, updated_at

**Activity Logs**
- id, task_id (FK), user_id (FK), action
- field_name, old_value, new_value, created_at

For detailed architecture diagrams, see [ARCHITECTURE.md](ARCHITECTURE.md).

For complete folder structure walkthrough, see [FOLDER_STRUCTURE.md](FOLDER_STRUCTURE.md).

## 🔒 Security Features

- **Password Hashing**: Werkzeug bcrypt-based hashing
- **Session Management**: Server-side sessions with secure cookies
- **User Isolation**: Users can only access their own tasks
- **Input Validation**: All inputs validated on backend
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- **XSS Protection**: Flask auto-escapes template variables

## 🧪 Testing

Run tests with pytest:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app tests/
```

## 🚀 Deployment

### Production Considerations

1. **Change Secret Key**
   ```python
   app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
   ```

2. **Use Production Database**
   ```python
   app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
   ```

3. **Disable Debug Mode**
   ```python
   app.run(debug=False)
   ```

4. **Use Production Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
   ```

### Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@localhost/taskmanager
FLASK_ENV=production
```

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:create_app()"]
```

Build and run:
```bash
docker build -t task-manager .
docker run -p 5000:5000 task-manager
```

## 📊 Performance Optimization

### Database Indexing

Add indexes for frequently queried fields:

```python
class Task(db.Model):
    __table_args__ = (
        db.Index('idx_task_status', 'status'),
        db.Index('idx_task_priority', 'priority'),
        db.Index('idx_task_user', 'created_by'),
    )
```

### Caching

Implement Redis for session storage:

```python
from flask_session import Session
app.config["SESSION_TYPE"] = "redis"
app.config["SESSION_REDIS"] = redis.from_url("redis://localhost:6379")
Session(app)
```

### Pagination

Add pagination to task lists:

```python
page = request.args.get('page', 1, type=int)
per_page = request.args.get('per_page', 20, type=int)
tasks = Task.query.paginate(page=page, per_page=per_page)
```

## 🛠️ Development

### Adding New Features

1. **Create Model** (if needed) in `app/models.py`
2. **Create Routes** in appropriate blueprint
3. **Update Frontend** in `static/index.html`
4. **Add Tests** in `tests/`
5. **Update Documentation**

### Code Style

Follow PEP 8 for Python code:

```bash
pip install black flake8
black app/
flake8 app/
```

### Database Migrations

Use Alembic for schema changes:

```bash
pip install alembic
alembic init migrations
alembic revision --autogenerate -m "Add new field"
alembic upgrade head
```

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
- Ensure all tests pass

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Asher-7**
- GitHub: [@Asher-7](https://github.com/Asher-7)
- Repository: [task-manager](https://github.com/Asher-7/task-manager)

## 🙏 Acknowledgments

- Flask documentation and community
- SQLAlchemy for excellent ORM
- All contributors and users

## 📞 Support

If you have any questions or issues:

1. Check the [documentation](FOLDER_STRUCTURE.md)
2. Search [existing issues](https://github.com/Asher-7/task-manager/issues)
3. Create a [new issue](https://github.com/Asher-7/task-manager/issues/new)

## 🗺️ Roadmap

### Planned Features

- [ ] Email notifications for due dates
- [ ] Task templates
- [ ] Recurring tasks
- [ ] File attachments
- [ ] Team collaboration
- [ ] Mobile app
- [ ] Dark mode
- [ ] Export to CSV/PDF
- [ ] Calendar view
- [ ] Kanban board view
- [ ] Time tracking
- [ ] Task dependencies
- [ ] Custom fields
- [ ] API rate limiting
- [ ] Webhooks

## 📈 Changelog

### Version 1.0.0 (Current)

- Initial release
- User authentication
- Task CRUD operations
- Project management
- Comments system
- Activity logging
- Statistics dashboard
- Responsive UI

---

**Made with ❤️ using Flask and JavaScript**

⭐ Star this repository if you find it helpful!
