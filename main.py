# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:39:00 2022

@author: Takodachi
"""

import time
import requests

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#自動打開Chrome
driver = webdriver.Chrome()



#抓取網址
driver.get(url="https://www.decathlon.tw/zh/series")

#空白處點一下 消除AD
ActionChains(driver).move_by_offset(200, 100).click().perform()




    
    

