from werkzeug.wrappers import Response,Request
from werkzeug.serving import run_simple


@Request.application
def app(req):
    print(req)
    print(req.method)
    print(req.path)
    return Response("200 OK!")


run_simple(hostname="127.0.0.1",port=8800,application=app)

app()