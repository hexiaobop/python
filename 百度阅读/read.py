# -*-coding:utf-8 -*-
import re
import time
from Queue import Queue
from openurlproxy import *

class BaiDuReading():
    def __init__(self,url):
        self.url = url
        self.queue = Queue()
        self.flag = True
        self.bloomfilter = BloomFilter(capacity=10000, error_rate=0.001)
        self.openscanurl()
        self.domain = 'http://yuedu.baidu.com'


    def openscanurl(self):
        fp = open(u'已访问url.txt','r')
        scanlist = fp.readlines()
        for i in scanlist:
            self.bloomfilter.add(i)
        fp.close()
        
    def everypageurl(self):
        s=u'下一页'
        print repr(s.encode('gb2312'))
        #<a href="/book/list/0?od=1&show=0&pn=20" class="next">下一页&gt;</a>
        #print list.group(1)
        #print len(Open().openurl(self.url))
        #div class="book " data-track="0"
        #list =re.search(r'<a href="/book/list/0\?od=1&show=0&pn=([0-9]{1,9})" class="next">'+s.encode('gb2312')+'&gt;</a>',Open().openurl(self.url),re.S)
        
        while(self.flag):
            try:
                time.sleep(0.5)
                
                soup = Open.buildsoup(Open.openurl(self.url))
                lis = soup.find_all('a',{"class":"next"})    #下一页
                print lis
                li = soup.find_all('div',{"class":"book","data-track":True}) #书籍
                if len(li)<1:
                    
                    try:
                        print u'！！！！！！！！！！！ip已经被封：使用代理！！！！！！'
                        soup = Open.useproxy(Open.openurl(self.url))
                        lis = soup.find_all('a',{"class":"next"})
                        li = soup.find_all('div',{"class":"book","data-track":True})
                
                
                    except Exception,e:
                        print e
                        self.noteerroe()
                else:
                    
                    pass
                    
                self.joinqueue(li)
                if len(lis)<1:
                    self.flag = False
                    print 'no next----------------------------'
                    pass

                else:
                    print len(lis)
                    self.url = self.domain+lis[0]['href']
            except Exception,e:
                print e
            
            
    def joinqueue(self,list):     # 加入队列
        print self.url
        for i in list:
            try:
                name = i('a')[1].span.get_text()
                url = i('a')[1]['href']                
                self.queue.put(url)
                author = i.p.span.get_text()
                fp = open(u'百度阅读.txt','a+')
                fp.write(name.encode('utf-8')+'\n')
                fp.close()
                #print name.encode('utf-8'),url,author,self.queue.qsize()
            except Exception,e:              
                print e
                self.noteerroe()
    
    def noteerroe(self):
        print '--------------error-------------'
        fp =open(u'断点.txt','w')
        fp.write(self.url+'\n')
        fp.close()
            
        

        
        
        
