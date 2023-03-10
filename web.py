# 0301 开始试着建站
# 再测试一下提交
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


# 创建了网址/show/info 和函数index的关系
# 以后用户在浏览器访问/show/info，网站自动执行index
@app.route("/show/info")
def index():
    # return "中国<span style= 'color:red;'>电信</span>"
    # Flask 内部会自动打开这个index.html文件，读取内容
    # 默认去当前项目目录下的template文件夹下找
    # return render_template("PycharmQuick.html")
    return render_template("TestHtml.html")


@app.route("/get/news")
def getNews():
    return render_template("getNews.html")


@app.route("/comic/list")  # 漫画列表
def comic_list():
    return render_template("ComicR.html")


@app.route("/usr/list")  # 用户列表
def usr_list():
    return render_template("usrList.html")


@app.route("/usr/register")  # 用户列表
def usr_register():
    return render_template("usrRegister.html")


if __name__ == "__main__":
    app.run()
