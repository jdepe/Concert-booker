from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

#create a blueprint
bp = Blueprint('auth', __name__ )

@bp.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #get data from form
        username = form.user_name.data
        password = form.password.data
        
        check_user = User.query.filter_by(name=username).first()
        
        # check if user exists in db
        if check_user is not None:
            if check_password_hash(check_user.password_hash, password):
                # username and password are correct
                flash(f'Welcome, {check_user.name}!', 'success')
                login_user(check_user)
                return redirect(url_for('main.index'))
        flash(f'Incorrect credentials!', 'warning')
        
    return render_template('user.html', form=form, heading='Login')

@bp.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #get data from the form
        username = form.user_name.data
        email = form.email_id.data
        password = form.password.data
           
        #check if a user exists
        check_user = User.query.filter_by(name=username).first()
        if check_user is None:
            # There is not a user - we are ok to create
            new_user = User(
                name=username,
                email_id=email, 
                password_hash=generate_password_hash(password) 
            )
            
            db.session.add(new_user)
            db.session.commit()
            flash(f'Successfully registered, {new_user.name}!', 'primary')
            return redirect(url_for('auth.login'))

        flash(f'That user already exists!', 'warning')

    return render_template('user.html', form=form, heading='Register')

@bp.route('/logout', methods=["POST", "GET"])
@login_required
def logout():
    logout_user()
    flash(f'You have been logged out', 'info')
    return redirect(url_for('main.index'))