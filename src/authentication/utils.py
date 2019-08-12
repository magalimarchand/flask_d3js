from src import mail
from flask import current_app, url_for
from flask_mail import Message
from PIL import Image
import secrets #generate secure random numbers
import os #filesystem module



# SAVE IMAGE
def save_image(form_image):
	#create new randomized filename (preserve extension)
	random_hex = secrets.token_hex(8)
	_, file_ext = os.path.splitext(form_image.filename) # _ = variable not used
	image_filename = random_hex + file_ext
	image_path = os.path.join(current_app.root_path, 'static/profile_pics', image_filename)
	#resize image
	output_size = (256,256)
	resized_image = Image.open(form_image)
	resized_image.thumbnail(output_size)
	#save image
	resized_image.save(image_path)
	return image_filename



# CONFIGURE EMAIL CONTENT
def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Réinitialisation du mot de passe', 
								sender='noreply@demo.com', 
								recipients=[user.email])
	#with f string, only one curly braces pair instead of 2
	#_external option to get tueh abosulte path of reset_password.html page
	msg.body = f'''Pour réinitialiser votre mot de passe, cliquez sur le lien ci-dessous:
{url_for('authentication.reset_password', token=token, _external=True)}

Si vous n'avez pas demandé cette demande de réinitialisation de mot de passe, ignorez ce courriel et aucun changement ne sera effectué.
'''
	mail.send(msg)