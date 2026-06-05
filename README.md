# Customer Management App

A Django-based CRM (Customer Relationship Management) web application for managing customers, products, and orders. Built by following [Dennis Ivy's Django 3.0 Crash Course](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO) on YouTube.

---

## Features

- **Dashboard** — Overview of customers and orders
- **Customer management** — View, create, update, and delete customers
- **Product & order management** — Track orders linked to customers
- **Search & filtering** — Filter orders and customers using `django-filters`
- **User authentication** — Register, login, and logout
- **Role-based access** — Permissions and decorators to restrict views by user group
- **User profiles** — Profile pages with image upload support
- **Django Signals** — Automatically create a user profile on registration
- **Password reset** — Email-based password reset flow

> **Note:** AWS S3 (file storage), AWS RDS (cloud database), and deployment are not implemented. The app runs locally with PostgreSQL and local static/media file storage.

---

## Tech Stack

- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Filtering:** django-filters
- **Config:** python-decouple (`.env` file)
- **Frontend:** HTML, CSS (Django templates)

---

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd CustomerManagement
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet, install the core packages manually:

```bash
pip install django django-filters psycopg2-binary python-decouple Pillow
```

### 4. Configure environment variables

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

Then open `.env` and set:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=cma
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

### 5. Create the PostgreSQL database

```bash
psql -U postgres
CREATE DATABASE cma;
\q
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Project Structure

```
CustomerManagement/
├── CustomerManagement/     # Project config (settings, urls, wsgi)
├── app/                    # Main application
│   ├── models.py           # Customer, Product, Order models
│   ├── views.py            # All views (dashboard, CRUD, auth)
│   ├── forms.py            # Model forms and registration form
│   ├── filters.py          # django-filters config
│   ├── signals.py          # Auto profile creation on user register
│   ├── decorators.py       # Custom role/permission decorators
│   └── urls.py             # App-level URL patterns
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── .env                    # Local environment variables (not committed)
├── .env.example            # Template for .env
├── .gitignore
└── manage.py
```

---

## Environment Variables Reference

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key | — |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `DB_NAME` | PostgreSQL database name | — |
| `DB_USER` | PostgreSQL username | — |
| `DB_PASSWORD` | PostgreSQL password | — |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |
| `EMAIL_HOST_USER` | Gmail address for password reset | — |
| `EMAIL_HOST_PASSWORD` | Gmail app password | — |

---

## Admin Panel

Access the Django admin at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) using your superuser credentials. From here you can manage all users, customers, products, and orders directly.

---

## Credits

- Tutorial by [Dennis Ivy](https://www.youtube.com/@DennisIvy) — [Django 3.0 Crash Course](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
