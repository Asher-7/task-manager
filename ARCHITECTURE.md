# Task Manager - Architecture Documentation

## System Architecture Overview

```mermaid
graph TB
    subgraph "Client Layer"
        Browser[Web Browser]
        HTML[index.html]
        CSS[Inline CSS Styles]
        JS[JavaScript Client]
    end
    
    subgraph "Application Layer"
        Flask[Flask Application]
        
        subgraph "Blueprints/Routes"
            AuthBP[auth_bp<br/>Authentication Routes]
            TasksBP[tasks_bp<br/>Task Management]
            ProjectsBP[projects_bp<br/>Project Management]
            CommentsBP[comments_bp<br/>Comments & Activity]
        end
        
        subgraph "Core Components"
            Session[Session Management]
            Security[Werkzeug Security<br/>Password Hashing]
        end
    end
    
    subgraph "Data Layer"
        SQLAlchemy[SQLAlchemy ORM]
        
        subgraph "Database Models"
            UserModel[User Model]
            TaskModel[Task Model]
            ProjectModel[Project Model]
            CommentModel[Comment Model]
            ActivityModel[ActivityLog Model]
        end
        
        SQLite[(SQLite Database<br/>tasks.db)]
    end
    
    Browser --> HTML
    HTML --> CSS
    HTML --> JS
    JS -->|HTTP/JSON| Flask
    
    Flask --> AuthBP
    Flask --> TasksBP
    Flask --> ProjectsBP
    Flask --> CommentsBP
    
    AuthBP --> Session
    AuthBP --> Security
    TasksBP --> Session
    CommentsBP --> Session
    ProjectsBP --> Session
    
    AuthBP --> SQLAlchemy
    TasksBP --> SQLAlchemy
    ProjectsBP --> SQLAlchemy
    CommentsBP --> SQLAlchemy
    
    SQLAlchemy --> UserModel
    SQLAlchemy --> TaskModel
    SQLAlchemy --> ProjectModel
    SQLAlchemy --> CommentModel
    SQLAlchemy --> ActivityModel
    
    UserModel --> SQLite
    TaskModel --> SQLite
    ProjectModel --> SQLite
    CommentModel --> SQLite
    ActivityModel --> SQLite
```

## Database Schema

```mermaid
erDiagram
    User ||--o{ Task : "creates (created_by)"
    User ||--o{ Task : "assigned to (assigned_to)"
    User ||--o{ Comment : "writes"
    User ||--o{ ActivityLog : "performs"
    
    Project ||--o{ Task : "contains"
    
    Task ||--o{ Comment : "has"
    Task ||--o{ ActivityLog : "tracks"
    
    User {
        int id PK
        string username UK
        string email UK
        string password_hash
        datetime created_at
    }
    
    Project {
        int id PK
        string name
        text description
        string color
        datetime created_at
    }
    
    Task {
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
    
    Comment {
        int id PK
        text content
        int task_id FK
        int user_id FK
        datetime created_at
        datetime updated_at
    }
    
    ActivityLog {
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

## API Endpoints Architecture

### Authentication Endpoints (`/auth`)
- `POST /auth/register` - Register new user
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout
- `GET /auth/me` - Get current user info

### Task Endpoints (`/tasks`)
- `GET /tasks/` - List all tasks (with filters)
- `POST /tasks/` - Create new task
- `GET /tasks/:id` - Get specific task
- `PUT /tasks/:id` - Update task
- `DELETE /tasks/:id` - Delete task
- `GET /tasks/stats` - Get task statistics

### Project Endpoints (`/projects`)
- `GET /projects/` - List all projects
- `POST /projects/` - Create new project
- `GET /projects/:id` - Get specific project
- `PUT /projects/:id` - Update project
- `DELETE /projects/:id` - Delete project

### Comment & Activity Endpoints (`/api`)
- `GET /api/task/:id/comments` - Get task comments
- `POST /api/task/:id/comments` - Add comment
- `PUT /api/comments/:id` - Update comment
- `DELETE /api/comments/:id` - Delete comment
- `GET /api/task/:id/activity` - Get task activity log

## Request/Response Flow

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant Flask
    participant Session
    participant Database
    
    User->>Browser: Enter credentials
    Browser->>Flask: POST /auth/login
    Flask->>Database: Query User
    Database-->>Flask: User data
    Flask->>Session: Store user_id
    Flask-->>Browser: User object (JSON)
    Browser-->>User: Show dashboard
    
    User->>Browser: Create task
    Browser->>Flask: POST /tasks/
    Flask->>Session: Verify user_id
    Flask->>Database: Insert Task
    Flask->>Database: Insert ActivityLog
    Database-->>Flask: Task created
    Flask-->>Browser: Task object (JSON)
    Browser->>Flask: GET /tasks/stats
    Flask->>Database: Query statistics
    Database-->>Flask: Stats data
    Flask-->>Browser: Statistics (JSON)
    Browser-->>User: Update UI
```

