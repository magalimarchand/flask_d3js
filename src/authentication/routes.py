from src import db, bcrypt
from src.authentication.models import User
from src.authentication.forms import (RegistrationForm, LoginForm, 
																		UpdateAccountForm, ResetRequestForm, ResetPasswordForm)
from src.authentication.utils import save_image, send_reset_email
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required


authentication = Blueprint('authentication', __name__)



# REGISTER
@authentication.route('/register', methods=['GET','POST'])
def register(): 
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = RegistrationForm() 
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Votre compte a été créé, vous pouvez maintenant vous connecter.', 'success')
		return redirect(url_for('authentication.login'))
	return render_template('authentication/register.html', title='Register', form=form)


# LOGIN
@authentication.route('/login', methods=['GET','POST'])
def login(): 
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			# http://localhost:5000/login?next=%2Faccount
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('main.home'))
		else:
			flash('Erreur de connexion, email ou mot de passe incorrect', 'danger')
	return render_template('authentication/login.html', title='Login', form=form)


# LOGOUT
@authentication.route('/logout')
def logout(): 
	logout_user()
	return redirect(url_for('main.home'))


# ACCOUNT
@authentication.route('/account', methods=['GET','POST'])
@login_required
def account(): 
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.image.data:
			image_file = save_image(form.image.data)
			current_user.image_file = image_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Votre compte a bien été modifié!', 'success')
		return redirect(url_for('authentication.account')) #to avoid double submit
	elif request.method == 'GET': #to fill form with current infos
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	return render_template('authentication/account.html', title='Account', image_file=image_file, form=form)



# SEND EMAIL (TO RESET PASSWORD)
@authentication.route('/reset_password', methods=['GET','POST'])
def reset_request(): 
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = ResetRequestForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		send_reset_email(user)
		flash('Un courriel a été envoyé pour réinitialiser le mot de passe.', 'info')
		return redirect(url_for('authentication.login'))
	return render_template('authentication/reset_request.html', title='Réinitialiser le mot de passe', form=form)


# RESET PASSWORD
@authentication.route('/reset_password/<token>', methods=['GET','POST'])
def reset_password(token): 
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	user = User.verify_reset_token(token)
	if user is None:
		flash('L\'Authentification est invalide ou expirée.', 'warning')
		return redirect(url_for('authentication.reset_request'))
	form = ResetPasswordForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user.password = hashed_password
		db.session.commit()
		flash('Votre mot de passe a été modifié, vous pouvez maintenant vous connecter.', 'success')
		return redirect(url_for('authentication.login'))
	return render_template('authentication/reset_password.html', title='Nouveau mot de passe', form=form)

