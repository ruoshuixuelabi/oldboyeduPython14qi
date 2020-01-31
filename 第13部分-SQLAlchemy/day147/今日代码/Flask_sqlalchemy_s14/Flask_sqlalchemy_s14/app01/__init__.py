from flask import Flask
# 1.导入Flask-sqlalchemy 中的SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# 2.实例化 Flask-sqlalchemy 中的 SQLAlchemy 对象
# 此操作一定要在导入蓝图之前
db = SQLAlchemy()

# Session(app)
# app.config["SESSION_TYPE"] = "redis"

# 为什么db一定要在导入蓝图之前
from .views.acc import acc
from .views.user import user

def create_app():
    app = Flask(__name__)
    # 3.基于上下文进行SQLAlchemy的配置
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:dd112211@127.0.0.1:3306/sqlalchemy?charset=utf8"
    app.config["SQLALCHEMY_POOL_SIZE"] = 10
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    app.config["DEBUG"] = True
    
    # 4.SQLAlchemy初始化App的相关配置
    db.init_app(app)  # 通过 init_app可以查看SQLAlchemy的配置关键字
    
    app.register_blueprint(acc)
    app.register_blueprint(user)
    
    return app