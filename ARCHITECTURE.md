# Task Manager Application - Architecture Diagram

## System Architecture Overview

```mermaid
graph TB
    subgraph "Client Layer"
        Browser[Web Browser]
        HTML[Static HTML/CSS/JS<br/>index.html]
    end

    subgraph "Application Layer - Flask"
        App[Flask Application<br/>run.py]
        Factory[App Factory<br/>create_app]
        
        subgraph "API Routes/Blueprints"
            AuthBP[Auth Blueprint<br/>/auth/*]
            TasksBP[Tasks Blueprint<br/>/tasks/*]
            ProjectsBP[Projects Blueprint<br/>/projects/*]
            CommentsBP[Comments Blueprint<br/>/api/*]
        end
        
        Session[Session Management<br/>Flask Sessions]
    end

    subgraph "Business Logic Layer"
        subgraph "Models - SQLAlchemy ORM"
            UserModel[User Model<br/>Authentication & Profile]
            TaskModel[Task Model<br/>Core Task Entity]
            ProjectModel[Project Model<br/>Task Organization]
            CommentModel[Comment Model<br/>Task Discussions]
            ActivityModel[ActivityLog Model<br/>Audit Trail]
        end
    end

    subgraph "Data Layer"
        DB[(SQLite Database<br/>tasks.db)]
        DBEngine[SQLAlchemy Engine<br/>database.py]
    end

    subgraph "Security Layer"
        Werkzeug[Werkzeug Security<br/>Password Hashing]
    end

    Browser -->|HTTP Requests| HTML
    HTML -->|AJAX/Fetch API| App
    App --> Factory
    Factory --> AuthBP
    Factory --> TasksBP
    Factory --> ProjectsBP
    Factory --> CommentsBP
    Factory --> Session
    
    AuthBP --> Werkzeug
    AuthBP --> UserModel
    TasksBP --> TaskModel
    TasksBP --> ActivityModel
    ProjectsBP --> ProjectModel
    CommentsBP --> CommentModel
    CommentsBP --> ActivityModel
    
    UserModel --> DBEngine
    TaskModel --> DBEngine
    ProjectModel --> DBEngine
    CommentModel --> DBEngine
    ActivityModel --> DBEngine
    
    DBEngine --> DB
    
    Session -.->|Stores user_id| AuthBP
    Session -.->|Validates| TasksBP
    Session -.->|Validates| ProjectsBP
    Session -.->|Validates| CommentsBP

    style Browser fill:#e1f5ff
    style HTML fill:#e1f5ff
    style App fill:#fff4e1
    style Factory fill:#fff4e1
    style DB fill:#e8f5e9
    style Werkzeug fill:#ffe1e1
```

## Data Model Relationships

```mermaid
erDiagram
    USER ||--o{ TASK : "creates (created_by)"
    USER ||--o{ TASK : "assigned to (assigned_to)"
    USER ||--o{ COMMENT : "writes"
    USER ||--o{ ACTIVITY_LOG : "performs"
    
    PROJECT ||--o{ TASK : "contains"
    
    TASK ||--o{ COMMENT : "has"
    TASK ||--o{ ACTIVITY_LOG : "tracks"
    
    USER {
        int id PK
        string username UK
        string email UK
        string password_hash
        datetime created_at
    }
    
    PROJECT {
        int id PK
        string name
        text description
        string color
        datetime created_at
    }
    
    TASK {
        int id PK
        string title
        text description
        string status
        string priority
        datetime due_date
        int project_id FK
        int created_by FK
        int assigned_to FK
        datetime created_at
        datetime updated_at
        datetime completed_at
    }
    
    COMMENT {
        int id PK
        text content
        int task_id FK
        int user_id FK
        datetime created_at
        datetime updated_at
    }
    
    ACTIVITY_LOG {
        int id PK
        int task_id FK
        int user_id FK
        string action
        string field_name
        text old_value
        text new_value
        datetime created_at
    }
```

