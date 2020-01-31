# Flask
# 1.Flask 启动
# from flask import Flask , url_for
# from 来自
# form 表 - orm - 操纵表的 - form
# app = Flask(__name__)

# 4.Flask 路由
# endpoint="index" # 反向URL地址解析
# strict_slashes=True # 是否严格遵循路由规则 /
# redirect_to="/login" -> 301  视图函数中的 redirect 302
# @app.route("/",methods=["GET","POST"],endpoint="index",
#            strict_slashes=True,defaults={"name":"value"},redirect_to="/login")
# @app.route("/index",methods=["GET","POST"],endpoint="index")
# def index():
#     url = url_for("index")
#     print(url) # "/index"
#     return str(url)


# 2.Flask Response
    # 1.HttpResponse
    # return "hello S14"

    # 2.render_template
    # from flask import render_template
    # return render_template #返回模板

    # 3.redirect
    # from flask import redirect
    # return redirect("/login")

    # 4.send_file
    # from flask import send_file
    # return send_file("文件路径") # 自动识别文件类型

    # 5.jsonify
    # from flask import jsonify
    # return jsonify({"name":"value"}) # 响应头中加入：Content-type:application/json


# 3.Flask Request - from flask import request
    # 1.request.form -> 存放FormData中的数据
    # 2.request.args -> 存放url中的参数
    # 3.request.json -> 请求头:Content-type:application/json
    # 4.request.data -> 存放请求体中的原始信息 b""
        # print(request.json)
        # print(request.data)
        # import json
        # data_dict = json.loads(request.data)
        # print(type(data_dict),data_dict)
        # return "123"
    # 5.request.files -> 存放FormData中的文件类型数据
        # file = request.files.get("my_file")
        # file.save(file.filename)
        # file.save("1.mp3")
    # 6.request.cookie -> 存放的Cookie数据
        # request.cookie.get("session")

# 8.Flask Session
#   Flask中的Session存放在客户端 Cookie - session
#   1.from flask import session
#   2.app.secret_key = "#$%^&*("
#   3.if session["user"] KeyError

# 5.Flask 实例化配置
# app = Flask(__name__,template_folder="",static_folder="",static_url_path="/{static_folder}")
# template_folder="", 模板存放目录 templates
# static_folder="", 静态文件存放目录 static
# static_url_path="/{static_folder}" 静态文件访问路径 默认时候 “/+static_folder”

# 6.Flask 对象配置
# from flask import jsonify
# app = Flask(__name__)
# app.config["DEBUG"] = True
# app.config["SECRET_KEY"] = "$%^&*()_"
# app.config["JSONIFY_MIMETYPE"] = "      /debaba"
# class MySet(object):
#     DEBUG = True
#     SECRET_KEY = "$%^&*()"
#     JSONIFY_MIMETYPE = "fasjdfhjkasdf/asdfasdfsadf"
#     SESSION_TYPE = "reids"
#     # SESSION_REDIS=redis.Redis()
# 通过 类 配置
# app.config.from_object(MySet)
# app.default_config
#
# @app.route("/index",methods=["GET","POST"],endpoint="index")
# def index():
#     return jsonify({"name":123})

# 7.Flask 蓝图
# 详见bp.py
# 蓝图项目目录详见代码

# 9.Flask 特殊装饰器 @app.before_request
from flask import Flask
app = Flask(__name__)

# @app.before_request 在请求进入视图函数之前
# @app.before_request
# def be1():
#     print("be1")
#     return None
#
# @app.before_request
# def be2():
#     print("be2")
#     return None

# @app.after_request 在视图函数结束之后，响应返回客户端之前
# @app.after_request
# def af1(response):
#     print("af1")
#     return response
#
# @app.after_request
# def af2(response):
#     print("af2")
#     return response
# 正常  be1 - be2 - views - af2 - af1
# 异常  be1 - af2 - af1

# @app.errorhandler(404)
# def error404(error_msg)
# @app.errorhandler(404)
# def error404(error_msg):
#     print(error_msg)
#     return f"你所访问的页面不存在404了{error_msg}"

# from flask import jsonify,redirect
# @app.errorhandler(404)
# def error404(error_msg):
#     # return jsonify({"code":834473503,"msg":"页面错误","redirect":"/index"})
#     return redirect("/index")


# 10.Flask 请求应用上下文

from flask import request
request.method # __getattr__

if __name__ == '__main__':
    app.run()
    app.__call__
    app.wsgi_app


