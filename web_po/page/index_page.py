# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 下午2:22
# @Author  : biao.du
# @Email   : MrDu_biao@163.com
# @File    : index_page.py
from selenium.webdriver.common.by import By

from web_po.page.add_menmbers import AddMembers
from web_po.page.base import Base


class IndexPage(Base):
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_members(self):
        # By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)"
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMembers(self.driver)






if __name__ == '__main__':
    index = IndexPage()
    index.goto_add_members()