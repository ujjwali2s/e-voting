# 🗳️ E-Voting System — Django

> **Internship Project** · Developed by **Ravi Ranjan Kumar**  
> Built with Django (Python) · PostgreSQL · AdminLTE

This E-Voting System is a web application that serves as an automated voting system for organizations and institutions. It provides an online platform for voters to cast their votes while automatically counting results for each candidate.

The system has **2 sides**:
- **Admin** — manages positions, candidates, voters, and views results
- **Voter** — logs in and casts their vote (no OTP required)

---

## ✨ Features

- [x] Direct login for voters — no OTP or phone number required
- [x] Vote preview before final submission
- [x] Multiple vote positions support
- [x] Live results tally via Horizontal Bar Charts
- [x] Print voting results as PDF
- [x] Reorder ballot positions
- [x] Full CRUD for Voters, Candidates, and Positions
- [x] AdminLTE dashboard template
- [x] PostgreSQL & Supabase ready

### Admin Can
1. View live vote summary charts
2. Reset all votes
3. Add / Edit / Delete Voters
4. Add / Edit / Delete Candidates
5. Add / Edit / Delete Positions
6. Change ballot order (Ballot Position)
7. Update election title
8. View detailed votes list

### Voters Can
1. Register an account (or admin creates one)
2. Login with email + password
3. Vote for their preferred candidates
4. View their submitted votes

---

## 📸 Screenshots

| Admin | Voter |
|-------|-------|
|<img src="ss/admin/1.png" width="400">|<img src="ss/voter/1.png" width="400">|
|<img src="ss/admin/2.png" width="400">|<img src="ss/voter/2.png" width="400">|
|<img src="ss/admin/3.png" width="400">|<img src="ss/voter/3.png" width="400">|
|<img src="ss/admin/4.png" width="400">|<img src="ss/voter/4.png" width="400">|

---

## ⚙️ Pre-Requisites

1. **Python 3.10+** → https://www.python.org/downloads/
2. **Git** → https://git-scm.com/
3. **pip** → comes with Python
4. **PostgreSQL 14+** (local) OR a **Supabase** account (cloud) — see database setup below

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/jobic10/e-voting-with-django.git
cd e-voting-with-django
```

### 2. Create and Activate Virtual Environment

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Choose **one** of the following options:

---

### Option A — Local PostgreSQL (Recommended for Development)

#### Step 1: Install PostgreSQL
Download and install from: https://www.postgresql.org/download/

During installation:
- Set a password for the `postgres` user (remember this!)
- Keep default port: `5432`

#### Step 2: Create the Database

Open **pgAdmin** or **psql** terminal and run:
```sql
CREATE DATABASE evoting_db;
```

Or via command line:
```bash
psql -U postgres -c "CREATE DATABASE evoting_db;"
```

#### Step 3: Configure `settings.py`

Open `e_voting/settings.py` and update the `DATABASES` section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'evoting_db',       # your database name
        'HOST': '127.0.0.1',        # localhost
        'PORT': '5432',             # default PostgreSQL port
        'USER': 'postgres',         # your PostgreSQL username
        'PASSWORD': 'your_password' # your PostgreSQL password
    }
}
```

#### Step 4: Install the PostgreSQL driver
```bash
pip install psycopg2-binary
```

---

### Option B — Supabase (Cloud PostgreSQL — Free Tier Available)

Supabase is a free cloud PostgreSQL database. Great for sharing or deploying the project.

#### Step 1: Create a Supabase Account & Project

1. Go to https://supabase.com and sign up (free)
2. Click **New Project**
3. Fill in:
   - **Project Name:** `evoting`
   - **Database Password:** set a strong password (save it!)
   - **Region:** choose the closest to you
4. Click **Create new project** and wait ~1 minute

#### Step 2: Get Your Connection Details

1. In your Supabase project, go to **Settings → Database**
2. Scroll to **Connection string** section
3. Select the **"URI"** tab — you'll see something like:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.abcdefghij.supabase.co:5432/postgres
   ```
4. Or use individual parameters from the **Connection parameters** section:
   | Field | Value |
   |-------|-------|
   | Host | `db.xxxxxxxxxxxx.supabase.co` |
   | Port | `5432` |
   | Database name | `postgres` |
   | User | `postgres` |
   | Password | *(your project password)* |

#### Step 3: Configure `settings.py` for Supabase

Open `e_voting/settings.py` and replace the DATABASES section:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',                           # Supabase default DB name
        'HOST': 'db.xxxxxxxxxxxx.supabase.co',        # Your Supabase host
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'your-supabase-db-password',      # Password you set during project creation
    }
}
```

