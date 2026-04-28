# Task Manager Application

A full-featured task management web application built with Flask and vanilla JavaScript. Manage your tasks, projects, and collaborate with team members efficiently.

## Features

- 🔐 **User Authentication** - Secure registration and login system
- 📋 **Task Management** - Create, update, delete, and organize tasks
- 📁 **Project Organization** - Group tasks into projects with custom colors
- 💬 **Comments** - Add comments to tasks for collaboration
- 🎯 **Priority Levels** - Set task priorities (low, medium, high, urgent)
- 📅 **Due Dates** - Track deadlines and overdue tasks
- 📊 **Status Tracking** - Monitor task progress (todo, in_progress, done)
- 👥 **Task Assignment** - Assign tasks to team members
- 📝 **Activity Logs** - Track all changes and updates to tasks
- 🎨 **Modern UI** - Clean, responsive interface with gradient design

## Tech Stack

### Backend
- **Flask 3.0.0** - Python web framework
- **Flask-SQLAlchemy 3.1.1** - ORM for database operations
- **SQLite** - Lightweight database
- **Werkzeug 3.0.1** - WSGI utilities and password hashing

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern gradients
- **Vanilla JavaScript** - Interactive functionality

### Testing
- **Pytest 8.0.0** - Testing framework

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Asher-7/task-manager.git
cd task-manager
```

2. Create a virtual environment (recommended):
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

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
task-manager/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── database.py          # Database configuration
│   ├── models.py            # Database models (User, Task, Project, Comment, ActivityLog)
│   └── routes/
│       ├── __init__.py
│       ├── auth.py          # Authentication endpoints
│       ├── tasks.py         # Task management endpoints
│       ├── projects.py      # Project management endpoints
│       └── comments.py      # Comment endpoints
├── static/
│   └── index.html           # Frontend interface
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Database Models

### User
- User authentication and profile information
- Relationships with tasks (created and assigned)

### Project
- Project organization with custom colors
- One-to-many relationship with tasks

### Task
- Core task entity with title, description, status, priority
- Due dates and completion tracking
- Relationships with users, projects, comments, and activity logs

### Comment
- Task comments for collaboration
- Linked to users and tasks

### ActivityLog
- Audit trail of all task changes
- Tracks field changes with old and new values

## API Endpoints

### Authentication (`/auth`)
- `POST /auth/register` - Register new user
- `POST /auth/login` - User login

### Tasks (`/tasks`)
- `GET /tasks` - List all tasks
- `POST /tasks` - Create new task
- `GET /tasks/<id>` - Get task details
- `PUT /tasks/<id>` - Update task
- `DELETE /tasks/<id>` - Delete task

### Projects (`/projects`)
- `GET /projects` - List all projects
- `POST /projects` - Create new project
- `GET /projects/<id>` - Get project details
- `PUT /projects/<id>` - Update project
- `DELETE /projects/<id>` - Delete project

### Comments (`/api`)
- `GET /api/tasks/<id>/comments` - Get task comments
- `POST /api/tasks/<id>/comments` - Add comment
- `PUT /api/comments/<id>` - Update comment
- `DELETE /api/comments/<id>` - Delete comment

## Configuration

The application uses the following default configuration:
- **Database**: SQLite (`tasks.db`)
- **Port**: 5000
- **Debug Mode**: Enabled (development only)
- **Secret Key**: `dev-secret-key` (change in production!)

## Development

### Running Tests
```bash
pytest
```

### Database
The SQLite database (`tasks.db`) is automatically created on first run. To reset the database, simply delete the file and restart the application.

## Security Notes

⚠️ **Important for Production:**
- Change the `SECRET_KEY` in `app/__init__.py`
- Disable debug mode in `run.py`
- Use a production-grade database (PostgreSQL, MySQL)
- Implement proper password hashing validation
- Add HTTPS support
- Implement rate limiting
- Add CSRF protection

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

**Asher-7**
- GitHub: [@Asher-7](https://github.com/Asher-7)

## Acknowledgments

- Built with Flask framework
- Inspired by modern task management tools
- UI design influenced by contemporary web design trends

---

**Happy Task Managing! 🚀**