## Component Interaction Flow

```mermaid
graph TD
    A[User Action] --> B{Authenticated?}
    B -->|No| C[Show Login]
    B -->|Yes| D[Process Request]
    
    D --> E{Request Type}
    
    E -->|Create| F[Validate Input]
    E -->|Read| G[Check Permissions]
    E -->|Update| H[Track Changes]
    E -->|Delete| I[Cascade Delete]
    
    F --> J[Insert to DB]
    G --> K[Query DB]
    H --> L[Update DB + Log Activity]
    I --> M[Delete from DB]
    
    J --> N[Return Response]
    K --> N
    L --> N
    M --> N
    
    N --> O[Update UI]
```

## Data Flow Architecture

```mermaid
flowchart LR
    subgraph Frontend
        UI[User Interface]
        State[Application State]
    end
    
    subgraph Backend
        Routes[Route Handlers]
        Auth[Authentication]
        Models[Data Models]
    end
    
    subgraph Storage
        DB[(SQLite Database)]
        Sess[Session Store]
    end
    
    UI -->|User Actions| Routes
    Routes -->|Verify| Auth
    Auth -->|Check| Sess
    Routes -->|CRUD| Models
    Models -->|ORM| DB
    DB -->|Data| Models
    Models -->|JSON| Routes
    Routes -->|Response| UI
    UI -->|Update| State
```

## Security Architecture

```mermaid
graph TB
    subgraph "Security Layers"
        A[Password Hashing<br/>Werkzeug Security]
        B[Session Management<br/>Flask Sessions]
        C[Authentication Check<br/>current_user_id]
        D[Authorization<br/>Owner Verification]
    end
    
    User[User Request] --> C
    C -->|Valid Session| D
    C -->|No Session| Reject[401 Unauthorized]
    D -->|Owner Match| Allow[Process Request]
    D -->|No Match| Deny[404 Not Found]
    
    Register[Registration] --> A
    A --> Store[Store Hash in DB]
    
    Login[Login] --> A
    A -->|Verify| B
    B --> Session[Create Session]
```

## File Structure

```
task-manager/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── database.py          # SQLAlchemy setup
│   ├── models.py            # Database models
│   └── routes/
│       ├── __init__.py
│       ├── auth.py          # Authentication routes
│       ├── tasks.py         # Task management routes
│       ├── projects.py      # Project management routes
│       └── comments.py      # Comments & activity routes
├── static/
│   └── index.html           # Frontend SPA
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md
```

## Technology Stack

### Backend
- **Framework**: Flask 3.0.0
- **ORM**: Flask-SQLAlchemy 3.1.1
- **Database**: SQLite
- **Security**: Werkzeug 3.0.1
- **Testing**: pytest 8.0.0

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling (inline)
- **JavaScript**: Client-side logic (vanilla)
- **Fetch API**: HTTP requests

## Key Design Patterns

### 1. **Blueprint Pattern**
- Modular route organization
- Separation of concerns
- Easy to maintain and extend

### 2. **Repository Pattern**
- SQLAlchemy ORM abstracts database operations
- Models encapsulate data logic

### 3. **Session-Based Authentication**
- Stateful authentication
- Server-side session storage
- Secure user identification

### 4. **Activity Logging Pattern**
- Audit trail for all changes
- Tracks who, what, when
- Useful for debugging and compliance

### 5. **RESTful API Design**
- Standard HTTP methods
- Resource-based URLs
- JSON request/response

## Scalability Considerations

### Current Limitations
- SQLite (single-file database)
- Session-based auth (not distributed)
- No caching layer
- Synchronous request handling

### Future Improvements
1. **Database**: Migrate to PostgreSQL/MySQL
2. **Authentication**: JWT tokens for stateless auth
3. **Caching**: Redis for session and data caching
4. **API**: Rate limiting and pagination
5. **Frontend**: React/Vue for better state management
6. **Deployment**: Docker containerization
7. **Monitoring**: Logging and error tracking
8. **Testing**: Comprehensive test coverage

## Performance Optimization

### Database
- Indexes on foreign keys
- Eager loading for relationships
- Query optimization

### API
- Pagination for list endpoints
- Field filtering
- Compression

### Frontend
- Lazy loading
- Debouncing user input
- Local state caching

---

**Last Updated**: 2026-05-13  
**Version**: 1.0
