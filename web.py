#0301 开始试着建站
from flask import Flask

app = Flask(__name__)

#创建了网址/show/info 和函数index的关系
#以后用户在浏览器访问/show/info，网站自动执行index
@app.route("/show/info")
def index():
    return "中国电信"

if __name__ == "__main__":
    app.run()