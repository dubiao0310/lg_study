
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 下午3:13
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : ｔｅｓｔ.py
import pytest


# @pytest.fixture()
# def db():
#     print("test前")
#     yield
#     print("test后")



# @pytest.mark.usefixtures("fun_scope")
def test_fixture():
    assert 0 == 1
    # print("test")

# @pytest.mark.usefixtures("fun_scope")
def test_fixture2():
    print("test2")


# @pytest.mark.usefixtures("fun_scope")
def test_fixture3():
    print("test3")


# @pytest.mark.usefixtures("fun_scope")
def test_fixture4():
    print("test4")


# @pytest.mark.usefixtures("fun_scope")
def test_fixture5():
    print("test5")


# @pytest.mark.usefixtures("fun_scope")
def test_fixture6():
    print("test6")

"""
insert into employee(name ,sex,age,hire_date,post,salary,office,depart_id) values
('egon','male',18,'20170301','teacher',7300.33,401,1), #以下是教学部
('alex','male',78,'20150302','teacher',1000000.31,401,1),
('wupeiqi','male',81,'20130305','teacher',8300,401,1),
('yuanhao','male',73,'20140701','teacher',3500,401,1),
('liwenzhou','male',28,'20121101','teacher',2100,401,1),
('jingliyang','female',18,'20110211','teacher',9000,401,1),
('jinxin','male',18,'19000301','teacher',30000,401,1),
('xiaomage','male',48,'20101111','teacher',10000,401,1),

('aa','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
('bb','female',38,'20101101','sale',2000.35,402,2),
('cc','female',18,'20110312','sale',1000.37,402,2),
('dd','female',18,'20160513','sale',3000.29,402,2),
('ee','female',28,'20170127','sale',4000.33,402,2),

('ff','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
('gg','male',18,'19970312','operation',20000,403,3),
('hh','female',18,'20130311','operation',19000,403,3),
('ii','male',18,'20150411','operation',18000,403,3),
('jj','female',18,'20140512','operation',17000,403,3)
;
"""