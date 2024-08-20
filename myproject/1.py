from flask import Flask , request  #导入Flask类
#使用Flask类创建一个app对象
app = Flask(__name__)   #注意这里前后都是双在下划线，代表当前1.py这个模块

#创建一个路由和视图函数的映射
@app.route('/')    #设置网页的目录也就是 path 
def hello_world():
	return "Hello niumo!"   #返回Hello World!,也就是在网页上显示Hello World!
#修改host
#主要作用：让其他电脑能访问我电脑上的flask项目
#修改host:如果5000端口被其他程序占用了，可以通过修改port来监听端口号


@app.route("/profile")
def profile():
      return "我是大帅哥"

#带参数的url
@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
      return "您访问的博客是：%s"% blog_id

#查询字符串的方式传参
#/book/list:会返回第一页的数据
#/book/list?page=2:会返回第2页的数据
@app.route('/book/list')
def book_list():
      #arguments:参数
      #request.args:类字典类型
      page=request.args.get("page",default=1,type=int)
      return f"您获取的是第{page}的图书列表"




if __name__ == "__main__":
    app.run(debug=True)


#url:http[端口：80]/https[443]://www.qq.com: