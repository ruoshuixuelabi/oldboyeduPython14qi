# ORM
# 1.Class - Obj
# 2.创建数据库引擎
# 3.将所有的Class序列化成数据表
# 4.ORM操作 - CRUD

# 1.创建一个 Class
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Base 是 ORM模型 基类
# ORM模型 - Obj里面的属性 == table中创建的字段
#        - Obj定义table的操作方式和属性

from sqlalchemy import Column,Integer,INT,INTEGER,VARCHAR,String

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32),index=True)
    

# 2.创建数据引擎
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/sqlalchemy_s14?charset=utf8")

# 3.将所有的继承Base的Class序列化成数据表
Base.metadata.create_all(engine)


