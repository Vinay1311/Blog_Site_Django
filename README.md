# Blog Site - A Modern Django Blog Platform

## 🚀 Project Overview

Blog Site is a modern blog platform built with Django, showcasing advanced features and best practices in web development. This project demonstrates a clean architecture, robust authentication, and efficient data management.

## 📋 Key Features

- ✨ **Role-Based Authentication**
  - Admin, Editor, and Reader roles with proper permission management
  - Custom authentication middleware for role-based access control

- 📝 **Blog Management**
  - Create, edit, and delete blog posts
  - Category and tag system for content organization
  - Status management (Draft/Published)
  - Timestamp tracking for posts

- 🔍 **Advanced Search & Filtering**
  - Search by title, category, tags, and date
  - Pagination support for large datasets
  - Custom pagination utility

- 🔐 **Security Features**
  - JWT authentication for API security
  - Role-based permissions
  - Secure password handling

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

All endpoints are documented using:
- Swagger/OpenAPI documentation
- Comprehensive Python docstrings
- Clear request/response examples
- Detailed error handling
- Interactive API testing
- `POST /api/user/login/` - User login

### Blog Management
- `POST /api/post_blog/` - Create new blog post
- `PATCH /api/edit_blog/<id>/` - Edit blog post
- `DELETE /api/delete_blog/<id>/` - Delete blog post
- `GET /api/blog_list/` - List blog posts with pagination

## 📝 API Response Format

All API responses follow this format:
```json
{
    "data": [...],
    "pagination": {
        "total_pages": X,
        "total_count": Y,
        "page_number": Z,
        "page_count": N
    }
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

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
