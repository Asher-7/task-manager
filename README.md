# 📋 Task Manager

A modern, full-stack task management application built with Flask and vanilla JavaScript. Organize your work with projects, track progress with detailed statistics, collaborate through comments, and maintain a complete audit trail of all changes.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3.1.1-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🔐 User Management
- **Secure Authentication**: Register and login with password hashing
- **Session Management**: Persistent sessions across browser refreshes
- **User Profiles**: Track user information and activity

### 📝 Task Management
- **CRUD Operations**: Create, read, update, and delete tasks
- **Status Tracking**: Todo, In Progress, and Done states
- **Priority Levels**: Low, Medium, High, and Urgent priorities
- **Due Dates**: Set deadlines with automatic overdue detection
- **Task Assignment**: Assign tasks to specific users
- **Rich Descriptions**: Add detailed task descriptions

### 📊 Project Organization
- **Project Grouping**: Organize tasks into projects
- **Color Coding**: Visual project identification with custom colors
- **Task Counting**: Automatic task count per project
- **Project Management**: Full CRUD operations for projects

### 💬 Collaboration
- **Task Comments**: Discussion threads on each task
- **User Attribution**: Track who commented and when
- **Comment Management**: Edit and delete your own comments

### 📈 Analytics & Tracking
- **Statistics Dashboard**: Real-time metrics including:
  - Total tasks count
  - Tasks by status breakdown
  - Completion rate percentage
  - Overdue task tracking
- **Activity Logging**: Complete audit trail of all changes
  - Task creation and updates
  - Field-level change tracking (before/after values)
  - Comment activity
  - User attribution and timestamps

### 🎨 User Interface
- **Responsive Design**: Works on desktop and mobile devices
- **Modern Styling**: Gradient themes and smooth animations
- **Modal Dialogs**: Detailed task views with comments and activity
- **Real-time Updates**: Instant UI updates without page refresh
- **Color-coded Badges**: Visual status and priority indicators

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

4. **Open your browser**
   ```
   Navigate to: http://localhost:5000
   ```

That's it! The application will automatically create the SQLite database on first run.

## 📖 Usage Guide

### Getting Started

1. **Register an Account**
   - Open the application in your browser
   - Fill in username, email, and password
   - Click "Register"

2. **Create Your First Task**
   - After logging in, use the "Create New Task" form
   - Enter a title (required)
   - Add description, set priority and status
   - Click "Create Task"

3. **View Task Details**
   - Click on any task card to open the detail modal
   - View full task information
   - Add comments for discussion
   - See complete activity history

4. **Organize with Projects**
   - Create projects to group related tasks
   - Assign tasks to projects when creating or editing
   - View all tasks in a project

### Task Workflow

```
Create Task → Set Priority → Assign to Project → Work on Task → Add Comments → Mark as Done
```

### Status Progression

```
Todo → In Progress → Done
```

## 🏗️ Architecture

### Technology Stack

**Backend:**
- **Flask 3.0.0**: Lightweight Python web framework
- **Flask-SQLAlchemy 3.1.1**: ORM for database operations
- **Werkzeug 3.0.1**: Password hashing and security
- **SQLite**: Embedded database (no separate server needed)

**Frontend:**
- **HTML5**: Semantic markup
- **CSS3**: Custom styling with gradients and animations
- **Vanilla JavaScript**: No frameworks, pure ES6+
- **Fetch API**: RESTful API communication

### Project Structure

```
task-manager/
├── run.py                      # Application entry point
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── ARCHITECTURE.md             # Detailed architecture documentation
│
├── app/                        # Main application package
│   ├── __init__.py            # App factory and configuration
│   ├── database.py            # Database instance
│   ├── models.py              # SQLAlchemy models
│   │
│   └── routes/                # API endpoints
│       ├── auth.py           # Authentication routes
│       ├── tasks.py          # Task management routes
│       ├── projects.py       # Project management routes
│       └── comments.py       # Comments and activity routes
│
└── static/                    # Frontend files
    └── index.html            # Single-page application
```

