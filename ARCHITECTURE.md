# Task Manager Application - Architecture Documentation

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                          CLIENT LAYER                                │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    Web Browser (Frontend)                      │  │
│  │  ┌─────────────────────────────────────────────────────────┐  │  │
│  │  │              static/index.html                           │  │  │
│  │  │  • HTML5 Structure                                       │  │  │
│  │  │  • CSS3 Styling (Gradient UI)                           │  │  │
│  │  │  • Vanilla JavaScript (AJAX/Fetch API)                  │  │  │
│  │  └─────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  │ HTTP/HTTPS
                                  │ REST API Calls
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       APPLICATION LAYER                              │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    Flask Application                           │  │
│  │                      (run.py)                                  │  │
│  │  ┌─────────────────────────────────────────────────────────┐  │  │
│  │  │              app/__init__.py                             │  │  │
│  │  │  • Application Factory (create_app)                      │  │  │
│  │  │  • Blueprint Registration                                │  │  │
│  │  │  • Database Initialization                               │  │  │
│  │  │  • Session Configuration                                 │  │  │
│  │  └─────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    ROUTING LAYER                              │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │  │
│  │  │   auth_bp    │  │   tasks_bp   │  │ projects_bp  │       │  │
│  │  │  /auth/*     │  │  /tasks/*    │  │ /projects/*  │       │  │
│  │  └──────────────┘  └──────────────┘  └──────────────┘       │  │
│  │  ┌──────────────┐                                            │  │
│  │  │ comments_bp  │                                            │  │
│  │  │   /api/*     │                                            │  │
│  │  └──────────────┘                                            │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                   BUSINESS LOGIC LAYER                        │  │
│  │  ┌─────────────────────────────────────────────────────────┐  │  │
│  │  │              Route Handlers                              │  │  │
│  │  │  • Request Validation                                    │  │  │
│  │  │  • Authentication Checks                                 │  │  │
│  │  │  • Business Logic Processing                             │  │  │
│  │  │  • Response Formatting                                   │  │  │
│  │  └─────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  │ SQLAlchemy ORM
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA LAYER                                   │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │                    Database Models                            │  │
│  │                   (app/models.py)                             │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │  │
│  │  │   User   │  │   Task   │  │ Project  │  │ Comment  │    │  │
│  │  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │  │
│  │  ┌──────────────┐                                            │  │
│  │  │ ActivityLog  │                                            │  │
│  │  └──────────────┘                                            │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                       │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │              SQLite Database (tasks.db)                       │  │
│  │  • Persistent Storage                                         │  │
│  │  • ACID Transactions                                          │  │
│  │  • Relational Data Structure                                 │  │
│  └───────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Detailed Component Architecture

### 1. **Frontend Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                    static/index.html                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │              UI Components                          │    │
│  │  • Authentication Forms (Login/Register)           │    │
│  │  • Task List View                                  │    │
│  │  • Task Creation/Edit Forms                        │    │
│  │  │  - Title, Description                           │    │
│  │  │  - Status Selector (todo/in_progress/done)     │    │
│  │  │  - Priority Selector (low/medium/high/urgent)  │    │
│  │  │  - Due Date Picker                              │    │
│  │  │  - Project Assignment                           │    │
│  │  │  - User Assignment                              │    │
│  │  • Project Management Interface                    │    │
│  │  • Statistics Dashboard                            │    │
│  │  • Comment Section                                 │    │
│  │  • Activity Log Viewer                             │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │              JavaScript Logic                       │    │
│  │  • AJAX/Fetch API Calls                            │    │
│  │  • DOM Manipulation                                │    │
│  │  • Event Handlers                                  │    │
│  │  • Client-side Validation                          │    │
│  │  • Session Management                              │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │              CSS Styling                            │    │
│  │  • Gradient Background (Purple Theme)              │    │
│  │  • Responsive Design                               │    │
│  │  • Form Styling                                    │    │
│  │  • Card-based Layout                               │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### 2. **Backend API Architecture**

```
┌─────────────────────────────────────────────────────────────────┐
│                      Flask Application                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Authentication Blueprint                     │  │
│  │              (app/routes/auth.py)                        │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  POST /auth/register                               │  │  │
│  │  │  • Validate username, email, password              │  │  │
│  │  │  • Check for duplicates                            │  │  │
│  │  │  • Hash password (Werkzeug)                        │  │  │
│  │  │  • Create user record                              │  │  │
│  │  │  • Set session                                     │  │  │
│  │  │  • Return user data                                │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  POST /auth/login                                  │  │  │
│  │  │  • Validate credentials                            │  │  │
│  │  │  • Verify password hash                            │  │  │
│  │  │  • Set session                                     │  │  │
│  │  │  • Return user data                                │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  POST /auth/logout                                 │  │  │
│  │  │  • Clear session                                   │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  GET /auth/me                                      │  │  │
│  │  │  • Return current user info                        │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Tasks Blueprint                              │  │
│  │              (app/routes/tasks.py)                       │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  GET /tasks/                                       │  │  │
│  │  │  • Query params: status, priority, project_id,    │  │  │
│  │  │    assigned_to_me                                  │  │  │
│  │  │  • Filter tasks by criteria                        │  │  │
│  │  │  • Return task list with count                     │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  POST /tasks/                                      │  │  │
│  │  │  • Validate required fields                        │  │  │
│  │  │  • Create task record                              │  │  │
│  │  │  • Log activity (created)                          │  │  │
│  │  │  • Return task data                                │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  GET /tasks/<id>                                   │  │  │
│  │  │  • Fetch single task                               │  │  │
│  │  │  • Verify ownership                                │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  PUT /tasks/<id>                                   │  │  │
│  │  │  • Track field changes                             │  │  │
│  │  │  • Update task fields                              │  │  │
│  │  │  • Handle status transitions                       │  │  │
│  │  │  • Log all changes to ActivityLog                  │  │  │
│  │  │  • Return updated task                             │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  DELETE /tasks/<id>                                │  │  │
│  │  │  • Verify ownership                                │  │  │
│  │  │  • Delete task (cascade deletes comments/logs)     │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  GET /tasks/stats                                  │  │  │
│  │  │  • Calculate statistics:                           │  │  │
│  │  │    - Total tasks                                   │  │  │
│  │  │    - By status (todo/in_progress/done)            │  │  │
│  │  │    - By priority (low/medium/high/urgent)         │  │  │
│  │  │    - Overdue count                                 │  │  │
│  │  │    - Completion rate                               │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Projects Blueprint                           │  │
│  │              (app/routes/projects.py)                    │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  GET /projects/                                    │  │  │
│  │  │  • List all projects with task counts              │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  POST /projects/                                   │  │  │
│  │  │  • Create project with name, description, color    │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  GET /projects/<id>                                │  │  │
│  │  │  • Get project details with associated tasks       │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  PUT /projects/<id>                                │  │  │
│  │  │  • Update project details                          │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  DELETE /projects/<id>                             │  │  │
│  │  │  • Delete project (cascade deletes tasks)          │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Comments Blueprint                           │  │
│  │              (app/routes/comments.py)                    │  │
│  │  • Comment CRUD operations                               │  │
│  │  • Associated with tasks                                 │  │
│  │  • User attribution                                      │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 3. **Database Schema**

```
┌─────────────────────────────────────────────────────────────────┐
│                      Database Models                             │
│                      (app/models.py)                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    User Model                             │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  id (PK)              : Integer                    │  │  │
│  │  │  username (UNIQUE)    : String(80)                 │  │  │
│  │  │  email (UNIQUE)       : String(120)                │  │  │
│  │  │  password_hash        : String(256)                │  │  │
│  │  │  created_at           : DateTime                   │  │  │
│  │  │                                                     │  │  │
│  │  │  Relationships:                                    │  │  │
│  │  │  • tasks (assigned)   → Task.assigned_to          │  │  │
│  │  │  • owned_tasks        → Task.created_by           │  │  │
│  │  │  • comments           → Comment.user_id           │  │  │
│  │  │  • activity_logs      → ActivityLog.user_id       │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   Project Model                           │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  id (PK)              : Integer                    │  │  │
│  │  │  name                 : String(120)                │  │  │
│  │  │  description          : Text                       │  │  │
│  │  │  color                : String(7) [hex color]      │  │  │
│  │  │  created_at           : DateTime                   │  │  │
│  │  │                                                     │  │  │
│  │  │  Relationships:                                    │  │  │
│  │  │  • tasks              → Task.project_id           │  │  │
│  │  │    (cascade delete)                                │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    Task Model                             │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  id (PK)              : Integer                    │  │  │
│  │  │  title                : String(200)                │  │  │
│  │  │  description          : Text                       │  │  │
│  │  │  status               : String(20)                 │  │  │
│  │  │    [todo, in_progress, done]                       │  │  │
│  │  │  priority             : String(10)                 │  │  │
│  │  │    [low, medium, high, urgent]                     │  │  │
│  │  │  due_date             : DateTime (nullable)        │  │  │
│  │  │  project_id (FK)      : Integer → projects.id     │  │  │
│  │  │  created_by (FK)      : Integer → users.id        │  │  │
│  │  │  assigned_to (FK)     : Integer → users.id        │  │  │
│  │  │  created_at           : DateTime                   │  │  │
│  │  │  updated_at           : DateTime                   │  │  │
│  │  │  completed_at         : DateTime (nullable)        │  │  │
│  │  │                                                     │  │  │
│  │  │  Methods:                                          │  │  │
│  │  │  • is_overdue()       : Boolean                    │  │  │
│  │  │  • to_dict()          : Dictionary                 │  │  │
│  │  │                                                     │  │  │
│  │  │  Relationships:                                    │  │  │
│  │  │  • project            → Project                    │  │  │
│  │  │  • creator            → User                       │  │  │
│  │  │  • assignee           → User                       │  │  │
│  │  │  • comments           → Comment.task_id           │  │  │
│  │  │  • activity_logs      → ActivityLog.task_id       │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   Comment Model                           │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  id (PK)              : Integer                    │  │  │
│  │  │  content              : Text                       │  │  │
│  │  │  task_id (FK)         : Integer → tasks.id        │  │  │
│  │  │  user_id (FK)         : Integer → users.id        │  │  │
│  │  │  created_at           : DateTime                   │  │  │
│  │  │  updated_at           : DateTime                   │  │  │
│  │  │                                                     │  │  │
│  │  │  Relationships:                                    │  │  │
│  │  │  • task               → Task                       │  │  │
│  │  │  • user               → User                       │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                 ActivityLog Model                         │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  id (PK)              : Integer                    │  │  │
│  │  │  task_id (FK)         : Integer → tasks.id        │  │  │
│  │  │  user_id (FK)         : Integer → users.id        │  │  │
│  │  │  action               : String(50)                 │  │  │
│  │  │    [created, updated, status_changed, etc.]        │  │  │
│  │  │  field_name           : String(50) (nullable)      │  │  │
│  │  │  old_value            : Text (nullable)            │  │  │
│  │  │  new_value            : Text (nullable)            │  │  │
│  │  │  created_at           : DateTime                   │  │  │
│  │  │                                                     │  │  │
│  │  │  Relationships:                                    │  │  │
│  │  │  • task               → Task                       │  │  │
│  │  │  • user               → User                       │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 4. **Entity Relationship Diagram**

```
┌─────────────┐
│    User     │
│─────────────│
│ id (PK)     │◄──────────────┐
│ username    │               │
│ email       │               │
│ password    │               │
└─────────────┘               │
       │                      │
       │ created_by           │ assigned_to
       │                      │
       ▼                      │
┌─────────────┐               │
│    Task     │◄──────────────┘
│─────────────│
│ id (PK)     │◄──────────────┐
│ title       │               │
│ description │               │
│ status      │               │
│ priority    │               │
│ due_date    │               │
│ project_id  │───┐           │
│ created_by  │   │           │
│ assigned_to │   │           │
└─────────────┘   │           │
       │          │           │
       │          │           │
       │          ▼           │
       │   ┌─────────────┐   │
       │   │   Project   │   │
       │   │─────────────│   │
       │   │ id (PK)     │   │
       │   │ name        │   │
       │   │ description │   │
       │   │ color       │   │
       │   └─────────────┘   │
       │                     │
       ├─────────────────────┤
       │                     │
       ▼                     ▼
┌─────────────┐       ┌─────────────┐
│   Comment   │       │ ActivityLog │
│─────────────│       │─────────────│
│ id (PK)     │       │ id (PK)     │
│ content     │       │ action      │
│ task_id (FK)│       │ field_name  │
│ user_id (FK)│       │ old_value   │
└─────────────┘       │ new_value   │
                      │ task_id (FK)│
                      │ user_id (FK)│
                      └─────────────┘
```

---

## Data Flow Diagrams

### 5. **Authentication Flow**

```
┌─────────┐                                    ┌─────────────┐
│ Browser │                                    │   Flask     │
│         │                                    │   Server    │
└────┬────┘                                    └──────┬──────┘
     │                                                │
     │  1. POST /auth/register                       │
     │  {username, email, password}                  │
     ├──────────────────────────────────────────────►│
     │                                                │
     │                                         2. Validate input
     │                                         3. Check duplicates
     │                                         4. Hash password
     │                                         5. Create User
     │                                         6. Set session
     │                                                │
     │  7. Return user data + session cookie         │
     │◄──────────────────────────────────────────────┤
     │                                                │
     │  8. POST /auth/login                          │
     │  {username, password}                         │
     ├──────────────────────────────────────────────►│
     │                                                │
     │                                         9. Find user
     │                                         10. Verify password
     │                                         11. Set session
     │                                                │
     │  12. Return user data + session cookie        │
     │◄──────────────────────────────────────────────┤
     │                                                │
```

### 6. **Task Creation Flow**

```
┌─────────┐                                    ┌─────────────┐
│ Browser │                                    │   Flask     │
│         │                                    │   Server    │
└────┬────┘                                    └──────┬──────┘
     │                                                │
     │  1. POST /tasks/                              │
     │  {title, description, status,                 │
     │   priority, due_date, project_id}             │
     ├──────────────────────────────────────────────►│
     │                                                │
     │                                         2. Check auth
     │                                         3. Validate data
     │                                         4. Create Task
     │                                                │
     │                                                ▼
     │                                         ┌─────────────┐
     │                                         │  Database   │
     │                                         │             │
     │                                         │ 5. INSERT   │
     │                                         │    Task     │
     │                                         │             │
     │                                         │ 6. INSERT   │
     │                                         │ ActivityLog │
     │                                         │  (created)  │
     │                                         └─────────────┘
     │                                                │
     │  7. Return task data                          │
     │◄──────────────────────────────────────────────┤
     │                                                │
```

### 7. **Task Update Flow with Activity Logging**

```
┌─────────┐                                    ┌─────────────┐
│ Browser │                                    │   Flask     │
│         │                                    │   Server    │
└────┬────┘                                    └──────┬──────┘
     │                                                │
     │  1. PUT /tasks/<id>                           │
     │  {status: "done"}                             │
     ├──────────────────────────────────────────────►│
     │                                                │
     │                                         2. Check auth
     │                                         3. Fetch task
     │                                         4. Compare fields
     │                                         5. Track changes
     │                                                │
     │                                                ▼
     │                                         ┌─────────────┐
     │                                         │  Database   │
     │                                         │             │
     │                                         │ 6. UPDATE   │
     │                                         │    Task     │
     │                                         │  status=done│
     │                                         │  completed_at│
     │                                         │             │
     │                                         │ 7. INSERT   │
     │                                         │ ActivityLog │
     │                                         │  action:    │
     │                                         │   updated   │
     │                                         │  field:     │
     │                                         │   status    │
     │                                         │  old: todo  │
     │                                         │  new: done  │
     │                                         └─────────────┘
     │                                                │
     │  8. Return updated task                       │
     │◄──────────────────────────────────────────────┤
     │                                                │
```

---

## Security Architecture

### 8. **Security Layers**

```
┌─────────────────────────────────────────────────────────────┐
│                    Security Measures                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │         1. Authentication Layer                     │    │
│  │  • Session-based authentication                     │    │
│  │  • Password hashing (Werkzeug PBKDF2)              │    │
│  │  • Secure session cookies                           │    │
│  │  • SECRET_KEY for session signing                   │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │         2. Authorization Layer                      │    │
│  │  • User ownership verification                      │    │
│  │  • current_user_id() helper function               │    │
│  │  • 401 Unauthorized responses                       │    │
│  │  • Resource access control                          │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │         3. Input Validation                         │    │
│  │  • Required field checks                            │    │
│  │  • Data type validation                             │    │
│  │  • Enum validation (status, priority)              │    │
│  │  • 400 Bad Request responses                        │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │         4. Database Security                        │    │
│  │  • SQLAlchemy ORM (SQL injection prevention)       │    │
│  │  • Parameterized queries                            │    │
│  │  • Foreign key constraints                          │    │
│  │  • Cascade delete rules                             │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │         5. Audit Trail                              │    │
│  │  • ActivityLog for all changes                      │    │
│  │  • User attribution                                 │    │
│  │  • Timestamp tracking                               │    │
│  │  • Field-level change tracking                      │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

### 9. **Complete Technology Stack**

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend Stack                          │
├─────────────────────────────────────────────────────────────┤
│  • HTML5                                                     │
│  • CSS3 (Gradient UI, Flexbox, Grid)                       │
│  • Vanilla JavaScript (ES6+)                                │
│  • Fetch API for AJAX calls                                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      Backend Stack                           │
├─────────────────────────────────────────────────────────────┤
│  • Python 3.x                                               │
│  • Flask 3.0.0 (Web Framework)                              │
│  • Flask-SQLAlchemy 3.1.1 (ORM)                            │
│  • Werkzeug 3.0.1 (Security utilities)                      │
│  • SQLite (Database)                                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      Development Tools                       │
├─────────────────────────────────────────────────────────────┤
│  • pytest 8.0.0 (Testing framework)                         │
│  • Git (Version control)                                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      Deployment                              │
├─────────────────────────────────────────────────────────────┤
│  • Development server: Flask built-in (port 5000)           │
│  • Debug mode enabled                                       │
│  • Production: WSGI server recommended (Gunicorn/uWSGI)     │
└─────────────────────────────────────────────────────────────┘
```

---

## Application Lifecycle

### 10. **Application Startup Flow**

```
┌─────────────────────────────────────────────────────────────┐
│                   Application Startup                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. run.py executed                                         │
│     │                                                        │
│     ▼                                                        │
│  2. Import create_app from app/__init__.py                  │
│     │                                                        │
│     ▼                                                        │
│  3. create_app() called                                     │
│     │                                                        │
│     ├─► 4. Initialize Flask app                            │
│     │                                                        │
│     ├─► 5. Configure database URI (SQLite)                 │
│     │                                                        │
│     ├─► 6. Set SECRET_KEY                                  │
│     │                                                        │
│     ├─► 7. Initialize SQLAlchemy (db.init_app)             │
│     │                                                        │
│     ├─► 8. Register Blueprints:                            │
│     │      • auth_bp (/auth/*)                             │
│     │      • tasks_bp (/tasks/*)                           │
│     │      • projects_bp (/projects/*)                     │
│     │      • comments_bp (/api/*)                          │
│     │                                                        │
│     ├─► 9. Register root route (/)                         │
│     │      → Serves static/index.html                      │
│     │                                                        │
│     └─► 10. Create database tables (db.create_all)         │
│                                                              │
│  11. Start Flask development server                         │
│      • Host: localhost                                      │
│      • Port: 5000                                           │
│      • Debug: True                                          │
│                                                              │
│  12. Application ready to accept requests                   │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Features Summary

### 11. **Feature Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│                      Core Features                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  User Management                                    │    │
│  │  • Registration with validation                     │    │
│  │  • Secure login/logout                              │    │
│  │  • Session management                               │    │
│  │  • Password hashing                                 │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Task Management                                    │    │
│  │  • CRUD operations                                  │    │
│  │  • Status tracking (todo/in_progress/done)         │    │
│  │  • Priority levels (low/medium/high/urgent)        │    │
│  │  • Due date management                              │    │
│  │  • Overdue detection                                │    │
│  │  • Task assignment                                  │    │
│  │  • Filtering & search                               │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Project Organization                               │    │
│  │  • Project creation                                 │    │
│  │  • Color coding                                     │    │
│  │  • Task grouping                                    │    │
│  │  • Task count tracking                              │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Collaboration                                      │    │
│  │  • Task comments                                    │    │
│  │  • User mentions                                    │    │
│  │  • Activity logging                                 │    │
│  │  • Change history                                   │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Analytics & Reporting                              │    │
│  │  • Task statistics                                  │    │
│  │  • Status distribution                              │    │
│  │  • Priority breakdown                               │    │
│  │  • Completion rate                                  │    │
│  │  • Overdue tracking                                 │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## Scalability Considerations

### 12. **Future Enhancements**

```
┌─────────────────────────────────────────────────────────────┐
│              Potential Scalability Improvements              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Database:                                                   │
│  • Migrate from SQLite to PostgreSQL/MySQL                  │
│  • Add database indexing for performance                    │
│  • Implement connection pooling                             │
│                                                              │
│  Caching:                                                    │
│  • Add Redis for session storage                            │
│  • Cache frequently accessed data                           │
│  • Implement query result caching                           │
│                                                              │
│  API:                                                        │
│  • Add pagination for list endpoints                        │
│  • Implement rate limiting                                  │
│  • Add API versioning                                       │
│  • RESTful best practices                                   │
│                                                              │
│  Security:                                                   │
│  • Add JWT token authentication                             │
│  • Implement CORS properly                                  │
│  • Add HTTPS/SSL                                            │
│  • Input sanitization                                       │
│                                                              │
│  Frontend:                                                   │
│  • Migrate to React/Vue/Angular                             │
│  • Add real-time updates (WebSockets)                       │
│  • Progressive Web App (PWA)                                │
│  • Mobile responsive design                                 │
│                                                              │
│  Testing:                                                    │
│  • Unit tests for all routes                                │
│  • Integration tests                                        │
│  • End-to-end tests                                         │
│  • Load testing                                             │
│                                                              │
│  Deployment:                                                 │
│  • Docker containerization                                  │
│  • CI/CD pipeline                                           │
│  • Cloud deployment (AWS/GCP/Azure)                         │
│  • Load balancing                                           │
└─────────────────────────────────────────────────────────────┘
```

---

## Conclusion

This task manager application follows a **three-tier architecture** with clear separation of concerns:

1. **Presentation Layer**: HTML/CSS/JavaScript frontend
2. **Application Layer**: Flask REST API with business logic
3. **Data Layer**: SQLAlchemy ORM with SQLite database

The architecture is modular, maintainable, and follows Flask best practices with Blueprint organization, making it easy to extend and scale as requirements grow.