from 高级操作.create_table import engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# 引用增加
# res = db_session.query(User).update({User.age: User.age + 1},synchronize_session=False)
# print(res)

# db_session.query(User).filter(User.id > 0).update({"age": User.age + 1}, synchronize_session="evaluate")
# db_session.commit()