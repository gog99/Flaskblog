from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '37046177813704617781'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
