from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column,INT,VARCHAR,ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "student"
    id = Column(INT,primary_key=True)
    name = Column(VARCHAR(32))
    school_id = Column(INT,ForeignKey("school.id"))
    stu2sch = relationship("School",backref="sch2stu")

class School(Base):
    __tablename__ = "school"
    id = Column(INT,primary_key=True)
    name = Column(VARCHAR(32))
    
    
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/sqlalchemy_s14?charset=utf8")


Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

