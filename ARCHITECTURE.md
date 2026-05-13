# Task Manager - Architecture Documentation

## System Overview

The Task Manager is a full-stack web application built with Flask (Python) backend and vanilla JavaScript frontend. It provides comprehensive task management capabilities with user authentication, project organization, commenting, and activity tracking.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           CLIENT LAYER                                   │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                     Static Frontend (HTML/CSS/JS)                  │  │
│  │                        index.html                                  │  │
│  │  - User Interface                                                  │  │
│  │  - Form Handling                                                   │  │
│  │  - API Communication                                               │  │
│  └───────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ HTTP/HTTPS
                                    │ REST API Calls
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        APPLICATION LAYER                                 │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                      Flask Application                             │  │
│  │                      (app/__init__.py)                             │  │
│  │  - Application Factory Pattern                                     │  │
│  │  - Blueprint Registration                                          │  │
│  │  - Database Initialization                                         │  │
│  │  - Session Management                                              │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                    │                                     │
│         ┌──────────────────────────┼──────────────────────────┐         │
│         │                          │                          │         │
│         ▼                          ▼                          ▼         │
│  ┌─────────────┐          ┌─────────────┐          ┌─────────────┐    │
│  │   Auth BP   │          │  Tasks BP   │          │ Projects BP │    │
│  │ /auth/*     │          │ /tasks/*    │          │ /projects/* │    │
│  │             │          │             │          │             │    │
│  │ - register  │          │ - list      │          │ - list      │    │
│  │ - login     │          │ - create    │          │ - create    │    │
│  │ - logout    │          │ - get       │          │ - get       │    │
│  │ - me        │          │ - update    │          │ - update    │    │
│  │             │          │ - delete    │          │ - delete    │    │
│  │             │          │ - stats     │          │             │    │
│  └─────────────┘          └─────────────┘          └─────────────┘    │
│         │                          │                          │         │
│         │                          ▼                          │         │
│         │                  ┌─────────────┐                    │         │
│         │                  │ Comments BP │                    │         │
│         │                  │ /api/*      │                    │         │
│         │                  │             │                    │         │
│         │                  │ - get       │                    │         │
│         │                  │ - create    │                    │         │
│         │                  │ - update    │                    │         │
│         │                  │ - delete    │                    │         │
│         │                  │ - activity  │                    │         │
│         │                  └─────────────┘                    │         │
│         │                          │                          │         │
│         └──────────────────────────┼──────────────────────────┘         │
│                                    │                                     │
│                                    ▼                                     │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ SQLAlchemy ORM
                                    │
┌─────────────────────────────────────────────────────────────────────────┐
│                          DATA ACCESS LAYER                               │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                    SQLAlchemy Models                               │  │
│  │                    (app/models.py)                                 │  │
│  │                                                                    │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐         │  │
│  │  │   User   │  │ Project  │  │   Task   │  │ Comment  │         │  │
│  │  ├──────────┤  ├──────────┤  ├──────────┤  ├──────────┤         │  │
│  │  │ id       │  │ id       │  │ id       │  │ id       │         │  │
│  │  │ username │  │ name     │  │ title    │  │ content  │         │  │
│  │  │ email    │  │ desc     │  │ desc     │  │ task_id  │         │  │
│  │  │ password │  │ color    │  │ status   │  │ user_id  │         │  │
│  │  │ created  │  │ created  │  │ priority │  │ created  │         │  │
│  │  └──────────┘  └──────────┘  │ due_date │  │ updated  │         │  │
│  │                               │ proj_id  │  └──────────┘         │  │
│  │                               │ created  │                        │  │
│  │                               │ assigned │  ┌──────────────┐     │  │
│  │                               │ updated  │  │ ActivityLog  │     │  │
│  │                               │ complete │  ├──────────────┤     │  │
│  │                               └──────────┘  │ id           │     │  │
│  │                                             │ task_id      │     │  │
│  │                                             │ user_id      │     │  │
│  │                                             │ action       │     │  │
│  │                                             │ field_name   │     │  │
│  │                                             │ old_value    │     │  │
│  │                                             │ new_value    │     │  │
│  │                                             │ created_at   │     │  │
│  │                                             └──────────────┘     │  │
│  └───────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ SQL Queries
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         PERSISTENCE LAYER                                │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                      SQLite Database                               │  │
│  │                      (tasks.db)                                    │  │
│  │                                                                    │  │
│  │  Tables: users, projects, tasks, comments, activity_logs          │  │
│  └───────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Client Layer

**Technology**: HTML5, CSS3, Vanilla JavaScript

**Responsibilities**:
- Render user interface
- Handle user interactions
- Make HTTP requests to backend API
- Display data received from server
- Client-side form validation

**Key Files**:
- `static/index.html` - Single-page application interface

### 2. Application Layer

**Technology**: Flask 3.0.0, Python

**Responsibilities**:
- Route HTTP requests to appropriate handlers
- Business logic implementation
- Authentication and authorization
- Session management
- Request/response processing

**Key Components**:

#### Flask Application Factory (`app/__init__.py`)
- Creates and configures Flask application
- Initializes database connection
- Registers blueprints
- Sets up static file serving
- Configures session management

#### Authentication Blueprint (`app/routes/auth.py`)
**Endpoints**:
- `POST /auth/register` - User registration
- `POST /auth/login` - User authentication
- `POST /auth/logout` - Session termination
- `GET /auth/me` - Get current user info

**Features**:
- Password hashing with Werkzeug
- Session-based authentication
- Duplicate username/email validation

#### Tasks Blueprint (`app/routes/tasks.py`)
**Endpoints**:
- `GET /tasks/` - List tasks with filtering
- `POST /tasks/` - Create new task
- `GET /tasks/<id>` - Get specific task
- `PUT /tasks/<id>` - Update task
- `DELETE /tasks/<id>` - Delete task
- `GET /tasks/stats` - Get task statistics

**Features**:
- Status filtering (todo, in_progress, done)
- Priority filtering (low, medium, high, urgent)
- Project-based filtering
- Assignment filtering
- Automatic activity logging
- Overdue task detection
- Completion tracking

#### Projects Blueprint (`app/routes/projects.py`)
**Endpoints**:
- `GET /projects/` - List all projects
- `POST /projects/` - Create new project
- `GET /projects/<id>` - Get project with tasks
- `PUT /projects/<id>` - Update project
- `DELETE /projects/<id>` - Delete project

**Features**:
- Project organization
- Color coding
- Task count tracking
- Cascade deletion of associated tasks

#### Comments Blueprint (`app/routes/comments.py`)
**Endpoints**:
- `GET /api/task/<id>/comments` - Get task comments
- `POST /api/task/<id>/comments` - Add comment
- `PUT /api/comments/<id>` - Update comment
- `DELETE /api/comments/<id>` - Delete comment
- `GET /api/task/<id>/activity` - Get activity log

**Features**:
- Threaded comments on tasks
- Activity logging for comments
- User attribution
- Timestamp tracking

### 3. Data Access Layer

**Technology**: SQLAlchemy 3.1.1

**Responsibilities**:
- Object-Relational Mapping (ORM)
- Database schema definition
- Relationship management
- Data validation
- Query abstraction

**Models**:

#### User Model
```python
- id: Integer (Primary Key)
- username: String(80) (Unique)
- email: String(120) (Unique)
- password_hash: String(256)
- created_at: DateTime
```

**Relationships**:
- One-to-Many with Task (as creator)
- One-to-Many with Task (as assignee)
- One-to-Many with Comment
- One-to-Many with ActivityLog

#### Project Model
```python
- id: Integer (Primary Key)
- name: String(120)
- description: Text
- color: String(7) (Hex color)
- created_at: DateTime
```

**Relationships**:
- One-to-Many with Task (cascade delete)

#### Task Model
```python
- id: Integer (Primary Key)
- title: String(200)
- description: Text
- status: String(20) [todo, in_progress, done]
- priority: String(10) [low, medium, high, urgent]
- due_date: DateTime
- project_id: Integer (Foreign Key)
- created_by: Integer (Foreign Key)
- assigned_to: Integer (Foreign Key)
- created_at: DateTime
- updated_at: DateTime
- completed_at: DateTime
```

**Relationships**:
- Many-to-One with Project
- Many-to-One with User (creator)
- Many-to-One with User (assignee)
- One-to-Many with Comment (cascade delete)
- One-to-Many with ActivityLog (cascade delete)

**Methods**:
- `is_overdue()` - Check if task is past due date

#### Comment Model
```python
- id: Integer (Primary Key)
- content: Text
- task_id: Integer (Foreign Key)
- user_id: Integer (Foreign Key)
- created_at: DateTime
- updated_at: DateTime
```

**Relationships**:
- Many-to-One with Task
- Many-to-One with User

#### ActivityLog Model
```python
- id: Integer (Primary Key)
- task_id: Integer (Foreign Key)
- user_id: Integer (Foreign Key)
- action: String(50) [created, updated, commented, etc.]
- field_name: String(50)
- old_value: Text
- new_value: Text
- created_at: DateTime
```

**Relationships**:
- Many-to-One with Task
- Many-to-One with User

### 4. Persistence Layer

**Technology**: SQLite

**Responsibilities**:
- Data storage
- ACID transactions
- Query execution
- Data integrity

**Database File**: `tasks.db`

**Tables**:
- users
- projects
- tasks
- comments
- activity_logs

## Data Flow

### Example: Creating a Task

```
1. User fills form in frontend (index.html)
   ↓
2. JavaScript sends POST request to /tasks/
   ↓
3. Flask routes request to tasks_bp.create_task()
   ↓
4. Route handler validates data and checks authentication
   ↓
5. Creates Task model instance with SQLAlchemy
   ↓
6. Creates ActivityLog entry for audit trail
   ↓
7. SQLAlchemy commits to SQLite database
   ↓
8. Returns JSON response with created task
   ↓
9. Frontend updates UI with new task
```

### Example: User Authentication Flow

```
1. User submits login form
   ↓
2. POST /auth/login with credentials
   ↓
3. auth_bp.login() validates credentials
   ↓
4. Werkzeug checks password hash
   ↓
5. Session created with user_id
   ↓
6. User data returned to frontend
   ↓
7. Frontend stores session and updates UI
```

## Security Features

1. **Password Security**
   - Passwords hashed using Werkzeug's `generate_password_hash`
   - Never stored in plain text

2. **Session Management**
   - Server-side sessions with Flask
   - Session-based authentication
   - Secure session cookies

3. **Authorization**
   - User ownership validation on all operations
   - Users can only access their own tasks
   - Session validation on protected routes

4. **Input Validation**
   - Required field validation
   - Status/priority enum validation
   - Duplicate username/email checks

## API Design Patterns

1. **RESTful Architecture**
   - Resource-based URLs
   - HTTP methods (GET, POST, PUT, DELETE)
   - JSON request/response format

2. **Blueprint Organization**
   - Modular route organization
   - Separation of concerns
   - URL prefix namespacing

3. **Consistent Response Format**
   - JSON responses
   - HTTP status codes
   - Error messages in JSON

4. **Activity Logging**
   - Automatic audit trail
   - Change tracking
   - User attribution

## Database Schema Relationships

```
User ──────┬─── creates ───→ Task
           │
           └─── assigned ───→ Task
           │
           └─── writes ────→ Comment
           │
           └─── performs ──→ ActivityLog

Project ───── contains ───→ Task

Task ──────┬─── has ───────→ Comment
           │
           └─── tracks ────→ ActivityLog
```

## Technology Stack

### Backend
- **Framework**: Flask 3.0.0
- **ORM**: SQLAlchemy 3.1.1
- **Database**: SQLite
- **Security**: Werkzeug 3.0.1
- **Testing**: pytest 8.0.0

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling with gradients
- **JavaScript**: Vanilla JS for interactivity

## Deployment Considerations

1. **Development**
   - SQLite database (tasks.db)
   - Flask development server
   - Debug mode enabled

2. **Production Recommendations**
   - Use PostgreSQL or MySQL instead of SQLite
   - Configure production-grade WSGI server (Gunicorn, uWSGI)
   - Enable HTTPS
   - Use environment variables for secrets
   - Implement rate limiting
   - Add CORS configuration if needed
   - Set up proper logging
   - Configure session security settings

## Scalability Considerations

1. **Database**
   - Add indexes on frequently queried fields
   - Consider database connection pooling
   - Implement caching layer (Redis)

2. **Application**
   - Stateless design enables horizontal scaling
   - Session storage can be moved to Redis
   - API can be load balanced

3. **Frontend**
   - Static files can be served via CDN
   - Implement lazy loading
   - Add pagination for large datasets

## Future Enhancements

1. **Features**
   - Real-time updates with WebSockets
   - File attachments
   - Task dependencies
   - Recurring tasks
   - Email notifications
   - Team collaboration
   - Advanced search

2. **Technical**
   - API versioning
   - GraphQL endpoint
   - Microservices architecture
   - Containerization (Docker)
   - CI/CD pipeline
   - Comprehensive test coverage

## Conclusion

This architecture provides a solid foundation for a task management application with clear separation of concerns, RESTful API design, and comprehensive data modeling. The modular structure allows for easy maintenance and future enhancements while maintaining code quality and security best practices.
