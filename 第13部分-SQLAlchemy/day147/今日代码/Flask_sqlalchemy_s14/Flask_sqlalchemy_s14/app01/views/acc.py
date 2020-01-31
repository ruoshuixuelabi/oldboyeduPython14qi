from flask import Blueprint
from app01.models import User
from app01 import db


acc = Blueprint("acc",__name__)

@acc.route("/acc")
def acc_func():
    user_obj = User(name="Dragon")
    db.session.add(user_obj)
    db.session.commit()
    
    return "acc func"