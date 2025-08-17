from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = (request.form.get("email") or "").lower()
        password = request.form.get("password") or ""
        
        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Email does not exist.', category='error')
        elif not check_password_hash(user.password, password):
            flash('Incorrect password. Try again.', category='error')
        else:
            login_user(user, remember=True)
            flash('Logged in successfully!', category='success')
            return redirect(url_for('views.passwords'))

    return render_template("login.html")

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = (request.form.get('user') or "").strip()
        email = (request.form.get('email') or "").lower().strip()
        password1 = (request.form.get('password') or "")
        password2 = (request.form.get('password1') or "")

        # Check if email or username already exist
        if not username or not email or not password1 or not password2:
            flash("All fields are required.", category="error")
        elif User.query.filter_by(email=email).first():
            flash('Email already exists.', category='error')
        elif User.query.filter_by(username=username).first():
            flash('Username already exists.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters long.', category='error')
        elif len(username) < 2:
            flash('Username must be at least 2 characters long.', category='error')
        elif len(email) < 4:
            flash('Email must be at least 4 characters long.', category='error')
        else:
            new_user = User(
                email=email,
                username=username,
                password=generate_password_hash(password1, method='pbkdf2:sha256')
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully!', category='success')
            return redirect(url_for('views.passwords'))

    return render_template("sign_up.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', category='info')
    return redirect(url_for('auth.login'))
