# 📋 Task Manager

A full-stack task management application built with Flask and vanilla JavaScript, featuring comprehensive task tracking, project organization, comments, and activity logging.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### Core Functionality
- 🔐 **User Authentication** - Secure registration and login with password hashing
- ✅ **Task Management** - Create, read, update, and delete tasks
- 📊 **Project Organization** - Group tasks into color-coded projects
- 💬 **Comments System** - Collaborate with threaded comments on tasks
- 📝 **Activity Logging** - Complete audit trail of all task changes
- 📈 **Statistics Dashboard** - Real-time task analytics and completion rates

### Task Features
- **Priority Levels**: Low, Medium, High, Urgent
- **Status Tracking**: To Do, In Progress, Done
- **Due Dates**: Set deadlines and track overdue tasks
- **Task Assignment**: Assign tasks to users
- **Detailed Descriptions**: Rich task information
- **Timestamps**: Track creation, updates, and completion times

### Collaboration
- **Comments**: Add, edit, and delete comments on tasks
- **Activity Feed**: See who changed what and when
- **User Tracking**: Know who created and is assigned to each task

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
   http://localhost:5000
   ```

The application will automatically create the SQLite database on first run.

## 📁 Project Structure

```
task-manager/
│
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── database.py           # Database configuration
│   ├── models.py             # Data models (User, Task, Project, etc.)
│   │
│   └── routes/
│       ├── __init__.py
│       ├── auth.py           # Authentication endpoints
│       ├── tasks.py          # Task CRUD operations
│       ├── projects.py       # Project management
│       └── comments.py       # Comments & activity log
│
├── static/
│   └── index.html            # Single-page application frontend
│
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
├── architecture.md           # Detailed architecture documentation
└── README.md                 # This file
```

## 🔧 Technology Stack

### Backend
- **Flask 3.0.0** - Web framework
- **Flask-SQLAlchemy 3.1.1** - ORM for database operations
- **Werkzeug 3.0.1** - Password hashing and security utilities
- **SQLite** - Lightweight database

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with gradient themes
- **Vanilla JavaScript** - No frameworks, pure ES6+
- **Fetch API** - HTTP requests

### Testing
- **pytest 8.0.0** - Testing framework

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
GET /tasks/?status=todo&priority=high&project_id=1
```

Query Parameters:
- `status` - Filter by status (todo, in_progress, done)
- `priority` - Filter by priority (low, medium, high, urgent)
- `project_id` - Filter by project
- `assigned_to_me` - Show only assigned tasks (true/false)

#### Create Task
```http
POST /tasks/
Content-Type: application/json

{
  "title": "Implement new feature",
  "description": "Add user profile page",
  "status": "todo",
  "priority": "high",
  "due_date": "2026-05-20T10:00:00Z",
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

Returns:
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
    "medium": 10,
    "high": 7,
    "urgent": 3
  },
  "overdue": 2,
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
  "color": "#ff6b6b"
}
```

#### Delete Project
```http
DELETE /projects/{id}
```

### Comment Endpoints

#### Get Task Comments
```http
GET /api/task/{task_id}/comments
```

#### Add Comment
```http
POST /api/task/{task_id}/comments
Content-Type: application/json

{
  "content": "This looks great! Let's proceed."
}
```

#### Update Comment
```http
PUT /api/comments/{id}
Content-Type: application/json

{
  "content": "Updated comment text"
}
```

#### Delete Comment
```http
DELETE /api/comments/{id}
```

#### Get Task Activity Log
```http
GET /api/task/{task_id}/activity
```

## 🗄️ Database Schema

### Models

**User**
- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `password_hash` - Hashed password
- `created_at` - Registration timestamp

**Task**
- `id` - Primary key
- `title` - Task title
- `description` - Detailed description
- `status` - todo, in_progress, done
- `priority` - low, medium, high, urgent
- `due_date` - Optional deadline
- `project_id` - Foreign key to Project
- `created_by` - Foreign key to User (creator)
- `assigned_to` - Foreign key to User (assignee)
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp
- `completed_at` - Completion timestamp

