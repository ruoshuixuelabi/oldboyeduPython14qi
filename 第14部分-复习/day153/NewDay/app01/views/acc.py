from flask import Blueprint

acc = Blueprint("acc",__name__)

@acc.route("/acc")
def acc_func():
    return "I am acc_func"

