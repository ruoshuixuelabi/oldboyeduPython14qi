from flask import Blueprint
from app01 import db
from app01.models import User

user = Blueprint("user", __name__)


@user.route("/user")
def user_func():
    # res = User.query.first() # User.query == db_session.query(User)
    res = db.session.query(User).first()
    print(res,res.name)
    
    return "user func"