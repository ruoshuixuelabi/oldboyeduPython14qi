from flask import Flask,request


app = Flask(__name__)

@app.route("/")
def index():
    request.method
    
    return "123"


if __name__ == '__main__':
    app.run()
    app.__call__
    app.wsgi_app