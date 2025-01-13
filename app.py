from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from matplotlib import pyplot as plt


from UserMangager import UserManager

# pip install flask-cors

app = Flask(__name__)
CORS(app)

@app.route("/login",methods=['POST'])
def login():
    data = request.get_json()
    um = UserManager()
    flag = um.search_user_info(data["username"],data["password"])
    if flag == 2:
        return jsonify({"msg":"用户名或密码错误","code":500})
    if flag == 1:
        return jsonify({"msg":"请检查数据库问题","code":500})
    return jsonify({"msg":"success","code":200})


@app.route("/register",methods=['POST'])
def register():
    data = request.get_json()
    um = UserManager()
    flag = um.add_user_info(data["username"],data["password"])
    if flag == 1:
        return jsonify({"msg":"请检查数据库问题","code":500})
    return jsonify({"msg":"success","code":200})


if __name__ == '__main__':
    app.run()
