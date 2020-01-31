# from werkzeug.serving import run_simple
# from werkzeug.wrappers import Response,Request
#
# @Request.application
# def app(req):
#     print(req)
#     return Response("200 OK!")
#
#
# run_simple("0.0.0.0",9527,app)
#请求进来执行的是app()


#对象+()
class Abc(object):
    def __call__(self, *args, **kwargs):
        print("call被执行")

abc = Abc()

abc()