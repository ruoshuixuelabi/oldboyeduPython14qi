#1.选中数据库 - 创建数据库引擎 导入数据库引擎
#2.创建查询窗口,必须是选中数据库的查询窗口
#3.创建sql语句
#4.点击运行

#1.选中数据库 - 创建数据库引擎 导入数据库引擎
from 单表操作.create_table import engine

#2.创建查询窗口,必须是选中数据库的查询窗口
from sqlalchemy.orm import sessionmaker
Session_window = sessionmaker(engine)
# 打开查询窗口
db_session = Session_window()


# 1.增加数据 - #3.创建sql语句
# insert into table(name) values("123")
# from create_table import User
# user_obj = User(name="DragonFire") # 创建sql语句
# db_session.add(user_obj) # 将sql语句粘贴到查询窗口中
#4.点击运行
# db_session.commit() # 执行全部的sql语句
# db_session.close()

# 2.增加多条数据
# from create_table import User
# user_obj_list = [User(name="赵丽颖"),User(name="陈妍希")]
# db_session.add_all(user_obj_list)
# db_session.commit()
# db_session.close()
