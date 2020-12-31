# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 下午10:01
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : models.py

import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

conf = yaml.safe_load(open("./mysql_config.yaml"))
user = conf["user"]
password = conf["password"]
url = conf["url"]
port = conf["port"]
db = conf["db"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{user}:{password}@{url}:{port}/{db}?charset=utf8".\
    format(user=user, password=password, url=url, port=port, db=db)
print("mysql+pymysql://{user}:{password}@{url}:{port}/{db}?charset=utf8".\
    format(user=user, password=password, url=url, port=port, db=db))
# 解决警告：FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
#   'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app, use_native_unicode='utf8')


class User(db.Model):
    """
    用户表
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)


# 测试用例与任务关联表
case_task = db.Table("case_task",
                     db.Column("case_id", db.Integer, db.ForeignKey("test_case.id")),
                     db.Column("task_id", db.Integer, db.ForeignKey("task.id"))
                     )


class TestCase(db.Model):
    """
    测试用例表
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)
    steps = db.Column(db.String(120), nullable=True)


class Task(db.Model):
    '''
    任务表
    '''
    id = db.Column(db.Integer, primary_key=True)
    cases = db.relationship("TestCase", secondary=case_task,
                                backref="tasks")


class Report(db.Model):
    """
    报告表
    """
    __tablename__ = "report"
    id = db.Column(db.Integer, primary_key=True)
    pass_case_num = db.Column(db.Integer, nullable=False)
    fail_case_num = db.Column(db.Integer, nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey(Task.id))
    report_task = db.relationship("Task", backref="task_reports")





if __name__ == '__main__':
    db.create_all()