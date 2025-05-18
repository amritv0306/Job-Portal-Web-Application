# 🚀 Job Portal Web Application

A comprehensive job portal built with Flask and SQLite where users can post job listings, search for jobs, and apply for positions.

Live Link: 
https://job-portal-web-application-1ekb.onrender.com
---

## 👥 User Roles

- 🧑‍💼 **Job Seekers**: Register, search for jobs, and submit applications  
- 👔 **Employers**: Post job listings and manage applications  
- 🛡️ **Administrators**: Manage users, job listings, and applications

---

## 🔍 Core Functionality

- 🔐 User registration and authentication  
- 📝 Job posting with detailed information (title, description, salary, location)  
- 🔎 Advanced job search with multiple filters (location, category, company)  
- 📨 Job application submission and tracking  
- 📊 Employer dashboard for managing job listings and reviewing applications  
- ⚙️ Admin dashboard for site management

---

## 🛠️ Tech Stack

- 🐍 **Backend**: Python (Flask)  
- 🎨 **Frontend**: HTML, CSS, Bootstrap 5  
- 💾 **Database**: SQLite  
- 🔒 **Authentication**: Flask-Login  
- 📋 **Forms**: Flask-WTF

---

## 🚀 Installation and Setup

### 📋 Prerequisites

- Python 3.8 or higher  
- pip (Python package manager)

### 💻 Local Development Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/job-portal.git
cd job-portal
```

2. **Create and activate a virtual environment**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set environment variables**

```bash
# On Windows
set FLASK_APP=app.py
set FLASK_ENV=development

# On macOS/Linux
export FLASK_APP=app.py
export FLASK_ENV=development
```

5. **Initialize the database**

The database will be created when you run the application using:

```python
with app.app_context():
    db.create_all()
```

6. **Run the application**

```bash
flask run
```

Access the application at: http://127.0.0.1:5000/

---


## 📁 Project Structure
``` csharp
job_portal/
├── app.py              # Main application file
├── models.py           # Database models
├── forms.py            # Form definitions
├── config.py           # Configuration settings
├── requirements.txt    # Dependencies
├── static/             # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
└── templates/          # HTML templates
    ├── base.html
    ├── index.html
    ├── auth/
    │   ├── login.html
    │   └── register.html
    ├── jobs/
    │   ├── create.html
    │   ├── detail.html
    │   └── search.html
    ├── profile/
    │   ├── job_seeker.html
    │   ├── employer.html
    │   └── applications.html
    └── admin/
        └── dashboard.html
```

---

## 📝 Usage

### 🧑‍💼 For Job Seekers
- Register for an account with the "Job Seeker" role
- Browse available jobs using the search functionality
- View job details and submit applications
- Track application status from your profile

### 👔 For Employers
- Register for an account with the "Employer" role
- Post new job listings with detailed information
- Manage your job listings from your dashboard
- Review applications and contact candidates

### 🛡️ For Administrators
- Access the admin dashboard
- Manage users, job listings, and applications
- Monitor site activity and maintain the platform

---

## 🤝 Contributing

- Fork the repository

- Create a feature branch
```bash
git checkout -b feature/amazing-feature
```

- Commit your changes
```bash
git commit -m 'Add some amazing feature'
```

- Push to the branch
```bash
git push origin feature/amazing-feature
```

- Open a Pull Request

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## ✨ Created as a final project for the Web Development with Flask course.
```vbnet
Let me know if you'd like this saved to a file directly
```