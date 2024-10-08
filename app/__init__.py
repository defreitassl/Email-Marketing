from flask import Flask
from app.config.settings import Config
from app.database import db
from app.routes.presentation import presentation
from app.routes.learn_more import learn_more
from app.routes.home import home
from app.routes.clients import client


def create_app():
    
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(presentation)
    app.register_blueprint(learn_more)
    app.register_blueprint(home)
    app.register_blueprint(client)

    return app