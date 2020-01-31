from M2M.create_table_M2M import engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# 1.查询数据 - relationship 正向
# girl_obj_list = db_session.query(Girls).all()
# for girl in girl_obj_list:
#     for boy in girl.g2b:
#         print(girl.name,boy.name)


# 2.查询数据 - relationship 反向
# boy_obj_list = db_session.query(Boys).all()
# for boy in boy_obj_list:
#     for girl in boy.b2g:
#         print(girl.name,boy.name)
