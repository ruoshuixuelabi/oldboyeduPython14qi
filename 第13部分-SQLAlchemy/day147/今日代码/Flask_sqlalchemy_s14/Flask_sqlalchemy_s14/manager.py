import app01
from flask_script import Manager

app = app01.create_app()
manager = Manager(app)

from flask_migrate import Migrate,MigrateCommand
Migrate(app,app01.db)

manager.add_command("db",MigrateCommand)

"""
数据库迁移指令:
python manager.py db init
python manager.py db migrate   # Django中的 makemigration
python manager.py db upgrade  # Django中的 migrate
"""


@manager.command
def look_at(args):
    print("123",args)
    return 456


@manager.option("-n","--name",dest="name")
@manager.option("-s","--say",dest="say")
def run_flask(name,say):
    app.run(host=name,port=int(say))
    print(f"{name}真{say}")
    
    
    

if __name__ == '__main__':
    manager.run()