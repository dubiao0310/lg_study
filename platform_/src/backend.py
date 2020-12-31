# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 下午9:46
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : backend.py

import os
import sys
from flask import Flask, request, redirect
from flask_restful import Api, Resource

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from platform_.src.models import *


api = Api(app)


@app.route("/", methods=["GET"])
def index():
    return redirect("/login")


@app.route("/login", methods=["GET"])
def login():
    return "login"


@app.route("/register", methods=["GET", "POST"])
def register():
    data = request.json
    user = User(name=data["name"], password=data["password"])

    db.session.add(user)
    db.session.commit()
    return ""



class TestCaseServer(Resource):

    def get(self):
        case = TestCase.query.all()[0]
        print(case.id)
        return case

    def post(self):
        data = request.json
        case = TestCase(name=data["name"], description=data["des"], steps=data["steps"])
        db.session.add(case)
        db.session.commit()



class TaskServer(Resource):

    def get(self):
        task = Task.query.filter(Task.id==3).all()
        print(task[0].cases)

    def post(self):
        data = request.json
        case_list = data["case_list"]

        case = TestCase.query.filter(TestCase.id.in_(case_list)).all()
        task_id = data["id"]
        task = Task(id=task_id)
        task.cases = case

        db.session.add(task)
        db.session.commit()


class ReportServer(Resource):

    def get(self):
        report = Report.query.filter(Report.id==1).first()
        print(report.report_task)
        return ""

    def post(self):
        data = request.json
        report = Report(id=data["id"], pass_case_num=data["pass_num"],
                        fail_case_num=data["fail_num"], task_id=data["task_id"])

        db.session.add(report)
        db.session.commit()



api.add_resource(TestCaseServer, "/testcase")
api.add_resource(TaskServer, "/taskserver")
api.add_resource(ReportServer, "/reportserver")


if __name__ == '__main__':
    app.run(debug=True)

