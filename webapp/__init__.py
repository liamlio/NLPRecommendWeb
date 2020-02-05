from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt
from flask_ngrok import run_with_ngrok
from flask.ext.session import Session

app = Flask(__name__)

app.secret_key = b'3\x19R$\xae\x1e\xba[\xd0\x99Dd\xc7\xe4\x98\xb1'
#Session(app)

run_with_ngrok(app)
#Can't import routes above this since it creates circular imports
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from webapp import routes
