# coding=utf-8   #
__author__ = 'younger'
import re
import urllib
import urllib2
from bs4 import BeautifulSoup


# comment='http://search.jd.com/search?keyword=%E5%B7%A7%E5%85%8B%E5%8A%9B&enc=utf-8&ev=exbrand_%E8%B4%B9%E5%88%97%E7%BD%97%EF%BC%88Ferrero%20Rocher%EF%BC%89&psort=4&page=42'
#
# response=urllib.urlopen(comment).read()
# soup=BeautifulSoup(response)
# ss=soup.find_all('span',{'class':'next-disabled'})
# print len(ss)
# ss="http://item.jd.com/2.html"
# ss1=re.findall('''/item.jd.com/(.*?).html''',ss)
# print type(ss1[0])
# url="http://club.jd.com/review/730618-0-1-0.html";

def usual_open(url):                #页面打开函数，返回页面源码
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req=urllib2.Request(url, headers = headers)
    return urllib2.urlopen(req).read()

def input_keyword():           #用户输入关键字函数
    global urlKey
    inputKeyword=raw_input('*******************input key:')
    urlKey=urllib.quote(inputKeyword)
    return "http://search.jd.com/Search?keyword="+str(urlKey)+"&enc=utf-8"

def open_url(url):                      #抓取用户输入商品的所有品牌
    global b
    b=[]
    data=urllib2.urlopen(url).read()
    soup=BeautifulSoup(data)
    listMain=soup.find_all('a',{'rel':'nofollow','title':re.compile(".*")})
    for i in listMain:
        ListEver=i.get_text().strip()
        b.append(ListEver)
    print ''
    s="*********京东共有你所搜索的"+urllib.unquote(urlKey)+"的品牌有"+str(len(listMain)-1)+"种"
    print s
    print "选择排序方式"


def obtain_goods():                                       #商品数量函数
    for i in b:
        comment="http://search.jd.com/search?keyword="+urlKey+"&enc=utf-8&ev=exbrand_"+urllib.quote(i.encode('utf-8'))+"&psort=4&page=0"
        response=usual_open(comment)
        print i,
        number=re.findall('''<strong id="res_count">(.*?)</strong>''',response,re.S)
        print str(number).lstrip()
        fp = open("index.doc","a")
        fp.writelines(i.encode("utf-8")+"#"+str(number).lstrip()+"\n")
        fp.close()

        # if (p%2)==0:
        #     print '       %-30s'%ever,
        #     print ('(商品有'+str(number)+'种)').lstrip() ,
        #     print
        # else:
        #     print "%-30s" %ever,
        #     print ('(商品有%s'+str(number)+'种)').lstrip() ,



global b
url=input_keyword()
print url
open_url(url)
# obtain_goods()


