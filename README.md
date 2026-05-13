# 📋 Task Manager

A full-stack task management web application built with Flask and vanilla JavaScript. Manage tasks, projects, and team collaboration with an intuitive interface and powerful features.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### Core Functionality
- 🔐 **User Authentication** - Secure registration and login with password hashing
- ✅ **Task Management** - Create, update, delete tasks with rich metadata
- 📊 **Project Organization** - Group tasks into color-coded projects
- 💬 **Comments & Collaboration** - Discuss tasks with team members
- 📈 **Activity Tracking** - Complete audit trail of all changes
- 📉 **Statistics Dashboard** - Real-time insights into task completion

### Task Features
- **Status Tracking**: Todo, In Progress, Done
- **Priority Levels**: Low, Medium, High, Urgent
- **Due Dates**: Set deadlines and track overdue tasks
- **Assignments**: Assign tasks to team members
- **Descriptions**: Rich text descriptions for detailed context

### Collaboration
- **Comments**: Thread discussions on tasks
- **Activity Log**: See who changed what and when
- **User Management**: Multiple users with individual accounts

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
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── database.py          # SQLAlchemy configuration
│   ├── models.py            # Database models
│   └── routes/
│       ├── auth.py          # Authentication endpoints
│       ├── tasks.py         # Task management endpoints
│       ├── projects.py      # Project management endpoints
│       └── comments.py      # Comments & activity endpoints
├── static/
│   └── index.html           # Frontend single-page application
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
├── ARCHITECTURE.md          # Detailed architecture documentation
└── FEATURE_ROADMAP.md       # Future feature plans
```

## 🏗️ Architecture

### Technology Stack

**Backend**
- **Flask 3.0.0** - Web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Lightweight database
- **Werkzeug** - Password hashing and security

**Frontend**
- **HTML5** - Structure
- **CSS3** - Styling with gradient design
- **Vanilla JavaScript** - Client-side logic
- **Fetch API** - HTTP requests

### Architecture Layers

```
┌─────────────────────────────────────┐
│         Client Layer                │
│  (HTML, CSS, JavaScript)            │
└──────────────┬──────────────────────┘
               │ HTTP/JSON
┌──────────────▼──────────────────────┐
│      Application Layer              │
│  (Flask Blueprints & Routes)        │
│  - Authentication                   │
│  - Task Management                  │
│  - Project Management               │
│  - Comments & Activity              │
└──────────────┬──────────────────────┘
               │ SQLAlchemy ORM
┌──────────────▼──────────────────────┐
│         Data Layer                  │
│  (SQLite Database)                  │
│  - Users, Tasks, Projects           │
│  - Comments, Activity Logs          │
└─────────────────────────────────────┘
```

For detailed architecture diagrams and documentation, see [ARCHITECTURE.md](ARCHITECTURE.md).

## 📊 Database Schema

The application uses 5 main models:

- **User** - User accounts and authentication
- **Project** - Project containers for tasks
- **Task** - Individual tasks with metadata
- **Comment** - Task comments and discussions
- **ActivityLog** - Audit trail of all changes

See [ARCHITECTURE.md](ARCHITECTURE.md) for the complete entity-relationship diagram.

## 🔌 API Endpoints

### Authentication (`/auth`)
- `POST /auth/register` - Register new user
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout
- `GET /auth/me` - Get current user

### Tasks (`/tasks`)
- `GET /tasks/` - List tasks (with filters)
- `POST /tasks/` - Create task
- `GET /tasks/:id` - Get task details
- `PUT /tasks/:id` - Update task
- `DELETE /tasks/:id` - Delete task
- `GET /tasks/stats` - Get statistics

### Projects (`/projects`)
- `GET /projects/` - List projects
- `POST /projects/` - Create project
- `GET /projects/:id` - Get project
- `PUT /projects/:id` - Update project
- `DELETE /projects/:id` - Delete project

### Comments & Activity (`/api`)
- `GET /api/task/:id/comments` - Get comments
- `POST /api/task/:id/comments` - Add comment
- `PUT /api/comments/:id` - Update comment
- `DELETE /api/comments/:id` - Delete comment
- `GET /api/task/:id/activity` - Get activity log

## 🎯 Usage

### Creating Your First Task

1. **Register/Login** - Create an account or log in
2. **Create a Task** - Fill in the task form with:
   - Title (required)
   - Description (optional)
   - Priority (low, medium, high, urgent)
   - Status (todo, in progress, done)
3. **View Tasks** - See all your tasks in the list
4. **Click a Task** - View details, add comments, see activity

### Managing Projects

1. Navigate to Projects section
2. Create a new project with name, description, and color
3. Assign tasks to projects when creating/editing tasks
4. View project statistics and task counts

### Collaboration

1. **Comments** - Click any task to add comments
2. **Activity Log** - See all changes made to a task
3. **Assignments** - Assign tasks to team members
4. **Tracking** - Monitor who's working on what

## 🔒 Security Features

- **Password Hashing** - Werkzeug security for password storage
- **Session Management** - Secure Flask sessions
- **Authentication Required** - All API endpoints require login
- **Authorization** - Users can only access their own tasks
- **SQL Injection Protection** - SQLAlchemy ORM prevents SQL injection

## 🧪 Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app tests/
```

## 🚀 Future Features

We have an extensive roadmap of 30+ features planned! See [FEATURE_ROADMAP.md](FEATURE_ROADMAP.md) for details.

### Coming Soon
- Task dependencies and subtasks
- File attachments
- Real-time notifications
- Task templates
- Advanced search and filters
- Kanban board view
- Time tracking
- Calendar view

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

If you have any questions or run into issues, please open an issue on GitHub.

---

**Made with ❤️ using Flask and JavaScript**
