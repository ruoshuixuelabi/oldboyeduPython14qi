# 5.创建 ORM 对象 及 关联数据表
from app01 import db
# db 啥也不知道

# db.Model # ORM模型基类

class User(db.Model):
    __tablename__ = "myuser"
    # __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.VARCHAR(32))
    


if __name__ == '__main__':
    # 6.绕过应用上下文创建 关联数据表,剩下的就是应用了
    from app01 import create_app
    app = create_app()
    db.drop_all(app=app)
    db.create_all(app=app)

