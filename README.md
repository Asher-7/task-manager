# 📋 Task Manager

A full-stack task management web application built with Flask and vanilla JavaScript, featuring user authentication, project organization, real-time commenting, and comprehensive activity tracking.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.1.1-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### Core Functionality
- ✅ **Task Management**: Create, read, update, and delete tasks with rich metadata
- 🎯 **Priority Levels**: Organize tasks by urgency (Low, Medium, High, Urgent)
- 📊 **Status Tracking**: Monitor task progress (To Do, In Progress, Done)
- 📅 **Due Date Management**: Set deadlines and track overdue tasks
- 🗂️ **Project Organization**: Group related tasks into projects with custom colors

### Collaboration Features
- 💬 **Task Comments**: Discuss tasks with threaded comments
- 📝 **Activity Logging**: Comprehensive audit trail of all task changes
- 👥 **Task Assignment**: Assign tasks to specific users
- 🔔 **Real-time Updates**: See changes as they happen

### User Experience
- 🔐 **Secure Authentication**: User registration and login with password hashing
- 📈 **Statistics Dashboard**: Visual overview of task completion and status
- 🎨 **Modern UI**: Clean, gradient-themed interface with responsive design
- ⚡ **Fast Performance**: Single-page application with instant updates

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

## 📖 Usage Guide

### Getting Started

1. **Register an Account**
   - Enter username, email, and password
   - Click "Register" to create your account

2. **Create Your First Task**
   - Fill in the task title (required)
   - Add description, set priority, and choose status
   - Click "Create Task"

3. **Manage Tasks**
   - Click on any task to view details
   - Add comments to discuss the task
   - View activity history to see all changes

### Task Properties

| Property | Options | Description |
|----------|---------|-------------|
| **Title** | Text | Task name (required) |
| **Description** | Text | Detailed task information |
| **Status** | To Do, In Progress, Done | Current task state |
| **Priority** | Low, Medium, High, Urgent | Task importance level |
| **Due Date** | Date/Time | Task deadline (optional) |
| **Project** | Project name | Group tasks together |
| **Assigned To** | User | Task assignee |

### Statistics Dashboard

The dashboard provides real-time insights:
- **Total Tasks**: Overall task count
- **Status Breakdown**: Tasks by status (To Do, In Progress, Done)
- **Completion Rate**: Percentage of completed tasks
- **Overdue Tasks**: Tasks past their due date

## 🏗️ Architecture

### Technology Stack

**Backend:**
- **Flask 3.0.0**: Lightweight Python web framework
- **Flask-SQLAlchemy 3.1.1**: ORM for database operations
- **Werkzeug 3.0.1**: Password hashing and security
- **SQLite**: Embedded database (easily upgradeable to PostgreSQL)

**Frontend:**
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients and animations
- **Vanilla JavaScript**: No framework dependencies
- **Fetch API**: RESTful API communication

### Project Structure

```
task-manager/
├── app/
│   ├── __init__.py           # Flask application factory
│   ├── database.py           # SQLAlchemy configuration
│   ├── models.py             # Database models
│   └── routes/
│       ├── auth.py           # Authentication endpoints
│       ├── tasks.py          # Task management endpoints
│       ├── projects.py       # Project endpoints
│       └── comments.py       # Comments & activity endpoints
├── static/
│   └── index.html            # Single-page application
├── run.py                    # Application entry point
├── requirements.txt          # Python dependencies
├── ARCHITECTURE.md           # Detailed architecture documentation
└── README.md                 # This file
```

### Database Schema

The application uses 5 main models:

1. **User**: User accounts with authentication
2. **Task**: Core task entity with all properties
3. **Project**: Task grouping and organization
4. **Comment**: Task discussions and collaboration
5. **ActivityLog**: Audit trail of all changes

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed diagrams and relationships.

## 🔌 API Endpoints

### Authentication (`/auth`)
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `POST /auth/logout` - Logout user
- `GET /auth/me` - Get current user

### Tasks (`/tasks`)
- `GET /tasks/` - List all tasks (with filters)
- `POST /tasks/` - Create new task
- `GET /tasks/<id>` - Get task details
- `PUT /tasks/<id>` - Update task
- `DELETE /tasks/<id>` - Delete task
- `GET /tasks/stats` - Get statistics

### Projects (`/projects`)
- `GET /projects/` - List all projects
- `POST /projects/` - Create new project
- `GET /projects/<id>` - Get project with tasks
- `PUT /projects/<id>` - Update project
- `DELETE /projects/<id>` - Delete project

### Comments & Activity (`/api`)
- `GET /api/task/<id>/comments` - Get task comments
- `POST /api/task/<id>/comments` - Add comment
- `PUT /api/comments/<id>` - Update comment
- `DELETE /api/comments/<id>` - Delete comment
- `GET /api/task/<id>/activity` - Get activity log

## 🔒 Security Features

- **Password Hashing**: Werkzeug's PBKDF2 algorithm with automatic salting
- **Session Management**: Secure server-side sessions with Flask
- **Input Validation**: Server-side validation of all user inputs
- **SQL Injection Prevention**: SQLAlchemy ORM with parameterized queries
- **Authorization**: User ownership validation on all protected routes

## 🧪 Testing

Run the test suite:

```bash
pytest
```

The application includes pytest for testing. Tests cover:
- User authentication flows
- Task CRUD operations
- Comment functionality
- Activity logging
- API endpoint validation

## 🚀 Deployment

### Development
```bash
python run.py
```
Runs on `http://localhost:5000` with debug mode enabled.

### Production

1. **Update Configuration**
   ```python
   # In app/__init__.py
   app.config["SECRET_KEY"] = "your-secure-secret-key"
   app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@host/db"
   ```

2. **Use Production WSGI Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 run:app
   ```

3. **Set Up Reverse Proxy** (Nginx example)
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## 📊 Performance

- **Database**: SQLite for development, PostgreSQL recommended for production
- **Caching**: Consider Redis for session storage in production
- **Static Files**: Serve via CDN or Nginx for better performance
- **Scalability**: Horizontal scaling with multiple WSGI workers

## 🛠️ Configuration

### Environment Variables

```bash
# Optional configuration
export FLASK_ENV=production
export SECRET_KEY=your-secret-key
export DATABASE_URL=postgresql://user:pass@host/db
```

### Database Migration

To switch from SQLite to PostgreSQL:

1. Install PostgreSQL driver:
   ```bash
   pip install psycopg2-binary
   ```

2. Update database URI in `app/__init__.py`:
   ```python
   app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@host/db"
   ```

3. Run the application to create tables:
   ```bash
   python run.py
   ```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

## 🐛 Known Issues

- Session persistence requires cookies to be enabled
- Large file attachments not yet supported
- Real-time updates require page refresh

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] Real-time collaboration with WebSockets
- [ ] File attachments for tasks
- [ ] Email notifications
- [ ] Mobile responsive design
- [ ] Dark mode theme

### Version 3.0 (Future)
- [ ] Kanban board view
- [ ] Calendar integration
- [ ] Time tracking
- [ ] Advanced analytics
- [ ] API documentation (Swagger)

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed feature recommendations.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Asher Jacob**
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
- Review the [ARCHITECTURE.md](ARCHITECTURE.md) for technical details

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Architecture Documentation](ARCHITECTURE.md)

---

**Made with ❤️ using Flask and JavaScript**

*Last Updated: May 2026*
