import os
from dotenv import load_dotenv

load_dotenv()
database_uri = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = database_uri
    SECRET_KEY = secret_key