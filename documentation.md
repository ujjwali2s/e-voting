# 🗳️ E-Voting System — Complete Documentation

> **Internship Project** | Developed by **Ravi Ranjan Kumar**  
> **Tech Stack:** Django 4.1 · PostgreSQL · Python 3.12  
> **Server:** http://127.0.0.1:8000

---

## ✅ Test Results (All Passed)

| Step | Action | Result |
|------|--------|--------|
| 1 | Create Voter from Admin panel | ✅ PASS |
| 2 | Admin Logout | ✅ PASS |
| 3 | Voter Login (No OTP required) | ✅ PASS |
| 4 | Cast Vote (President + Vice President) | ✅ PASS |
| 5 | Voter Logout | ✅ PASS |
| 6 | Admin Login & Verify Vote Results | ✅ PASS |

---

## 🚀 How to Start the Server

Open a terminal in the project folder and run:

```powershell
cd e:\projects\projects\ujjwal\python\e-voting-with-django
py -3.12 manage.py runserver
```

Then open your browser and go to: **http://127.0.0.1:8000**

---

## 🔑 Login Credentials

### Admin Account
| Field | Value |
|-------|-------|
| **URL** | http://127.0.0.1:8000 |
| **Email** | `admin@evoting.com` |
| **Password** | `Admin@123` |

### Test Voter Account
| Field | Value |
|-------|-------|
| **Email** | `voter1@test.com` |
| **Password** | `Voter@123` |

---

## 👨‍💼 ADMIN GUIDE

### Step 1 — Login
1. Go to http://127.0.0.1:8000
2. Enter Email: `admin@evoting.com`
3. Enter Password: `Admin@123`
4. Click **Sign In**
5. You land on the **Admin Dashboard** showing live stats

---

### Step 2 — Create Positions (e.g. President, Vice President)
1. Click **Positions** in the left sidebar
2. Click the blue **+ New** button
3. Enter the Position **Name** (e.g. `President`)
4. Enter **Max Vote** = `1` (how many candidates a voter can pick)
5. Click **Save**
6. Repeat for other positions (e.g. `Vice President`)

---

### Step 3 — Add Candidates
1. Click **Candidates** in the sidebar
2. Click **+ New**
3. Fill in:
   - **Fullname** — candidate's full name
   - **Bio** — short description
   - **Position** — select from dropdown (must be created first)
   - **Photo** — upload an image (optional but recommended)
4. Click **Save**
5. Repeat for all candidates

---

### Step 4 — Add Voters
1. Click **Voters** in the sidebar
2. Click **+ New**
3. Fill in:
   - **Last name** — voter's last name
   - **First name** — voter's first name
   - **Email** — unique email address
   - **Password** — set a password for the voter
4. Click **Save**
5. The voter can now log in and vote

> **Note:** Voters can also self-register at http://127.0.0.1:8000/account/register

---

### Step 5 — Monitor Votes (Dashboard)
- The Dashboard shows:
  - **No. of Positions** — total election positions
  - **No. of Candidates** — total candidates registered
  - **Total Voters** — all registered voters
  - **Voters Voted** — how many have cast their vote
  - **Live bar charts** for each position showing vote counts

---

### Step 6 — View Detailed Votes
1. Click **Votes** in the sidebar
2. See a complete table of who voted for whom

---

### Step 7 — Reset All Votes (Start Fresh)
1. Go to **Votes** in the sidebar
2. Click the **Reset** button
3. All votes are cleared and voters can vote again

---

### Step 8 — Change Election Title
1. Click **Election Title** in the sidebar
2. Update the title shown on the ballot page
3. Click **Save**

---

### Step 9 — Manage Ballot Position Order
1. Click **Ballot Position** in the sidebar
2. Drag/reorder positions to control the order they appear on the ballot

---

## 🧑‍💻 VOTER GUIDE

### Step 1 — Register (Self Registration)
1. Go to http://127.0.0.1:8000/account/register
2. Fill in:
   - **Last name**
   - **First name**
   - **Email**
   - **Password**
3. Click **Register**
4. You're redirected to the login page

> Or ask your admin to create an account for you.

---

### Step 2 — Login
1. Go to http://127.0.0.1:8000
2. Enter your **Email** and **Password**
3. Click **Sign In**
4. You land directly on the **Ballot Page** _(No OTP required)_

---

### Step 3 — Cast Your Vote
1. You see the ballot with all positions and candidates
2. For each position, **click the radio button** next to your preferred candidate
3. Click the **View Platform** button to read a candidate's bio (optional)
4. Once done, scroll down and click **Cast Vote**
5. A preview summary appears — review your choices
6. Click **Confirm** to submit your vote
7. You see a **"Thanks for voting"** confirmation message

> ⚠️ **You can only vote once.** After voting, you can view your results but cannot change them.

---

### Step 4 — View Your Results
After voting, when you log in again you will see:
- A list of the candidates you voted for
- Results for each position

---

### Step 5 — Logout
- Click **Logout** in the left sidebar at any time

---

## 🗄️ Database Information

| Field | Value |
|-------|-------|
| **Engine** | PostgreSQL |
| **Database Name** | `evoting_db` |
| **User** | `postgres` |
| **Password** | `password` |
| **Host** | `localhost` |
| **Port** | `5432` |

---

## 🔧 Developer Notes

### Running Migrations
```powershell
py -3.12 manage.py makemigrations
py -3.12 manage.py migrate
```

### Creating a New Superuser/Admin
```powershell
$env:DJANGO_SUPERUSER_PASSWORD='Admin@123'
py -3.12 manage.py createsuperuser --email admin@evoting.com --noinput
```

### Project Structure
```
e-voting-with-django/
├── account/          → Login, Register, Logout
├── administrator/    → Admin views, templates
├── voting/           → Ballot, Positions, Candidates, Votes
├── e_voting/         → Settings, URLs
└── manage.py
```

### Key Changes Made (vs original)
- ✅ **OTP/Phone removed** — voters login directly, no SMS verification
- ✅ **PostgreSQL** instead of MySQL/SQLite
- ✅ **Developer credit** — Ravi Ranjan Kumar, Internship Project
- ✅ **Django 4.1.13** for Python 3.12 compatibility
- ✅ **WeasyPrint** imported conditionally (PDF works if GTK3 installed)

---

## 📞 Support & Contact

> **Developer:** Ravi Ranjan Kumar  
> **Project Type:** Internship Project  
> **Year:** 2026
