# Blog Site - A Modern Django Blog Platform

## 🚀 Project Overview

Blog Site is a modern blog platform built with Django, showcasing advanced features and best practices in web development. This project demonstrates a clean architecture, robust authentication, and efficient data management.

## 📋 Key Features

- ✨ **Role-Based Authentication**
  - Admin, Editor, and Reader roles with proper permission management
  - JWT authentication with 60-day token lifetime
  - Custom permission classes for role-based access control
  - Secure password handling

- 📝 **Blog Management**
  - Create, edit, and delete blog posts
  - Category and tag system for content organization
  - Status management (Draft/Published)
  - Timestamp tracking for posts
  - Improved error handling with try-except blocks

- 🔍 **Advanced Search & Filtering**
  - Search by title, category, tags, and date
  - Pagination support with configurable page size and count
  - Custom pagination utility

- 🔐 **Security Features**
  - JWT authentication with 60-day token lifetime
  - Role-based permissions
  - Secure password handling
  - Input validation and error handling

## 🎯 Solution Architecture

### 🏗️ Technical Stack
- **Backend**: Django 4.x
- **Authentication**: Django REST Framework + JWT
- **Database**: SQLite (production-ready with PostgreSQL support)
- **Middleware**: Custom role-based authentication

### 📁 Project Structure
```
blog_site/
├── blog/                # Main blog application
│   ├── models.py        # Blog models (User, BlogPost)
│   ├── serializers.py   # API serializers
│   ├── apis.py         # API endpoints with comprehensive docstrings
│   ├── urls.py         # URL routing
│   └── admin.py        # Admin configurations
├── master/              # Master data management
│   └── models.py       # Master data models
├── helper/              # Utility functions and mixins
│   ├── models.py       # Base model mixins
│   └── utils.py        # Utility functions
├── middleware/          # Custom middleware
│   └── admin_role_middleware.py  # Middleware for admin-only operations
└── blog_site/          # Project settings
    └── settings.py
```

### 🔧 Key Components

#### 1. Authentication System
- JWT-based authentication
- Role-based access control
- Custom middleware for admin operations
- Secure password handling
- Comprehensive API documentation

#### 2. Blog Management
- RESTful API endpoints with detailed docstrings
- Role-based permissions
- Status management
- Category and tag system
- Improved error handling

#### 3. Search & Filtering
- Custom pagination utility
- Multi-field search
- Date-based filtering
- Category and tag filtering
- Optimized query performance

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone [repository-url]
cd blog_site
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Run the development server**
```bash
python manage.py runserver
```

## 📚 API Documentation

All endpoints are documented using Swagger/OpenAPI with detailed descriptions and examples. The API is accessible at `/api/docs/`.

### Authentication
- **JWT Authentication**
  - Access Token Lifetime: 60 days
  - Refresh Token Lifetime: 60 days
  - Header Format: `Bearer <token>`
  - **Note**: If you encounter "Unauthenticated" or "Authentication credentials were not provided" errors, ensure the token is prefixed with "Bearer " in the Authorization header.

### API Endpoints

#### User Authentication
- `POST /api/user/register/` - Register new user
- `POST /api/user/login/` - User login

#### Blog Management
- `POST /api/post_blog/` - Create new blog post (Admin/Editor only)
- `GET /api/blog_list/` - List blog posts (Public access)
- `PATCH /api/edit_blog/<str:id>/` - Edit blog post (Admin/Editor only)
- `DELETE /api/delete_blog/<str:id>/` - Delete blog post (Admin/Editor only)

#### Tag Management
- `POST /api/add_tag/` - Add new tag (Admin/Editor only)

### Response Format

#### Success Response
```json
{
    "data": [...],
    "success": true,
    "pagination": {
        "total_pages": X,
        "total_count": Y,
        "page_number": Z,
        "page_count": N
    }
}
```

#### Error Response
```json
{
    "error": "Error message",
    "success": false
}
```

## 🛡️ Security

- JWT token-based authentication
- Role-based access control
- Secure password hashing
- Input validation
- CSRF protection

## 🎯 Best Practices Implemented

- Clean architecture with separation of concerns
- RESTful API design
- Proper error handling
- Pagination for large datasets
- Consistent code style
- Documentation for all endpoints
