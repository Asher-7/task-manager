# 📋 Task Manager

A comprehensive full-stack web application for managing tasks, projects, and team collaboration. Built with Flask (Python) backend and vanilla JavaScript frontend, featuring real-time updates, activity tracking, and collaborative commenting.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.1.1-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

### Core Functionality
- ✅ **User Authentication**: Secure registration, login, and session management
- 📝 **Task Management**: Create, read, update, and delete tasks with rich metadata
- 📊 **Project Organization**: Group tasks into projects with custom colors and descriptions
- 💬 **Collaborative Comments**: Add comments to tasks for team communication
- 📈 **Activity Logging**: Comprehensive audit trail of all task changes
- 📉 **Statistics Dashboard**: Real-time analytics and completion metrics

### Task Features
- **Status Tracking**: Todo, In Progress, Done
- **Priority Levels**: Low, Medium, High, Urgent
- **Due Dates**: Set deadlines with automatic overdue detection
- **Task Assignment**: Assign tasks to team members
- **Descriptions**: Rich text descriptions for detailed task information
- **Timestamps**: Track creation, update, and completion times

### User Experience
- 🎨 **Modern UI**: Clean, responsive design with gradient styling
- 🔄 **Real-time Updates**: Instant UI updates without page refresh
- 🎯 **Modal Dialogs**: Detailed task view with comments and activity
- 🏷️ **Color-coded Badges**: Visual status and priority indicators
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile devices

## 🚀 Quick Start

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Asher-7/task-manager.git
   cd task-manager
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python run.py
   ```

4. **Open in browser**
   ```
   http://localhost:5000
   ```

The application will automatically create the SQLite database on first run.

## 📁 Project Structure

```
task-manager/
├── app/
│   ├── __init__.py          # Application factory and configuration
│   ├── database.py          # Database initialization
│   ├── models.py            # SQLAlchemy data models
│   └── routes/
│       ├── __init__.py
│       ├── auth.py          # Authentication endpoints
│       ├── tasks.py         # Task CRUD operations
│       ├── projects.py      # Project management
│       └── comments.py      # Comments and activity logs
├── static/
│   └── index.html           # Single-page application frontend
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── architecture.md          # Detailed architecture documentation
└── README.md               # This file
```

## 🔧 Technology Stack

### Backend
- **Flask 3.0.0**: Lightweight Python web framework
- **SQLAlchemy 3.1.1**: SQL toolkit and ORM
- **Werkzeug 3.0.1**: WSGI utility library
- **SQLite**: Embedded database (easily upgradeable to PostgreSQL/MySQL)

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **JavaScript (ES6+)**: Vanilla JS for dynamic interactions
- **Fetch API**: RESTful API communication

### Testing
- **Pytest 8.0.0**: Testing framework

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | User login |
| POST | `/auth/logout` | User logout |
| GET | `/auth/me` | Get current user info |

### Task Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks/` | List all tasks |
| POST | `/tasks/` | Create new task |
| GET | `/tasks/:id` | Get task details |
| PUT | `/tasks/:id` | Update task |
| DELETE | `/tasks/:id` | Delete task |
| GET | `/tasks/stats` | Get task statistics |

### Project Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/projects/` | List all projects |
| POST | `/projects/` | Create new project |
| GET | `/projects/:id` | Get project details |
| PUT | `/projects/:id` | Update project |
| DELETE | `/projects/:id` | Delete project |

### Comment & Activity Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/task/:id/comments` | Get task comments |
| POST | `/api/task/:id/comments` | Add comment to task |
| GET | `/api/task/:id/activity` | Get task activity log |

## 💾 Database Schema

### Users
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email address
- `password_hash`: Hashed password
- `created_at`: Registration timestamp

### Projects
- `id`: Primary key
- `name`: Project name
- `description`: Project description
- `color`: Hex color code
- `created_at`: Creation timestamp

### Tasks
- `id`: Primary key
- `title`: Task title
- `description`: Task description
- `status`: todo | in_progress | done
- `priority`: low | medium | high | urgent
- `due_date`: Optional deadline
- `project_id`: Foreign key to projects
- `created_by`: Foreign key to users (creator)
- `assigned_to`: Foreign key to users (assignee)
- `created_at`, `updated_at`, `completed_at`: Timestamps

### Comments
- `id`: Primary key
- `content`: Comment text
- `task_id`: Foreign key to tasks
- `user_id`: Foreign key to users
- `created_at`, `updated_at`: Timestamps

### Activity Logs
- `id`: Primary key
- `task_id`: Foreign key to tasks
- `user_id`: Foreign key to users
- `action`: Action type (created, updated, etc.)
- `field_name`: Changed field name
- `old_value`, `new_value`: Change tracking
- `created_at`: Timestamp

## 🎯 Usage Guide

### Getting Started

1. **Register an Account**
   - Enter username, email, and password
   - Click "Register" button

2. **Create Your First Task**
   - Fill in task title (required)
   - Add description (optional)
   - Select priority level
   - Choose status
   - Click "Create Task"

3. **View Task Details**
   - Click on any task card
   - View full details in modal dialog
   - See comments and activity history

4. **Add Comments**
   - Open task details modal
   - Type comment in text area
   - Click "Add Comment"

5. **Track Progress**
   - View statistics dashboard
   - Monitor completion rates
   - Track tasks by status

## 🔐 Security Features

- **Password Hashing**: Secure password storage using Werkzeug
- **Session Management**: Server-side session handling
- **SQL Injection Protection**: SQLAlchemy ORM prevents SQL injection
- **XSS Protection**: Input sanitization and output encoding
- **CSRF Protection**: Built-in Flask security features

## 🧪 Testing

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app tests/
```

## 🚀 Deployment

### Development
The application runs on Flask's development server (port 5000) by default.

### Production
For production deployment:

1. **Use a production WSGI server** (Gunicorn, uWSGI)
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 run:app
   ```

2. **Set up a reverse proxy** (Nginx, Apache)

3. **Use environment variables** for configuration
   ```python
   app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
   app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
   ```

4. **Upgrade to PostgreSQL** for production database
   ```bash
   pip install psycopg2-binary
   ```

5. **Enable HTTPS** with SSL certificates

## 🔄 Future Enhancements

See [architecture.md](architecture.md) for detailed feature roadmap including:

- 🔔 Email and push notifications
- 👥 Team management and collaboration
- 📊 Advanced analytics and reporting
- 🔍 Full-text search and filtering
- 📅 Calendar integration
- 🔗 Task dependencies and subtasks
- 📎 File attachments
- 🎨 Customizable workflows
- 🤖 Automation and AI features
- 📱 Mobile applications
- 🌐 Internationalization

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide for Python code
- Write unit tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Asher-7**
- GitHub: [@Asher-7](https://github.com/Asher-7)
- Repository: [task-manager](https://github.com/Asher-7/task-manager)

## 🙏 Acknowledgments

- Flask framework and community
- SQLAlchemy ORM
- All contributors and users

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the [architecture documentation](architecture.md)

## 📊 Project Status

**Current Version**: 1.0.0  
**Status**: Active Development  
**Last Updated**: April 2026

---

**⭐ Star this repository if you find it helpful!**