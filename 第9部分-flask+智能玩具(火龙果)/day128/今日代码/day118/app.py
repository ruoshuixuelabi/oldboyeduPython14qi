from flask import Flask,request,render_template,send_file,jsonify
from uuid import uuid4
from baidu_ai import audio2text
from baidu_ai import my_nlp
from baidu_ai import text2audio

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("web.html")
    else:
        print(request.files)
        return "123"
    
import os
@app.route("/toy_uploader",methods=["GET","POST"])
def toy_uploader():
    print(request.files)
    file_path = os.path.join("audios",f"{uuid4()}.wav")
    request.files["record"].save(file_path)
    Q = audio2text(file_path)
    print(Q)
    A = my_nlp(Q)
    filename = text2audio(A)
    print(filename)
    return jsonify({"filename":filename,"A":A})

@app.route("/get_audio/<filename>",methods=["GET","POST"])
def get_audio(filename):
    new_file = os.path.join("audios",filename)
    print(new_file)
    return send_file(new_file)


if __name__ == '__main__':
    app.run("0.0.0.0",5000,debug=True)