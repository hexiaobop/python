#coding=utf-8
import sys, getopt
import re,string,pymongo
import threading
import Queue
from Open_page import OpenPage
opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
class Get_picture:
    def __init__(self):
        self.url_list=Queue.Queue()                   #队列不设置长度，多线程使用
        self.set = set()
        self.Open_page=OpenPage()
        self.mutex = threading.Lock()
    def Get_picture_url_in_homepage(self,url):       #从首页提取二级目录，title,图片链接
        count = 3                                     #设置默认请求的次数，三次不成功就没办法了
        while(count>0):
            try:
                myPage=self.Open_page.Openpage(url)
                break
            except Exception as e:
                print e
                count-=1
        url_list1=re.findall(' href="/mm/(.*?)" title="(.*?)" target="_blank">',myPage)      #提取首页链接，由于首页图片都是小图片就不保存了
        for r in url_list1:
            if len(r[0])>50:                                                                  #排除无用的url
                pass
            else:
                r3 = url+"mm/"+r[0]                                                            #完整url
                date=r3+'#'+r[1].decode("utf-8")
                self.set.add(date)                                                       #将首页url，title加入队列

        for i in self.set:
            print i
            self.url_list.put(i)

    def Get_page_number(self,myPage):                                                         #获取二级目录图片的页数,并返回页数
        page_number=re.findall('<strong class="diblcok"><span class="fColor">(.*?)</span>/(.*?)</strong>',myPage)
        if(len(page_number)<2):
            return page_number[0][1]                #返回图片总数构造图片url用要到
        else:
            pass

    def Save_picture_url(self,href_list,table_name,title):                                    #mongo操作，链接，数据插入
        conn = pymongo.MongoClient("127.0.0.1",27017)

        self.mutex.acquire()
        self.db = conn.picture                                                                #连接库

        print "_______________________--链接成功".decode("utf-8")

        self.db.table_pictur.insert({'_id':title,"picture_url":href_list})
        self.mutex.release()


    def Get_picture_url_in_seconde_page(self,url,table_name,title):  #从二级目录页提取图片链接并遍历所有页
        print table_name
        count = 3
        href_list=[]                                                #列表存储相册下的所有图片链接
        while(count>0):
            try:
                myPage=self.Open_page.Openpage(url)
                break
            except Exception as e:
                print e
                count -=1

        picture_url=re.findall('<div id="imgString"><img src="(.*?)"></div>',myPage)      #在这儿把第一张图片链接取出来
        if len(picture_url)>0:
            href_list.append(picture_url[0])
        else:
            print "!!!!!!图片链接提取失败!!!!!"
        page_number=self.Get_page_number(myPage)                                         #获取相册中图片总数

        for i in range(2,int(page_number)+1):                                           #构造相册中图片链接
            url2=url.split('.html')[0]
            next_url=url2+'-%s.html'%i
            count=3
            while(count>0):
                try:
                    the_myPage=self.Open_page.Openpage(next_url)
                    break
                except Exception as e:
                    print e
                    count-=1

            picture_url=re.findall('<div id="imgString"><img src="(.*?)" /></div>',the_myPage)   #获取图片url
            print picture_url[0]



            if len(picture_url)>0:
                href_list.append(picture_url[0])


            else:
                print "图片链接提取失败！"
        self.Save_picture_url(href_list,table_name,title)                                    #图片队列，表名写死了，标题


if __name__=="__main__":
    ss=Get_picture()
    thread_number=10
    table_name = "table_picture"
    for op, value in opts:#写各种参数的作用
        if op == "-n":
            thread_number=value         #线程数
        elif op == "-l":
            picture_number=value       #爬多少图片
        elif op=='-o':
            table_name=value        #表名

        elif op == "-h":             #帮助内容

            print '-n 后面带指定线程数目'
            sys.exit()

    url='http://www.22mm.cc/'
    ss.Get_picture_url_in_homepage(url)
#    raw_input('ssssssss')
    while(ss.url_list.qsize()>0):
        thread=[]

        for count in range(0,thread_number):
            data=ss.url_list.get()
            data=data.split('#')


            thread.append(threading.Thread(target=ss.Get_picture_url_in_seconde_page,args=(data[0],table_name,data[1])))
        for t in thread:
            try:
                t.start()
            except Exception as e2:
                print e2

        for t in thread:

            t.join()






