from flask import Flask,request,render_template
from serv import content
from serv import get_set_anthing
from serv import users
from serv import devices
from serv import friend
from serv import chats

app = Flask(__name__)

app.register_blueprint(content.content)
app.register_blueprint(get_set_anthing.gsanthing)
app.register_blueprint(users.users)
app.register_blueprint(devices.devices)
app.register_blueprint(friend.friend)
app.register_blueprint(chats.chats)


@app.route("/")
def index():
    return render_template("toy.html")

if __name__ == '__main__':
    app.run("0.0.0.0",9527,debug=True)