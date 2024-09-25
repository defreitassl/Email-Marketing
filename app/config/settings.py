import os
from dotenv import load_dotenv

load_dotenv()
database_uri = os.getenv('DATABASE_URL')

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = database_uri