### Database Schema

The application uses five main tables:

- **Users**: User accounts and authentication
- **Projects**: Project organization
- **Tasks**: Core task data with status and priority
- **Comments**: Task discussion threads
- **ActivityLogs**: Complete audit trail

For detailed architecture diagrams and data flow, see [`ARCHITECTURE.md`](ARCHITECTURE.md).

## 🔌 API Reference

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Create new user account |
| POST | `/auth/login` | Authenticate user |
| POST | `/auth/logout` | End user session |
| GET | `/auth/me` | Get current user info |

### Task Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks/` | List all tasks (with filters) |
| POST | `/tasks/` | Create new task |
| GET | `/tasks/:id` | Get task details |
| PUT | `/tasks/:id` | Update task |
| DELETE | `/tasks/:id` | Delete task |
| GET | `/tasks/stats` | Get statistics |

**Query Parameters for GET /tasks/:**
- `status`: Filter by status (todo, in_progress, done)
- `priority`: Filter by priority (low, medium, high, urgent)
- `project_id`: Filter by project
- `assigned_to_me`: Show only assigned tasks (true/false)

### Project Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/projects/` | List all projects |
| POST | `/projects/` | Create new project |
| GET | `/projects/:id` | Get project with tasks |
| PUT | `/projects/:id` | Update project |
| DELETE | `/projects/:id` | Delete project |

### Comment & Activity Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/task/:id/comments` | Get task comments |
| POST | `/api/task/:id/comments` | Add comment |
| PUT | `/api/comments/:id` | Update comment |
| DELETE | `/api/comments/:id` | Delete comment |
| GET | `/api/task/:id/activity` | Get activity log |

## 🔒 Security Features

- **Password Hashing**: Werkzeug PBKDF2 password hashing
- **Session Management**: Secure Flask sessions with secret key
- **Authentication Required**: All API endpoints require authentication
- **Ownership Verification**: Users can only access their own tasks
- **Input Validation**: Server-side validation of all inputs
- **SQL Injection Prevention**: SQLAlchemy ORM with parameterized queries

## 🧪 Testing

Run the test suite:

```bash
pytest
```

The application includes tests for:
- Client endpoint functionality
- Error handling
- Authentication flows
- Task operations

## 📊 Statistics Dashboard

The dashboard provides real-time insights:

- **Total Tasks**: Count of all your tasks
- **By Status**: Breakdown of todo, in progress, and done
- **Completion Rate**: Percentage of completed tasks
- **Overdue Tasks**: Tasks past their due date

## 💡 Usage Examples

### Creating a Task via API

```bash
curl -X POST http://localhost:5000/tasks/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Implement new feature",
    "description": "Add user profile page",
    "priority": "high",
    "status": "todo",
    "due_date": "2026-05-01T12:00:00"
  }'
```

### Filtering Tasks

```bash
# Get all high priority tasks
curl http://localhost:5000/tasks/?priority=high

# Get all tasks in progress
curl http://localhost:5000/tasks/?status=in_progress

# Get tasks assigned to me
curl http://localhost:5000/tasks/?assigned_to_me=true
```

### Adding a Comment

```bash
curl -X POST http://localhost:5000/api/task/1/comments \
  -H "Content-Type: application/json" \
  -d '{
    "content": "This looks great! Ready to merge."
  }'
```

## 🎯 Use Cases

### Personal Task Management
- Track daily todos and long-term goals
- Organize tasks by project or category
- Monitor completion rates and productivity

### Team Collaboration
- Assign tasks to team members
- Discuss tasks through comments
- Track who changed what and when

### Project Planning
- Break down projects into tasks
- Set priorities and deadlines
- Monitor project progress

### Audit & Compliance
- Complete activity log of all changes
- Track task lifecycle from creation to completion
- Maintain accountability with user attribution

## 🔧 Configuration

### Environment Variables

