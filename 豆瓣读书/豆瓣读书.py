
#coding=utf-8
from  bs4 import BeautifulSoup
import urllib2
import urllib
import pymongo
import time

class Douban(object):

   def __init__(self):
      
      
      self.queen=[]
      self.connection=pymongo.MongoClient('127.0.0.1',27017)
      self.db=self.connection.doubantext
      self.collection=self.db.text
      

   def openindex(self,url):
      count = 3
      i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
      req = urllib2.Request(url,headers=i_headers)
      while(count>0):

         try:
            response = urllib2.urlopen(req)
            print response.getcode()
            break
         except Exception,e:
            print e
            print url
            count=count-1
      
         
      
      return response

   def getindexurl(self,response):                #所有标签的url
      soup = BeautifulSoup(response)
      #print soup
      list = soup.findAll("div",{"id":None,"class":""})
      print type(list)
      #print list[1:]
      #print len(list[1:])      
      for i in list[1:]:              
         print i.h2.get_text()+'\n',self.handlelist(i.tbody('a'))
         

   def handlelist(self,list):                	#处理所有标签url列表
      for i in list:
         
         print i['href'],i.get_text()
         self.queen.append(i['href'])
         

   def handlethis(self,response):              #第一页的数据列表
      
      soup = BeautifulSoup(response)
      
      list = soup.findAll('div',{"class":"mod-list book-list","id":"book"})
      #print list[0]('dd')     
      self.handlebookdiv(list[0]('dd'))
      

   def handlebookdiv(self,list):              #处理第一页的数据
      time.sleep(1)
      info = []


      for i in list:

         infocol= {}
         name = i.a.get_text()
         url = i.a['href']

         messa = i.div.get_text()

         infocol['name']=name
         infocol['author']=messa .split('/')[:2]
         introduce = self.besutifulsoupobject(i.a['href'])
         infocol['intro']= introduce
               
         info.append(infocol)
      self.collection.insert(info)
      

   def besutifulsoupobject(self,url):         #内容简介
      
      response=self.openindex(url)
            
      soup = BeautifulSoup(response)
            
      intro = soup.find('div',{"class":"intro"})
      try:
         return intro.get_text()
      except Exception,e:
         pass
         
      
               

douban = Douban()
douban.getindexurl(douban.openindex("http://book.douban.com/tag/?view=type&icn=index-sorttags-all"))

print ''

print ''

for i in douban.queen[76:100]:
   
   print len(i)
   print len(i.encode('utf8'))
for i in douban.queen[76:100]:   
   print urllib.quote(i.encode('utf8'),':=?/')
   douban.handlethis(douban.openindex((i.encode('utf8'))))
