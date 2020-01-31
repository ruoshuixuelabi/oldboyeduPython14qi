from 高级操作.create_table import engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# res = db_session.query(User).filter(User.id == 1,User.name=="小笼包").first()
# res = db_session.query(User).filter(or_(User.id == 1,User.name=="小笼包")).all()
# res = db_session.query(User).filter(and_(User.id==1,or_(User.name=="小笼包",User.gender=="女"))).all()
# print(res[0].name)

# res = db_session.query(User.gender,User.name).filter(User.id == 1,User.name=="赵丽颖").first()

# res = db_session.query(User.gender.label("xb"),User.name).filter(User.id == 1,User.name=="赵丽颖").first()

# res = db_session.query(User).order_by(User.id.desc()).all()
# res = db_session.query(User).order_by(User.name).all()
# for row in res:
#     print(row.id,row.name)


# res = db_session.query(User).filter(User.id.between(2,4)).order_by(User.id.desc()).all()
# for row in res:
#     print(row.id)

# res = db_session.query(User).filter(User.id.notin_([1,4,3])).all()
# res = db_session.query(User).filter(User.id.in_([1,4,3])).all()
# for row in res:
#     print(row.id)


# from sqlalchemy.sql import text
#
# r6 = db_session.query(User).filter(text("id<:value and name=:name")).params(value=4, name='DragonFire').all()
# print(r6)
#
# r7 = db_session.query(User).from_statement(text("SELECT * FROM User where name=:name")).params(name='DragonFire').all()
# print(r7)

# from sqlalchemy.sql import func
#
# res = db_session.query(func.count(User.gender).label("count"),User.gender).group_by(User.gender).all()
# print(res)
#
# for row in res :
#     print(row.gender,row.count)