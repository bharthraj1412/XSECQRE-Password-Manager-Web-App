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

## Installation:
```bash
git clone https://github.com/yourusername/xsecqre-password-manager.git
cd xsecqre-password-manager
pip install -r requirements.txt
python app.py

