from flask import Flask
from .views.user import user
from .views.acc import acc



def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    app.register_blueprint(user)
    app.register_blueprint(acc)

    return app