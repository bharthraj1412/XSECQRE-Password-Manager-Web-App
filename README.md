# XSECQRE – Secure Password Manager

XSECQRE is a web-based **password manager** built with **Python, Flask, and SQLite**.  
It allows users to **sign up, log in, and securely store, view, update, and delete passwords**. Each user can only access their own data, and passwords are stored as **hashed values** for security.

---

## Features

- User authentication (signup, login, logout)  
- Passwords securely hashed using **PBKDF2 SHA-256**  
- CRUD operations for managing personal credentials  
- Each user can only access their own passwords  
- Responsive design using **Bootstrap 5**

---

## Project Structure

passwordmanager/
│
├─ website/
│ ├─ init.py # Flask app initialization
│ ├─ models.py # Database models for User & Password
│ ├─ views.py # Routes for home & password manager
│ ├─ auth.py # Routes for login, signup, logout
│ └─ templates/ # HTML templates (base, login, signup, home, password manager)
│
├─ static/ # CSS, images, logo
├─ data.db # SQLite database (auto-generated)
└─ app.py # Main file to run the Flask app


---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/xsecqre-password-manager.git
cd xsecqre-password-manager
pip install -r requirements.txt
python app.py

