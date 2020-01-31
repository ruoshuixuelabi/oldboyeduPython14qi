# delete from table

# 创建查询窗口
from sqlalchemy.orm import sessionmaker
from 单表操作.create_table import engine

Session = sessionmaker(engine)
db_session = Session()

# 1.删除数据
# res = db_session.query(User).filter(User.id == 1).delete()
# db_session.commit()

# 2.删除多条数据
# res = db_session.query(User).filter(User.id>=1).delete()
# db_session.commit()