# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 17:30
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : base_page.py
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='../log/myapp.log',
                        filemode='w')

    def __init__(self, driver: WebDriver = None):
        self._driver = driver
        # self.searcher_num = searcher_num

    def find(self, by, locator):
        logging.info("find:")
        logging.info(by)
        logging.info(locator)

        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        logging.info("finds:")
        logging.info(by)
        logging.info(locator)

        return self._driver.find_elements(by, locator)

    def find_by_scroll(self, text):
        logging.info("find_by_scroll")
        logging.info(text)

        return self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                         'new UiScrollable(new UiSelector()'
                                         '.scrollable(true).instance(0))'
                                         '.scrollIntoView(new UiSelector()'
                                         '.text("%s").instance(0));' % text)

    def get_toast_text(self):
        logging.info("get toast:")
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result
