from flask import Flask,request,render_template
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

from geventwebsocket.websocket import WebSocket


app = Flask(__name__)  # type:Flask

user_socket_list = []

@app.route("/ws")
def ws():
    user_socket = request.environ.get("wsgi.websocket") # type:WebSocket
    if user_socket:
        user_socket_list.append(user_socket)
    print(len(user_socket_list),user_socket_list)
    while 1:
        msg = user_socket.receive()
        print(msg)
        for usocket in user_socket_list:
            if user_socket == usocket:
                continue
            try:
                usocket.send(msg)
            except:
                continue

        
@app.route("/")
def index():
    return render_template("ws.html")
    
    



if __name__ == '__main__':
    # app.run("0.0.0.0",5000,debug=True)
    http_serv = WSGIServer(("0.0.0.0",5000),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()