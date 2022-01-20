import os

from flask import Flask
from sqlalchemy import create_engine

from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv(".env")


if os.getenv('DATABASE'):
    db_engine = create_engine(
        f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}'
        f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}'
        f'/{os.getenv("DATABASE")}'
    )
else:
    db_engine = create_engine('sqlite:///hi.db')
