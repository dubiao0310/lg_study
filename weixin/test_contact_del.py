# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 14:47
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_del_contact.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDelContact:
    def setup(self):
        caps = {
            "platformName": "Android",
            "deviceName": "P7C0218119005759",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.WwMainActivity",
            "noReset": "True",
            "skipDeviceInitialization": "true",  # 跳过安装，设置权限等操作
            "unicodeKeyBoard": "true",  # 可以输入中文
            "resetKeyBoard": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_contact(self):
        # logging.basicConfig(level=logging.INFO)
        name = "hogwarts_00003"
        gender = "男"
        phonenum = "13812121214"
        # 点击【通讯录】

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击【添加成员】

        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 点击【手动输入添加】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/..//*[@text='男']").click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']").click()
        # 获取toast
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert result == "添加成功"

    def test_del_contact(self):
        name = "aa"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "hk9").click()
        # id 是动态的
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView").click()
        self.driver.find_element(MobileBy.ID, "g75").send_keys(name)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located,
                                            (MobileBy.XPATH, "//*[@text='联系人']"))

        elements = self.driver.find_elements(MobileBy.ID, "ddw")
        if len(elements) >= 1:
            elements[0].click()

        self.driver.find_element(MobileBy.ID, "hjz").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        # 滚动查找
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located,
                                            (MobileBy.XPATH, "//*[@text='联系人']"))
        elements2 = self.driver.find_elements(MobileBy.ID, "ddw")

        assert len(elements) == len(elements2) - 1
