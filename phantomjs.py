# -*- coding: utf-8 -*-
import sys

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
url = "https://passport.baidu.com/v2/?login"
driver = webdriver.PhantomJS()
driver.get(url)  #//*[@id="TANGRAM__PSP_3__userName"] //*[@id="TANGRAM__PSP_3__password"]  //*[@id="TANGRAM__PSP_3__submit"]
name = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]').send_keys(u"")

passw = driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__password"]').send_keys("")



time.sleep(2)

driver.get_screenshot_as_file('show1.png')

driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__submit"]').submit()

try:
    dr=WebDriverWait(driver,5)
    dr.until(lambda the_driver:the_driver.find_element_by_xpath('//*[@id="displayUsername"]').is_displayed())
except:
    print u'登录失败'
    sys.exit(0)
    
driver.get_screenshot_as_file('show.png')


driver.get_screenshot_as_file('show.png')

