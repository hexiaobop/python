from pytesser import *
from PIL import Image
from PIL import ImageEnhance
from selenium import webdriver
from selenium.webdriver import ActionChains
import sys 
image = Image.open('B.jpg')  # Open image object using PIL
print image_to_string(image)     # Run tesseract.exe on image


driver = webdriver.Chrome()

driver.get("http://jwxt.swpu.edu.cn/logout.do")

username ='/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input'
password = '/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input'
va  = '/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[2]/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input'
image = '//*[@id="vchart"]'


action = ActionChains(driver)
imagesave = driver.find_element_by_xpath(image)
action.context_click(imagesave).perform()



