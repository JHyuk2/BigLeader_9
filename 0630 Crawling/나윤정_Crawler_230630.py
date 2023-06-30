# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:40:47 2023

@author: nyj
"""

#bigleader_crawling

from selenium import webdriver
import chromedriver_autoinstaller as ca
import time, os, sys
from selenium.webdriver.common.by import By

def ts(x):
    time.sleep(x)
    
#웹사이트 오픈
driver= webdriver.Chrome(ca.install())
ts(2); driver.get('http://www.riss.kr/')  #혁명적인 방법이다...! ;사용시 한줄에 여러줄의 코드를 쓸수 있다

#웹사이트 접속후 팝업창이 있으면 모두 제거
main= driver.window_handles
for handle in main:
    if handle !=main[0]:
        driver.switch_to.window(handle)
        driver.close()
driver.switch_to.window(driver.window_handles[0])

ts(2); driver.maximize_window()

#검색창에 검색어 넣기
ts(2); driver.find_element(By.ID, 'query').send_keys('여름여행'+'\n')
ts(2); driver.find_element(By.LINK_TEXT, '학위논문').click()

ts(5); driver.close()