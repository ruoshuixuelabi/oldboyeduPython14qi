from flask import Flask

app = Flask(__name__)

from .views.user import user
from .views.acc import acc


def create_app():
    app.config["DEBUG"] = True
    app.register_blueprint(user)
    app.register_blueprint(acc)
    return app