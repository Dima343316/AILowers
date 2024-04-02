from flask import Flask,session
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa96edd6ee85d8c7ec1f155e3fda04301be162e3'
app.secret_key = 'secret key228 volkan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://constantine:dox123456@localhost/people'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

from sweater import models,routes

with app.app_context():
    db.create_all()

