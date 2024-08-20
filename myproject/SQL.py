from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
import os
from flask import Flask
app = Flask(__name__)

db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app

# ...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path,'/home/ubuntu/py_file/Flask/database_folder''data.db')

class User(db.Model):  # 表名将会是 user（自动生成，小写处理）,模型类要声明继承 db.Model
    id = db.Column(db.Integer, primary_key=True)  # 主键,每一个类属性（字段）要实例化 db.Column，传入的参数为字段的类型
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份