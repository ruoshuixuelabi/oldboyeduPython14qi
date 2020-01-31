# select * from {table}

# 创建查询窗口
from 单表操作.create_table import engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# 1.查询数据:
# user_obj = db_session.query(User).first()
# print(user_obj.id,user_obj.name)
#
# user_obj_list = db_session.query(User).all()
# print(user_obj_list)
# for row in user_obj_list:
#     print(row.id,row.name)

# 2.带条件的查询
# user_obj_list = db_session.query(User).filter(User.id <= 2,User.name == "赵丽颖").all()
# print(user_obj_list)
# for row in user_obj_list:
#     print(row.id,row.name)

# user_obj_list = db_session.query(User).filter_by(id=2,name="赵丽颖").all()
# print(user_obj_list)
# for row in user_obj_list:
#     print(row.id,row.name)


