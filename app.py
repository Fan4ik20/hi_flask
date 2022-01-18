from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

db_engine = create_engine('sqlite:///hi.db')
