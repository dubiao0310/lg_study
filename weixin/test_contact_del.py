# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 14:47
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_del_contact.py
toast

    # def test_del_contact(self):
    #     name = "aa"
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
    #     self.driver.find_element(MobileBy.ID, "hk9").click()
    #     # id 是动态的
    #     # self.driver.find_element(MobileBy.XPATH,
    #     #                          "//android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView").click()
    #     self.driver.find_element(MobileBy.ID, "g75").send_keys(name)
    #     WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located, (MobileBy.XPATH, "//*[@text='联系人']"))
    #
    #     elements = self.driver.find_elements(MobileBy.ID, "ddw")
    #     if len(elements) >= 1:
    #         elements[0].click()
    #
    #     self.driver.find_element(MobileBy.ID, "hjz").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
    #     # 滚动查找
    #     # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
    #     #                          'new UiScrollable(new UiSelector()'
    #     #                          '.scrollable(true).instance(0))'
    #     #                          '.scrollIntoView(new UiSelector()'
    #     #                          '.text("删除成员").instance(0));').click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='删除成员']").click()
    #     self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
    #
    #     WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located, (MobileBy.XPATH, "//*[@text='联系人']"))
    #     elements2 = self.driver.find_elements(MobileBy.ID, "ddw")
    #
    #     assert len(elements) == len(elements2) -1