## API Endpoints Flow

```mermaid
sequenceDiagram
    participant Client
    participant Flask
    participant Session
    participant Routes
    participant Models
    participant Database

    Note over Client,Database: Authentication Flow
    Client->>Flask: POST /auth/register
    Flask->>Routes: auth_bp.register()
    Routes->>Models: Create User
    Models->>Database: INSERT user
    Database-->>Models: user_id
    Models-->>Routes: User object
    Routes->>Session: Set user_id
    Routes-->>Client: 201 Created + user data

    Note over Client,Database: Task Management Flow
    Client->>Flask: POST /tasks/
    Flask->>Session: Check user_id
    Session-->>Flask: user_id
    Flask->>Routes: tasks_bp.create_task()
    Routes->>Models: Create Task
    Models->>Database: INSERT task
    Routes->>Models: Create ActivityLog
    Models->>Database: INSERT activity_log
    Database-->>Routes: Success
    Routes-->>Client: 201 Created + task data

    Note over Client,Database: Comment Flow
    Client->>Flask: POST /api/task/{id}/comments
    Flask->>Session: Validate user
    Flask->>Routes: comments_bp.create_comment()
    Routes->>Models: Verify Task ownership
    Routes->>Models: Create Comment
    Routes->>Models: Create ActivityLog
    Models->>Database: INSERT comment & activity
    Database-->>Client: 201 Created + comment data
```

## Component Architecture

```mermaid
graph LR
    subgraph "Frontend"
        UI[HTML/CSS/JavaScript<br/>Single Page Interface]
    end

    subgraph "Backend - Flask Application"
        subgraph "Entry Point"
            RunPy[run.py<br/>Application Entry]
        end
        
        subgraph "Application Factory"
            Init[__init__.py<br/>create_app]
            Config[Configuration<br/>SQLite, Secret Key]
        end
        
        subgraph "Route Handlers"
            Auth[auth.py<br/>Register, Login, Logout]
            Tasks[tasks.py<br/>CRUD + Stats]
            Projects[projects.py<br/>CRUD Operations]
            Comments[comments.py<br/>Comments + Activity]
        end
        
        subgraph "Data Models"
            Models[models.py<br/>5 SQLAlchemy Models]
        end
        
        subgraph "Database"
            DBModule[database.py<br/>SQLAlchemy Instance]
        end
    end

    subgraph "Storage"
        SQLite[(tasks.db<br/>SQLite Database)]
    end

    UI -->|HTTP/JSON| RunPy
    RunPy --> Init
    Init --> Config
    Init --> Auth
    Init --> Tasks
    Init --> Projects
    Init --> Comments
    
    Auth --> Models
    Tasks --> Models
    Projects --> Models
    Comments --> Models
    
    Models --> DBModule
    DBModule --> SQLite

    style UI fill:#e1f5ff
    style RunPy fill:#fff4e1
    style SQLite fill:#e8f5e9
```

## Request/Response Flow

