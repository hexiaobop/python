# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
import sys
import time

class Phone:


    def __init__(self,url):
        self.url = "http://item.jd.com/1554893.html"
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        
        self.actions = ActionChains(self.driver)

    def openurl(self):

        
        
        price = self.driver.find_element_by_xpath('//*[@id="jd-price"]')              #价格
        time.sleep(3)
        print price.text

        cs = self.driver.find_element_by_xpath('//*[@id="detail-tab-param"]')           #点击参数
        self.actions.move_to_element(cs)
        self.actions.click(cs).perform()
        time.sleep(2)
        self.driver.get_screenshot_as_file('show5.png')
        detail = self.driver.find_element_by_xpath('//*[@id="product-detail-2"]/table/tbody')  #参数
        canshu = detail.text
        commentnumber = self.driver.find_element_by_xpath(' //*[@id="detail-tab-comm"]')       #点击评论
        self.actions.click(commentnumber).perform()
        time.sleep(1)        
        comments = self.driver.find_element_by_xpath('//*[@id="comments-list"]/div[1]/div[1]/ul')   #评论数
        comment = comments.text
        fp = open('parameters.txt','w+')
        if len(fp.readlines())>20:
            fp.close()
            pass
        else:
            
            fp.write(u"价格：".encode('utf8')+price.text.encode('utf8')+'\n'+comment.encode('utf8')+'\n'+canshu.encode('utf8'))
            fp.close()
        print type(detail.text)

    def commentdata(self):
        self.driver.get_screenshot_as_file('show9.png')
        commentnumber = self.driver.find_element_by_xpath(' //*[@id="detail-tab-comm"]')       #点击评论
        self.actions.move_to_element(commentnumber)
        self.actions.click(commentnumber).perform()
        time.sleep(1)
        
        zhongpin = self.driver.find_element_by_xpath('//*[@id="comments-list"]/div[1]/div[1]/ul/li[3]')  #中评
        self.actions.click(zhongpin).perform()
        time.sleep(1)
        self.driver.get_screenshot_as_file('zhongpin.png')
        #print self.driver.find_element_by_xpath('//*[@id="comment-2"]/div[2]').text
        
        #print self.driver.find_element_by_xpath('//*[@id="comment-2"]/div[3]/div/div/a[2]').text
       
           
  
         
        a = True

        nextt = None
        #nex = self.driver.find_element_by_link_text('下一页')
        while a:
            
            
            try:
                nextt = self.driver.find_element_by_link_text('下一页')
                print "---------------有下一页啊"
                a=True
            except:
                print "------------a为false-----------"
                a=false
            
            zhong = self.driver.find_element_by_xpath('//*[@id="comment-2"]/div[2]')
            fp = open('zhongpin.txt','a')
            print zhong.text
            fp.write(zhong.text.encode('utf-8'))
            fp.close()
            #next =self.driver.find_element_by_xpath('//*[@id="comment-2"]/div[3]/div/div')

            #print next.text
            #nex = self.driver.find_element_by_xpath('//*[@id="comment-2"]/div[3]/div/div/a[2]')
            
            #self.actions.focus(nex)#comment-2 > div.com-table-footer > div > div > a.ui-pager-next
            #self.actions.click(nex).perform()
            #print self.driver.page_source
            #nex = self.driver.find_element_by_link_text('下一页')
            #print self.driver.page_source
            #nextt1 = self.driver.find_element_by_link_text('下一页')
            
            #self.actions.click(self.driver.find_element_by_link_text('下一页'))
            
            action2 = ActionChains(self.driver)
            action2.click(nextt)
            action2.perform()
            #self.actions.click(nex)
            #self.actions.perform()
            time.sleep(1)
            
            
            #self.actions.move_to_element(nex).perform()
            #self.actions.click_and_hold(nex).perform()
            #self.actions.release(nex).perform()
            self.driver.get_screenshot_as_file('show6.png')
            #print self.driver.page_source
            print "走向下一页"
          
        self.driver.close
            #comment = self.driver.find_element_by_xpath('//*[@id="detail-tab-comm"]')
            #self.driver.close      		
p = Phone('http://item.jd.com/1554893.html')
#p.openurl()
p.commentdata()
