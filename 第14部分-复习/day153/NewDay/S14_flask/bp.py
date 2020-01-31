from flask import Blueprint
bp = Blueprint("bp",__name__,url_prefix="/user")

@bp.route("/bp")
def bp_func():
    return "bp_func"


from flask import Flask
app = Flask(__name__)

app.register_blueprint(bp)

app.run()