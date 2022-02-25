from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

# import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '37046177813704617781'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# Flask_mail setup for Google email
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'qtest5027@gmail.com'
#password = os.getenv('MAIL_PASS', None)
#if password is None:
#  raise ValueError('password missin')
app.config['MAIL_PASSWORD'] = '#'
mail = Mail(app)

from core import routes
