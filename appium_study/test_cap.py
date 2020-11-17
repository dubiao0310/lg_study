# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 16:21
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_cap.py
from appium import webdriver

# com.xueqiu.android/.view.WelcomeActivityAlias
desire_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True,  # 解决更新弹窗、登陆等,
    "dontStopAppOnReset": "true", # 首次启动时，不重停止app
    "skipDeviceInitialization": "true", # 跳过安装，设置权限等操作
    "unicodeKeyBoard": "true"  # 可以输入中文
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
driver.implicitly_wait(10)

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
driver.back() # 返回到上一个页面
driver.back() # 返回到上一个页面
driver.quit()

