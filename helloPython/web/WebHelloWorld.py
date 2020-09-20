from flask import Flask,request  # 引入Flask模块

app = Flask(__name__)  # 创建一个应用

@app.route('/app')
def index():  # 定义根目录处理器
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()  # 启动服务

@app.route('/hello')
def hello():
    return '<h1>Hello</h1>'
