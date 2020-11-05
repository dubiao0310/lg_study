# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 下午9:44
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : test_weixin.py
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWx:
    def setup(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)

    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")  # 要复用浏览器页面链接
        self.driver.find_element_by_id("menu_contacts").click()

    def test_cookie(self):
        # 获取cookies
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': 'qq.com', 'expiry': 1604498500, 'secure': False, 'path': '/', 'httpOnly': False, 'value': '1',
             'name': '_gat'}, {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False,
                               'value': '1688853132845352', 'name': 'wwrtx.vid'},
            {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '1688853132845352', 'name': 'wxpay.vid'},
            {'domain': 'qq.com', 'expiry': 2147385600, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '4267064704', 'name': 'pgv_pvid'},
            {'domain': 'qq.com', 'expiry': 2147385600, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '7681306624', 'name': 'pgv_pvi'},
            {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '1970325106175366', 'name': 'wxpay.corpid'},
            {'domain': 'qq.com', 'expiry': 1604584840, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': 'GA1.2.1433348177.1604495577', 'name': '_gid'},
            {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True,
             'value': '0FHIacm1K4R2UG2g_AuC4p5Gk2A3dHIxyiMXmU7GvcNfX65AuFq6aUW7gU3RQRHZ', 'name': 'wwrtx.sid'},
            {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False, 'value': 'a6472120',
             'name': 'wwrtx.d2st'},
            {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False, 'value': '1604497823',
             'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d'},
            {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True,
             'value': '16884221112947399', 'name': 'wwrtx.refid'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1607090442.365818, 'secure': False, 'path': '/',
             'httpOnly': False, 'value': 'en', 'name': 'wwrtx.i18n_lan'},
            {'domain': 'qq.com', 'expiry': 1667570440, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': 'GA1.2.489605813.1604495577', 'name': '_ga'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604527093.54751, 'secure': False, 'path': '/', 'httpOnly': True,
             'value': '7jm1ago', 'name': 'ww_rtkey'},
            {'domain': 'qq.com', 'expiry': 1890183213, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '92b0796039e0d93d', 'name': 'tvfe_boss_uuid'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1636031557.547716, 'secure': False, 'path': '/',
             'httpOnly': False, 'value': '0', 'name': 'wwrtx.c_gdpr'},
            {'domain': 'qq.com', 'expiry': 1604539668, 'secure': True, 'path': '/', 'httpOnly': False,
             'value': 'gSd4jw73cVLLMBMmwOyb4Lre', 'name': 'webwx_data_ticket'},
            {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True,
             'value': 'mn0Zev8Bt5WgVg714hHQy_uC6llVlJIgAyuSkyeDvkEQp5HcCOZbzWHWx4SQU8LWKCY5nKVANLOPZeDJVrXjKGf3n7vdpTqU0bmuPWQXbTlM3AEMFMV6DJ7erMIXJyo41R6zbeIVVlxhsfJgzinolAPJat0T6LgT0bud1XJI_yODZxglQ3ZCbx16sc0B2i0Arg5qShrHKmlE5V9tnxjORPdk09lxtljRtt9EnUXT-MtMRXe_q4P6lB7f8Cc8pwhdlC9qdXO1hAqGxqdKKSYClA',
             'name': 'wwrtx.vst'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1636033823, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '1604495576,1604497823', 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d'},
            {'domain': 'qq.com', 'expiry': 1919143826.682199, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '1_442301500', 'name': 'pac_uid'},
            {'domain': 'qq.com', 'expiry': 2147385600, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '442301500', 'name': 'o_cookie'},
            {'domain': 'qq.com', 'expiry': 1894271993, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '1_16f9e7d0eba_8ef41', 'name': 'mobileUV'},
            {'domain': 'qq.com', 'expiry': 2147483647.412737, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': 'd5792a0e445a741bb0788a8fdaf65645a93c2b4bd9add7a5b7e290ce95155567', 'name': 'ptcz'},
            {'domain': 'qq.com', 'expiry': 2147483647.412682, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': 'sER0Ba92Mp', 'name': 'RK'},
            {'domain': 'qq.com', 'expiry': 1605790325, 'secure': False, 'path': '/', 'httpOnly': False,
             'value': '442301500', 'name': 'ptui_loginuin'},
            {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True, 'value': '1',
             'name': 'wwrtx.ltype'},
            {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True, 'value': 'direct',
             'name': 'wwrtx.ref'}]
        # expiry 不能是小数，　要删掉
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.refresh()

    def test_case(self):
        # shelve模块，　python自带的对象持久化存储
        # db = shelve.open("cookies")
        # db["cookie"] = [
        #     {'domain': 'qq.com', 'expiry': 1604498500, 'secure': False, 'path': '/', 'httpOnly': False, 'value': '1',
        #      'name': '_gat'}, {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False,
        #                        'value': '1688853132845352', 'name': 'wwrtx.vid'},
        #     {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '1688853132845352', 'name': 'wxpay.vid'},
        #     {'domain': 'qq.com', 'expiry': 2147385600, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '4267064704', 'name': 'pgv_pvid'},
        #     {'domain': 'qq.com', 'expiry': 2147385600, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '7681306624', 'name': 'pgv_pvi'},
        #     {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '1970325106175366', 'name': 'wxpay.corpid'},
        #     {'domain': 'qq.com', 'expiry': 1604584840, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': 'GA1.2.1433348177.1604495577', 'name': '_gid'},
        #     {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True,
        #      'value': '0FHIacm1K4R2UG2g_AuC4p5Gk2A3dHIxyiMXmU7GvcNfX65AuFq6aUW7gU3RQRHZ', 'name': 'wwrtx.sid'},
        #     {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False, 'value': 'a6472120',
        #      'name': 'wwrtx.d2st'},
        #     {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': False, 'value': '1604497823',
        #      'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d'},
        #     {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True,
        #      'value': '16884221112947399', 'name': 'wwrtx.refid'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1607090442.365818, 'secure': False, 'path': '/',
        #      'httpOnly': False, 'value': 'en', 'name': 'wwrtx.i18n_lan'},
        #     {'domain': 'qq.com', 'expiry': 1667570440, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': 'GA1.2.489605813.1604495577', 'name': '_ga'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1604527093.54751, 'secure': False, 'path': '/', 'httpOnly': True,
        #      'value': '7jm1ago', 'name': 'ww_rtkey'},
        #     {'domain': 'qq.com', 'expiry': 1890183213, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '92b0796039e0d93d', 'name': 'tvfe_boss_uuid'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1636031557.547716, 'secure': False, 'path': '/',
        #      'httpOnly': False, 'value': '0', 'name': 'wwrtx.c_gdpr'},
        #     {'domain': 'qq.com', 'expiry': 1604539668, 'secure': True, 'path': '/', 'httpOnly': False,
        #      'value': 'gSd4jw73cVLLMBMmwOyb4Lre', 'name': 'webwx_data_ticket'},
        #     {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True,
        #      'value': 'mn0Zev8Bt5WgVg714hHQy_uC6llVlJIgAyuSkyeDvkEQp5HcCOZbzWHWx4SQU8LWKCY5nKVANLOPZeDJVrXjKGf3n7vdpTqU0bmuPWQXbTlM3AEMFMV6DJ7erMIXJyo41R6zbeIVVlxhsfJgzinolAPJat0T6LgT0bud1XJI_yODZxglQ3ZCbx16sc0B2i0Arg5qShrHKmlE5V9tnxjORPdk09lxtljRtt9EnUXT-MtMRXe_q4P6lB7f8Cc8pwhdlC9qdXO1hAqGxqdKKSYClA',
        #      'name': 'wwrtx.vst'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1636033823, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '1604495576,1604497823', 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d'},
        #     {'domain': 'qq.com', 'expiry': 1919143826.682199, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '1_442301500', 'name': 'pac_uid'},
        #     {'domain': 'qq.com', 'expiry': 2147385600, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '442301500', 'name': 'o_cookie'},
        #     {'domain': 'qq.com', 'expiry': 1894271993, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '1_16f9e7d0eba_8ef41', 'name': 'mobileUV'},
        #     {'domain': 'qq.com', 'expiry': 2147483647.412737, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': 'd5792a0e445a741bb0788a8fdaf65645a93c2b4bd9add7a5b7e290ce95155567', 'name': 'ptcz'},
        #     {'domain': 'qq.com', 'expiry': 2147483647.412682, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': 'sER0Ba92Mp', 'name': 'RK'},
        #     {'domain': 'qq.com', 'expiry': 1605790325, 'secure': False, 'path': '/', 'httpOnly': False,
        #      'value': '442301500', 'name': 'ptui_loginuin'},
        #     {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True, 'value': '1',
        #      'name': 'wwrtx.ltype'},
        #     {'domain': 'work.weixin.qq.com', 'secure': False, 'path': '/', 'httpOnly': True, 'value': 'direct',
        #      'name': 'wwrtx.ref'}]
        # db.close()

        db = shelve.open("cookies")
        cookies = db["cookie"]
        db.close()

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            # expiry 不能是小数，　要删掉
            if 'expiry' in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 刷新当前页，获取登录状态
        self.driver.refresh()

        # 点击【导入联系人】
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
         # 上传文件，选择文件的完整路径上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
        "/Users/juanxu/Downloads/mydata.xlsx")
          # 断言上传文件名，与实际文件名一致
        result = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "mydata.xlsx" == result
        sleep(5)