> ⚠️ **Replace** `db.xxxxxxxxxxxx.supabase.co` with your actual project host from Supabase dashboard.

#### Step 4: Install the PostgreSQL driver
```bash
pip install psycopg2-binary
```

#### Step 5: Allow External Connections (if needed)

In Supabase dashboard → **Settings → Database → Connection pooling**:
- Make sure **Connection pooling** is enabled for better performance
- Use port `6543` (pooler port) instead of `5432` if you face connection issues:

```python
'PORT': '6543',  # Use this if 5432 doesn't work on Supabase
```

---

### Option C — SQLite (Simplest, No Setup — Not for Production)

If you just want to test quickly without installing PostgreSQL, use SQLite (built into Python — no setup needed).

In `e_voting/settings.py`, replace DATABASES with:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

> ⚠️ SQLite is for **local testing only**. Do not use for production.

---

## 🚀 Run the Project

### Step 1: Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Create Admin Superuser
```bash
python manage.py createsuperuser
```
You will be prompted to enter:
- Email
- Password

**Or use this one-liner (Windows PowerShell):**
```powershell
$env:DJANGO_SUPERUSER_PASSWORD='Admin@123'
py manage.py createsuperuser --email admin@evoting.com --noinput
```

**Mac / Linux:**
```bash
DJANGO_SUPERUSER_PASSWORD='Admin@123' python manage.py createsuperuser --email admin@evoting.com --noinput
```

### Step 3: Start the Server

**Windows:**
```powershell
python manage.py runserver
```

**Mac / Linux:**
```bash
python3 manage.py runserver
```

Then open: **http://127.0.0.1:8000**

---

## 🔑 Default Login Credentials

> These are the credentials you created in the step above.

| Role | Email | Password |
|------|-------|----------|
| **Admin** | `admin@evoting.com` | `Admin@123` |
| **Voter** | *(create via admin panel or register page)* | *(set by admin)* |

Voter registration page: http://127.0.0.1:8000/account/register

---

## 📖 How the System Works

### Admin Setup (do this first):
1. **Login** as admin
2. **Create Positions** — e.g., President, Vice President (sidebar → Positions)
3. **Add Candidates** — assign each candidate to a position (sidebar → Candidates)
4. **Add Voters** — create voter accounts (sidebar → Voters)

### Voter Flow:
1. Go to http://127.0.0.1:8000
2. Login with email + password
3. Land directly on the **Ballot page** — no OTP required
4. Select candidates for each position
5. Click **Cast Vote**, review the preview
6. Confirm — done!

---

## 🔧 Common Issues & Fixes

### ❌ `psycopg2` Installation Error on Windows
```bash
pip install psycopg2-binary
```
Use `psycopg2-binary` (not `psycopg2`) — it includes pre-compiled binaries.

### ❌ `django.db.utils.OperationalError: could not connect to server`
- Make sure PostgreSQL service is running
- Check your `HOST`, `PORT`, `USER`, and `PASSWORD` in `settings.py`
- On Windows: search **Services** → find **postgresql-x64-XX** → Start

### ❌ `relation does not exist` error
You forgot to run migrations:
```bash
python manage.py migrate
```

### ❌ Supabase connection timeout
- Try using port `6543` instead of `5432` (connection pooler)
- Make sure your IP is not blocked — Supabase allows all IPs by default

### ❌ PDF print not working on Windows
WeasyPrint requires GTK3 libraries on Windows. The app runs without it (PDF feature simply won't work). To enable PDF:
- Download and install GTK3 runtime for Windows: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

---

## 📁 Project Structure

```
e-voting-with-django/
├── account/              → Login, Register, Logout views & forms
├── administrator/        → Admin dashboard views & templates
│   └── templates/admin/  → Admin HTML templates
├── voting/               → Ballot, Positions, Candidates, Votes
│   └── templates/voting/ → Voter-side HTML templates
├── e_voting/
│   ├── settings.py       → ⚙️ Database config goes here
│   └── urls.py           → URL routing
├── requirements.txt      → Python dependencies
└── manage.py             → Django management commands
```

---

## 📦 Requirements

Key packages in `requirements.txt`:

```
Django==4.1.13
psycopg2-binary        # PostgreSQL driver
Pillow                 # Image handling for candidate photos
django-renderpdf       # PDF generation (optional)
requests               # HTTP requests
```

---

## 👨‍💻 Developer

**Ravi Ranjan Kumar**  
🎓 Internship Project — 2026

---

## 📄 License & Credits

- Frontend template: [AdminLTE](http://adminlte.io)
- Original project base: [jobic10/e-voting-with-django](https://github.com/jobic10/e-voting-with-django)
- Images from [Unsplash](https://unsplash.com)
