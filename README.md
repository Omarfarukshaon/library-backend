# 📚 Library Management Backend (Django REST API)

A production-ready Django backend for managing library operations — including book issuing, returns, overdue fine logging, and audit tracking. Built with atomic transactions, clean architecture, and reproducible workflows.

---

## 🚀 Features

- Book issuing and return tracking
- Automated overdue fine logging via management command
- Audit trail of issue events (IssueLog)
- Custom user profiles for library members
- RESTful API endpoints tested with Thunder Client
- Admin-friendly model design and filtering

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (dev) / PostgreSQL (prod-ready)
- **Testing**: Thunder Client, Django TestCase
- **Deployment**: WSGI-ready, `.env` support, minimal dependencies

---

## 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/library-backend.git
cd library-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