Create a `.env` file for production:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
DATABASE_URI=sqlite:///tasks.db
```

### Database Configuration

The default configuration uses SQLite. To use PostgreSQL or MySQL:

```python
# In app/__init__.py
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:pass@localhost/taskdb"
```

## 🚀 Deployment

### Development

```bash
python run.py
```

### Production

1. **Use a production WSGI server:**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

2. **Set up a reverse proxy (Nginx example):**
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;
       
       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
       
       location /static {
           alias /path/to/task-manager/static;
       }
   }
   ```

3. **Use environment variables for sensitive data**
4. **Enable HTTPS with SSL certificates**
5. **Use a production database (PostgreSQL, MySQL)**

## 🐛 Troubleshooting

### Database Issues

**Problem**: Database not found
```bash
# Solution: Delete and recreate
rm tasks.db
python run.py
```

**Problem**: Migration errors
```bash
# Solution: Fresh start
rm -rf migrations/
flask db init
flask db migrate
flask db upgrade
```

### Authentication Issues

**Problem**: Can't log in after registration
- Check that cookies are enabled in your browser
- Verify SECRET_KEY is set in configuration
- Clear browser cookies and try again

### Performance Issues

**Problem**: Slow task loading
- Add pagination to task lists
- Implement caching for statistics
- Add database indexes on foreign keys

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Flask framework and community
- SQLAlchemy ORM
- All contributors and users

## 📧 Contact

- **GitHub**: [@Asher-7](https://github.com/Asher-7)
- **Repository**: [task-manager](https://github.com/Asher-7/task-manager)

## 🗺️ Roadmap

### Planned Features

- [ ] **Real-time Updates**: WebSocket support for live collaboration
- [ ] **File Attachments**: Upload files to tasks
- [ ] **Email Notifications**: Get notified of task updates
- [ ] **Advanced Filtering**: More filter options and saved filters
- [ ] **Task Templates**: Create tasks from templates
- [ ] **Time Tracking**: Log time spent on tasks
- [ ] **Recurring Tasks**: Automatic task creation on schedule
- [ ] **Mobile App**: Native iOS and Android apps
- [ ] **API Documentation**: Interactive API docs with Swagger
- [ ] **Export/Import**: Export tasks to CSV/JSON
- [ ] **Dark Mode**: Theme switching
- [ ] **Keyboard Shortcuts**: Power user features
- [ ] **Task Dependencies**: Link related tasks
- [ ] **Gantt Charts**: Visual project timeline
- [ ] **Calendar View**: See tasks on a calendar

### Version History

**v1.0.0** (Current)
- Initial release
- Core task management features
- User authentication
- Project organization
- Comments and activity logging
- Statistics dashboard

## 📚 Additional Resources

- [Architecture Documentation](ARCHITECTURE.md) - Detailed technical architecture
- [API Documentation](#api-reference) - Complete API reference
- [Flask Documentation](https://flask.palletsprojects.com/) - Flask framework docs
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) - ORM documentation

## 💻 Development Setup

### Setting up Development Environment

1. **Clone and setup:**
   ```bash
   git clone https://github.com/Asher-7/task-manager.git
   cd task-manager
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run in debug mode:**
   ```bash
   export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
   python run.py
   ```

3. **Access the application:**
   - Main app: http://localhost:5000
   - API endpoints: http://localhost:5000/tasks/, etc.

### Database Management

```bash
# View database
sqlite3 tasks.db

# Common queries
.tables                          # List all tables
SELECT * FROM users;            # View users
SELECT * FROM tasks;            # View tasks
SELECT * FROM activity_logs;    # View activity
```

## 🎓 Learning Resources

This project demonstrates:
- RESTful API design
- Flask application structure
- SQLAlchemy ORM usage
- Session-based authentication
- Single-page application patterns
- Activity logging and audit trails
- Responsive web design

Perfect for learning full-stack web development with Python!

---

**Made with ❤️ using Flask and JavaScript**

⭐ Star this repository if you find it helpful!
