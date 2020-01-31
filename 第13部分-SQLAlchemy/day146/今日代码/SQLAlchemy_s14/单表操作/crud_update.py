# update table set name="123"

# 创建查询窗口
from sqlalchemy.orm import sessionmaker
from 单表操作.create_table import engine

Session = sessionmaker(engine)
db_session = Session()

# 1.修改一条数据
# user_obj = db_session.query(User).filter(User.id == 1).update({"name":"Dragon"})
# db_session.commit()

# 2.修改多条数据
# user_obj = db_session.query(User).filter(User.id >= 1).update({"name":"666"})
# db_session.commit()
