from M2M.create_table_M2M import engine
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
db_session = Session()

# 1.增加数据 - relationship 正向
# girl_obj = Girls(name="赵丽颖")
# girl_obj.g2b = [Boys(name="DragonFire")]
# db_session.add(girl_obj)
# db_session.commit()

# 2.增加数据 - relationship 反向
# boy_obj = Boys(name="AlexDSB")
# boy_obj.b2g = [Girls(name="罗玉凤"),Girls(name="谢依霖")]
# db_session.add(boy_obj)
# db_session.commit()
