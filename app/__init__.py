from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from os import getenv
from fernet import Fernet

load_dotenv()

appl = Flask(__name__)
CORS(appl)
appl.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
db = SQLAlchemy(appl)
migrate = Migrate(appl, db)
ENCRYPTION_KEY = getenv('ENCRYPTION_KEY')
fernet = Fernet(ENCRYPTION_KEY.encode())



