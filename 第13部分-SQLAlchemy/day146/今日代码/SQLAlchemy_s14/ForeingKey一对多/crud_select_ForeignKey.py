from sqlalchemy.orm import sessionmaker
from ForeingKey一对多.create_table_ForeignKey import engine

Session = sessionmaker(engine)
db_session = Session()

# 1.查询 笨
# sch_obj = db_session.query(School).filter(School.name == "OldBoyBeijing").first()
# beijing_stu_obj = db_session.query(Student).filter(Student.school_id == sch_obj.id).first()
# print(beijing_stu_obj.name,sch_obj.name)

# 2.relationship 正向查询
# stu_obj = db_session.query(Student).filter(Student.name=="DragonFire").first()
# print(stu_obj.name,stu_obj.stu2sch.name)

# 3.relationship 反向查询
# sch_obj_list = db_session.query(School).all()
# for row in sch_obj_list:
#     for stu in row.sch2stu:
#         print(row.name,stu.name)