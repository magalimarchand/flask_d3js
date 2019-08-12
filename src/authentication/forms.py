from src.authentication.models import User
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed



# REGISTRATION
class RegistrationForm(FlaskForm):

	username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=2,max=20)])
	email = StringField('Adresse courriel', validators=[DataRequired(), Email()])
	password = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6,max=25)])
	confirm_password = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('M\'enregistrer')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Cette adresse courriel est déjà prise. Veuillez en choisir une autre.')


# LOGIN
class LoginForm(FlaskForm):

	email = StringField('Adresse courriel', validators=[DataRequired(), Email()])
	password = PasswordField('Mot de passe', validators=[DataRequired()])
	remember = BooleanField('Se rappeler de moi')
	submit = SubmitField('Me connecter')


# UPDATE ACCOUNT
class UpdateAccountForm(FlaskForm):

	username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=2,max=20)])
	email = StringField('Adresse courriel', validators=[DataRequired(), Email()])
	image = FileField('Modifier l\'image de profil', validators=[FileAllowed(['jpg','png'])])
	submit = SubmitField('Modifier')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Ce nom d\'utilisateur est déjà pris. Veuillez en choisir un autre.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Cette adresse courriel est déjà prise. Veuillez en choisir une autre.')


# SEND EMAIL
class ResetRequestForm(FlaskForm):

	email = StringField('Adresse e-mail', validators=[DataRequired(), Email()])
	submit = SubmitField('Réinitialiser le mot de passe')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('Cette Adresse courriel n\'est pas associée à un compte. Veuillez vous enregistrer.')


# RESET PASSWORD
class ResetPasswordForm(FlaskForm):

	password = PasswordField('Mot de passe', validators=[DataRequired(), Length(min=6,max=25)])
	confirm_password = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Enregistrer le nouveau mot de passe')