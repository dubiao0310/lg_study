# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 下午4:26
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_allure_story.py
import allure


# @allure.feature("登录模块")
# class TestLogin:
#     @allure.severity(allure.severity_level.NORMAL)
#     @allure.story("登录成功")
#     def test_login_success(self):
#         print("登录成功")
#
#     @allure.story("登录失败")
#     def test_login_fail(self):
#         print("登录失败")
#
#     @allure.severity(allure.severity_level.NORMAL)
#     @allure.story("用户名缺少")
#     def test_login_fail_1(self):
#         print("用户名缺少")
#
#     @allure.story("密码缺失")
#     def test_login_failure(self):
#         with allure.step("输入用户名"):
#             print("输入用户名")
#
#         with allure.step("点击登录"):
#             print("点击登录")
#
#         with allure.step("点击登录之后失败"):
#             print("点击登录之后失败")
#
#
# @allure.link("https://www.baidu.com/", name="测试用例名称")  # 链接测试用例　name对链接命名
# def test_with_link():
#     print("这是一条加了链接的测试")
#
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.testcase("https://www.baidu.com/", name="测试用例名称")
# def test_testcase_link():
#     print("链接到测试用例管理")
#
# @allure.issue("bug的id", "bug描述信息")
# def test_issue_link():
#     print("链接bug地址")


def test_attach_text():
    allure.attach("这是一个纯文本信息", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一段html代码块</body>", "html代码块", attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("/home/ubuntu/Desktop/1.png", name="这是一个图片", attachment_type=allure.attachment_type.PNG)