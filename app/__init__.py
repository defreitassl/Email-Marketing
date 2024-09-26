from flask import Flask
from app.config.settings import Config
from app.database import db
from app.routes.home import home


def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(home)

    return app