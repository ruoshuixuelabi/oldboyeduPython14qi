from flask import Flask,request
from serv import content
from serv import get_set_anthing
from serv import users
from serv import devices

app = Flask(__name__)

app.register_blueprint(content.content)
app.register_blueprint(get_set_anthing.gsanthing)
app.register_blueprint(users.users)
app.register_blueprint(devices.devices)

if __name__ == '__main__':
    app.run("0.0.0.0",9527,debug=True)