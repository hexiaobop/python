# -*- coding:utf-8 -*-
import threading
import time
from bs4 import BeautifulSoup
from Queue import Queue
from openurlproxy import *

class MyThread(threading.Thread):
    def __init__(self,url):
        threading.Thread.__init__(self)
        self.url = url
        self.domain = 'http://yuedu.baidu.com'


    def run(self):
        print 'open------------'
        return
        
    def findintroduce(self):
        url = self.domain+self.url
        #soup = BeautifulSoup(Open.openurl(url))
        # soup.find('span',{"class":"title-txt"})
        #<span class="title-txt">图书简介</span>
    def saveurl(self):
        fp = open(u'已访问url.txt','a+')
        for i in self.list:
            fp.write(i+'\n')
        fp.close()
            
        
