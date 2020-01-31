from sqlalchemy.orm import sessionmaker
from ForeingKey一对多.create_table_ForeignKey import engine

Session = sessionmaker(engine)
db_session = Session()

# 1.增加数据 笨
# sch_obj = School(name="OldBoyBeijing")
# db_session.add(sch_obj)
# db_session.commit()
#
# sch_obj = db_session.query(School).filter(School.name=="OldBoyBeijing").first()
#
# stu_obj = Student(name="DragonFire",school_id=sch_obj.id)
# db_session.add(stu_obj)
# db_session.commit()

# 2 Relationship 版 添加数据操作 - 正向
# stu_obj = Student(name="DragonFire",stu2sch=School(name="OldBoyBeijing"))
# db_session.add(stu_obj)
# db_session.commit()

# 3 Relationship 版 添加数据操作 - 反向
# sch_obj = School(name="OldBoyShanghai")
# sch_obj.sch2stu = [Student(name="赵丽颖"),Student(name="陈妍希")]
# db_session.add(sch_obj)
# db_session.commit()