**Project**
- `id` - Primary key
- `name` - Project name
- `description` - Project description
- `color` - Hex color code
- `created_at` - Creation timestamp

**Comment**
- `id` - Primary key
- `content` - Comment text
- `task_id` - Foreign key to Task
- `user_id` - Foreign key to User
- `created_at` - Creation timestamp
- `updated_at` - Last update timestamp

**ActivityLog**
- `id` - Primary key
- `task_id` - Foreign key to Task
- `user_id` - Foreign key to User
- `action` - Action type (created, updated, commented, etc.)
- `field_name` - Changed field name
- `old_value` - Previous value
- `new_value` - New value
- `created_at` - Action timestamp

### Relationships
- User → Tasks (1:N) - created_by
- User → Tasks (1:N) - assigned_to
- User → Comments (1:N)
- User → ActivityLog (1:N)
- Project → Tasks (1:N)
- Task → Comments (1:N, cascade delete)
- Task → ActivityLog (1:N, cascade delete)

## 🎨 User Interface

### Authentication Screen
- Clean login/registration form
- Email and password validation
- Session-based authentication

### Main Dashboard
- **Statistics Cards**: Total tasks, status breakdown, completion rate
- **Task Creation Form**: Quick task entry with all fields
- **Task List**: Scrollable list of all tasks with status badges
- **Task Cards**: Click to open detailed modal

### Task Details Modal
- Complete task information
- Comments section with add/edit/delete
- Activity log showing all changes
- User-friendly timestamps

### Design Features
- Modern gradient background (purple theme)
- Responsive card-based layout
- Color-coded status and priority badges
- Smooth animations and transitions
- Modal dialogs for detailed views

## 🔒 Security Features

- **Password Hashing**: Werkzeug secure password hashing
- **Session Management**: Flask server-side sessions
- **Authorization**: User-based resource access control
- **Input Validation**: Server-side validation for all inputs
- **SQL Injection Protection**: SQLAlchemy ORM parameterized queries

## 🧪 Testing

Run tests with pytest:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app tests/
```

## 📊 Activity Logging

The application tracks all task-related activities:

- **Task Creation**: Who created the task and when
- **Field Updates**: What changed, from what to what
- **Status Changes**: Track task progression
- **Comments**: All comment additions, edits, and deletions
- **User Actions**: Complete audit trail with timestamps

Example activity log entry:
```json
{
  "id": 1,
  "task_id": 5,
  "user_id": 2,
  "username": "john_doe",
  "action": "updated",
  "field_name": "status",
  "old_value": "todo",
  "new_value": "in_progress",
  "created_at": "2026-05-13T10:30:00Z"
}
```

## 🚀 Deployment

### Development
```bash
python run.py
```
Runs on `http://localhost:5000` with debug mode enabled.

### Production

1. **Set production configuration**
   ```python
   app.config["DEBUG"] = False
   app.config["SECRET_KEY"] = "your-secure-secret-key"
   ```

2. **Use production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
   ```

3. **Database**: Consider migrating to PostgreSQL or MySQL for production

4. **Environment Variables**: Use environment variables for sensitive configuration

## 🔮 Future Enhancements

See [architecture.md](architecture.md) for detailed feature roadmap including:

- Task search and advanced filtering
- Due date reminders and notifications
- Task tags and labels
- Subtasks and checklists
- File attachments
- Kanban board view
- Time tracking
- Team workspaces
- Real-time collaboration
- Mobile app
- Calendar integration
- And more...

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Asher-7**
- GitHub: [@Asher-7](https://github.com/Asher-7)

## 🙏 Acknowledgments

- Flask documentation and community
- SQLAlchemy for excellent ORM
- All contributors and users

## 📞 Support

For support, please open an issue in the GitHub repository.

---

**Made with ❤️ using Flask and JavaScript**