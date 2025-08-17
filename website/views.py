from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import Password

views = Blueprint('views', __name__)

# Home route
@views.route('/')
@views.route('/home')
@login_required
def home():
    return render_template("home.html", user=current_user)

# Password Manager Page
@views.route('/passwords')
@login_required
def passwords():
    user_passwords = Password.query.filter_by(user_id=current_user.id).all()
    return render_template("password_manager.html", passwords=user_passwords)

@views.route('/passwords/add', methods=['POST'])
@login_required
def add_password():
    site_name = request.form.get('site_name')
    site_url = request.form.get('site_url')
    site_password = request.form.get('site_password')

    if not site_name or not site_password:
        flash("Site name and password are required.", "error")
    else:
        new_password = Password(
            site_name=site_name,
            site_url=site_url,
            site_password=site_password,
            user_id=current_user.id
        )
        db.session.add(new_password)
        db.session.commit()
        flash("Password added successfully.", "success")
    return redirect(url_for('views.passwords'))


@views.route('/passwords/edit/<int:id>', methods=['POST'])
@login_required
def edit_password(id):
    password_entry = Password.query.get_or_404(id)
    if password_entry.user_id != current_user.id:
        flash("Unauthorized access.", "error")
        return redirect(url_for('views.passwords'))

    password_entry.site_name = request.form.get('site_name')
    password_entry.site_url = request.form.get('site_url')
    password_entry.site_password = request.form.get('site_password')

    db.session.commit()
    flash("Password updated successfully.", "success")
    return redirect(url_for('views.passwords'))


@views.route('/passwords/delete/<int:id>')
@login_required
def delete_password(id):
    password_entry = Password.query.get_or_404(id)
    if password_entry.user_id != current_user.id:
        flash("Unauthorized access.", "error")
        return redirect(url_for('views.passwords'))

    db.session.delete(password_entry)
    db.session.commit()
    flash("Password deleted successfully.", "success")
    return redirect(url_for('views.passwords'))
