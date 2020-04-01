# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : Hogwarts_11
@File    : search.py
@Time    : 2020-03-30  10:07:23
@Author  : indeyo_lin
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from test_appium.page.base_page import BasePage


class SearchPage(BasePage):
    # 定位符提取出来方便以后管理多版本、多平台
    _search_locator = (MobileBy.ID, "search_input_text")
    _stock_locator = (MobileBy.ID, "name")
    _add_locator = (By.XPATH, '//*[@text="加自选"]')
    _followed_locator = (By.ID, "followed_btn")

    def search(self, key: str):
        self.find(*self._search_locator).send_keys(key)
        # 奇怪，这里少了一步，业务逻辑改变了？？
        # self.find(*self._stock_locator).click()
        return self

    def get_price(self, key: str) -> float:
        # todo:获取股票价格参数化
        price_element = (By.XPATH, "//*[@text='%s']/../../..//*[contains(@resource-id, 'current_price')]" % key)
        return float(self.find(*price_element).text)

    def add_stock(self):
        self.find(self._add_locator).click()
        return self

    def get_msg(self):
        return self.find(self._followed_locator).text