```mermaid
flowchart TD
    Start([HTTP Request]) --> Route{Route Match?}
    Route -->|/auth/*| Auth[Auth Blueprint]
    Route -->|/tasks/*| Tasks[Tasks Blueprint]
    Route -->|/projects/*| Projects[Projects Blueprint]
    Route -->|/api/*| Comments[Comments Blueprint]
    Route -->|/| Static[Serve index.html]
    
    Auth --> SessionCheck1{Session Valid?}
    Tasks --> SessionCheck2{Session Valid?}
    Projects --> SessionCheck3{Session Valid?}
    Comments --> SessionCheck4{Session Valid?}
    
    SessionCheck1 -->|No & Required| Unauthorized1[401 Unauthorized]
    SessionCheck2 -->|No| Unauthorized2[401 Unauthorized]
    SessionCheck3 -->|No| Unauthorized3[401 Unauthorized]
    SessionCheck4 -->|No| Unauthorized4[401 Unauthorized]
    
    SessionCheck1 -->|Yes/Not Required| AuthLogic[Auth Logic]
    SessionCheck2 -->|Yes| TaskLogic[Task Logic]
    SessionCheck3 -->|Yes| ProjectLogic[Project Logic]
    SessionCheck4 -->|Yes| CommentLogic[Comment Logic]
    
    AuthLogic --> DBOp1[Database Operation]
    TaskLogic --> DBOp2[Database Operation]
    ProjectLogic --> DBOp3[Database Operation]
    CommentLogic --> DBOp4[Database Operation]
    
    DBOp1 --> Response1[JSON Response]
    DBOp2 --> ActivityLog[Log Activity]
    ActivityLog --> Response2[JSON Response]
    DBOp3 --> Response3[JSON Response]
    DBOp4 --> ActivityLog2[Log Activity]
    ActivityLog2 --> Response4[JSON Response]
    
    Static --> Response5[HTML Response]
    
    Response1 --> End([HTTP Response])
    Response2 --> End
    Response3 --> End
    Response4 --> End
    Response5 --> End
    Unauthorized1 --> End
    Unauthorized2 --> End
    Unauthorized3 --> End
    Unauthorized4 --> End

    style Start fill:#e1f5ff
    style End fill:#e8f5e9
    style Unauthorized1 fill:#ffe1e1
    style Unauthorized2 fill:#ffe1e1
    style Unauthorized3 fill:#ffe1e1
    style Unauthorized4 fill:#ffe1e1
```

## Technology Stack

```mermaid
mindmap
  root((Task Manager))
    Backend
      Flask 3.0.0
        Web Framework
        Routing
        Session Management
      Flask-SQLAlchemy 3.1.1
        ORM
        Database Abstraction
      Werkzeug 3.0.1
        Password Hashing
        Security Utilities
      SQLite
        Embedded Database
        File-based Storage
    Frontend
      HTML5
        Structure
      CSS3
        Styling
        Responsive Design
      JavaScript
        AJAX/Fetch API
        DOM Manipulation
    Testing
      Pytest 8.0.0
        Unit Testing
        Integration Testing
```

## Key Features & Capabilities

### Authentication & Authorization
- User registration with email validation
- Secure password hashing (Werkzeug)
- Session-based authentication
- User profile management

### Task Management
- CRUD operations for tasks
- Task status tracking (todo, in_progress, done)
- Priority levels (low, medium, high, urgent)
- Due date management with overdue detection
- Task assignment to users
- Task filtering and search

### Project Organization
- Project creation and management
- Color-coded projects
- Task grouping by project
- Project-level statistics

### Collaboration Features
- Comments on tasks
- Activity logging for audit trail
- User mentions and notifications (via activity log)

### Analytics & Reporting
- Task statistics by status
- Task statistics by priority
- Completion rate calculation
- Overdue task tracking

## Security Considerations

1. **Password Security**: Werkzeug password hashing
2. **Session Management**: Flask secure sessions with secret key
3. **Authentication**: Session-based user validation on protected routes
4. **Data Isolation**: Users can only access their own tasks
5. **Input Validation**: Request data validation in route handlers

## Deployment Architecture

```mermaid
graph TB
    subgraph "Development Environment"
        DevServer[Flask Dev Server<br/>Port 5000]
        DevDB[(SQLite DB<br/>tasks.db)]
    end
    
    subgraph "Production Considerations"
        WSGI[WSGI Server<br/>Gunicorn/uWSGI]
        WebServer[Web Server<br/>Nginx/Apache]
        ProdDB[(Production DB<br/>PostgreSQL/MySQL)]
        Static[Static Files<br/>CDN/Web Server]
    end
    
    DevServer --> DevDB
    WebServer --> WSGI
    WSGI --> ProdDB
    WebServer --> Static

    style DevServer fill:#fff4e1
    style WSGI fill:#e8f5e9
    style WebServer fill:#e8f5e9
```
