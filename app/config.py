#coding=utf-8
import flask
import os
from flask import send_from_directory, request, session, jsonify
from datetime import datetime
from encryption import Encryption
from sqlalchemy.sql.functions import user
from werkzeug.security import generate_password_hash
# Under import all classes from models.py
from models import encrypt, Groups, home_about, db
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql.expression import func
from sqlalchemy import desc, null, true, update, and_
from oauthlib.oauth2 import WebApplicationClient
from flask_session import Session
import flask_login
from google_auth_oauthlib.flow import Flow
from dotenv import load_dotenv

load_dotenv()

app = flask.Flask(__name__)
app.secret_key = "11d56c24aad491f45aac7a00f7adf03a3d922122682f276b"     # Secret key for sessions

## Flask login initialisations
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.session_protection = None


DEV_PORT = 5000  # Dev port
PRO_PORT = 80    # Production default port

DEV_HOST = 'localhost' # Dev host
PRO_HOST = '0.0.0.0'   # Production default host

# An attempt to limit SQL connetion reset
SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True, 
        "pool_recycle": 300 }



##### SETTINGS ######
#mode = 'production'
mode = 'development'

#db_mode = 'production'
db_mode = 'development'


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
if mode == 'development':
    toolbar = DebugToolbarExtension(app)
    # Kanskje denne må på i production også

# Google Login settings

# Database settings


app.debug = True
encrypt.development()
toolbar = DebugToolbarExtension(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MY_SQL_USER')}:{os.getenv('MY_SQL_PASSWORD')}@{os.getenv('MY_SQL_URL')}/it_nettside"
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_SIZE'] = 50
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 50


db.init_app(app) #adds the app to the database from models.py
with app.app_context():
    db.create_all()



" Session initialisations"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


