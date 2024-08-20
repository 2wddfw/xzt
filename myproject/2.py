#模板对象访问属性
from flask import Flask, render_template
from datetime import datetime
def datetime_format(value,format="%Y年%m月%d日 %H:%M"):
    return value.strftime(format)



app = Flask(__name__)   # 导入并创建Flask应用
app.add_template_filter(datetime_format,"dformat")

class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email



@app.route('/')
def you():
    user=User(username= "知了" , email="xx@qq.com")
    return render_template("3.html",user=user)



#过滤器的使用
@app.route("/filter")
def niuben():
    user=User(username="知了",email="xx@qq.com")
    mytime=datetime.now()
    return render_template("filter.html",user=user,mytime=mytime)#把user变量传给filter.html\


@app.route("/eng")
def zhangsan():
    user=User(username="知了",email="xx@qq.com")
    person={"username":"张三",
            "email":"zhangsan@qq.com"}
    return render_template("3.html",user=user,person=person)



@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
    return render_template("you.html",blog_id=blog_id,username="知了")

#if 语句和for语句
@app.route("/control")
def control_statement():
    age=18
    books = [{
        "name":"三国演义",
        "author":"罗贯中",
    },{
        "name":"水浒传",
        "author":"施耐庵"
    }]
    return render_template("control.html",age=age,books=books)


#父模板继承机制，使用extend继承父模板，使用block替换父模板中标有block的内容（在副模版的基础上插入内容）
@app.route("/child1")
def child1():
    return render_template("child.html")

#ul
@app.route("/child2")
def child2():
    return render_template("child2.html")


#加载静态文件

@app.route("/static")
def static_demo():
    return render_template("static.html")

if __name__ == "__main__":
    # 运行应用，调试模式开启
    app.run(debug=True)
