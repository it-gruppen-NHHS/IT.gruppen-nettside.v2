#coding=utf-8
import flask
import os
from flask import send_from_directory, request, session, jsonify
from datetime import datetime
from encryption import Encryption
from sqlalchemy.sql.functions import user
from werkzeug.security import generate_password_hash
# Under import all classes from models.py
from models import encrypt, Groups
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql.expression import func
from sqlalchemy import desc, null, true, update, and_
from oauthlib.oauth2 import WebApplicationClient
from flask_session import Session
import flask_login
from google_auth_oauthlib.flow import Flow


app = flask.Flask(__name__)
app.secret_key = "s_key"     # Secret key for sessions

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



# Read other schema in same db connection
from sqlalchemy.sql import text

def create_class(name, fields):
    """Dynamically creates a class."""
    return type(name, (object,), fields)

def read_from_other_schema_into_class(db, schema, table):
    """
    input: db, schema, table
    output: list of class instances
    Description: Reads all rows from a table in a different schema and creates a class instance for each row.
    """
    query = text(f"SELECT * FROM {schema}.{table}")
    result = db.engine.execute(query)
    columns = result.keys()

    entities = []
    for row in result.fetchall():
        # Map column names to row values for the current row
        fields = dict(zip(columns, row))
        
        # Create a class name based on the table name (could be adjusted for naming conventions)
        ClassName = ''.join(word.title() for word in table.split('_'))
        
        # Dynamically create a class with the row data
        EntityClass = create_class(ClassName, fields)
        
        # Instantiate the class and add it to the entities list
        entity = EntityClass()
        entities.append(entity)
    
    return entities










" Session initialisations"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


