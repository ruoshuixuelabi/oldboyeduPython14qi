from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

class Girls(Base):
    __tablename__ = "girl"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    g2b = relationship("Boys",backref="b2g",secondary="hotel")

class Boys(Base):
    __tablename__ = "boy"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))

class Hotel(Base):
    __tablename__ = "hotel"
    id = Column(Integer, primary_key=True)
    boy_id = Column(Integer,ForeignKey("boy.id"))
    girl_id = Column(Integer,ForeignKey("girl.id"))


from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/sqlalchemy_s14?charset=utf8")

Base.metadata.create_all(engine)
