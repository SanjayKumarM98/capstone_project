from flask import Flask,request,Blueprint,make_response,jsonify,session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import uuid  # used to generate public id
from werkzeug.security import generate_password_hash, check_password_hash

import jwt
from datetime import datetime,timedelta
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://sanjay:password@localhost/capstone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sanjay@divum.in'
app.config['MAIL_PASSWORD'] = 'Muniyappa@98#'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
