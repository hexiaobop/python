# coding=utf-8   #
__author__ = 'younger'
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
from pprint import pprint
import time
global urlKey  #输入关键字
global b,UrlAll  #
global AName
global comment  #网页url

b=[]

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
    data=urllib2.urlopen(url).read()
    soup=BeautifulSoup(data)
    listMain=soup.find_all('a',{'rel':'nofollow','title':re.compile(".*")})
    for i in listMain:
        ListEver=i.get_text().strip()
        b.append(ListEver)
    print ''
    print "*********京东共有你所搜索的"+urllib.unquote(urlKey)+"的品牌有"+str(len(listMain)-1)+"种",
    print "选择排序方式"

def goods_url():                                                        #综合操作，显示初步结果
    p=1
    for i in b[:-1]:
        print '第'+str(p)+'个商品',
        AName=set()
        he=i.encode('utf-8')
        global next_page
        next_page = 0
        # print "综合排序",
        # print "http://search.jd.com/search?keyword="+urlKey+"&enc=utf-8&ev=exbrand_"+urllib.quote(he)+"&psort=0"
        # print "评论数"
        # print "http://search.jd.com/search?keyword="+urlKey+"&enc=utf-8&ev=exbrand_"+urllib.quote(he)+"&psort=4"

        comment="http://search.jd.com/search?keyword="+urlKey+"&enc=utf-8&ev=exbrand_"+urllib.quote(he)+"&psort=4&page=0"

        # print "价格",
        # print "http://search.jd.com/search?keyword="+urlKey+"&enc=utf-8&ev=exbrand_"+urllib.quote(he)+"&psort=2"
        # print "销量",
        # print "http://search.jd.com/search?keyword="+urlKey+"&enc=utf-8&ev=exbrand_"+urllib.quote(he)+"&psort=3"
        response=usual_open(comment)         #抓取每个商品的数量
        # obtain_goods(response,comment,he,p)
        p=p+1
        open_first(response,comment)

def open_first(responses,comment):
        UrlAll=set()
        soup=BeautifulSoup(responses)
        all_goodsurl=soup.find('ul',{'class':'list-h clearfix','tpl':'1',})
        next_pag=soup.find_all('span',{'class':'next-disabled'})
        print 'next_pag****************'+str(len(next_pag))
        find_pname(str(all_goodsurl))
        if len(next_pag)!=0:
            print next_pag
            print '没有下一页'
            pass
        else:
            print '有下一页'
            global next_page
            print next_page
            next_page+=1
            comment1=re.findall('''(.*?)page=.*''',comment)
            comment=comment1[0]+'page='+str(2*next_page)
            print comment
            response=usual_open(comment)
            open_first(response,comment)
        # for i in all_goodsurl:
        # ss=BeautifulSoup(str(all_goodsurl)).find('div',{'class':'p-name'})
        # print ss.a['href']
        # print "每个品牌第一页商品链接和加入购物车链接："
        # for i in UrlAll:
        #     print i
        # time.sleep(1)

# def obtain_goods(response,url,ever,p):                                       #商品数量函数
#         number=re.findall('''<strong id="res_count">(.*?)</strong>''',response,re.S)
#         if (p%2)==0:
#             print '       %-30s'%ever,
#             print ('(商品有'+str(number)+'种)').lstrip() ,
#             print
#         else:
#             print "%-30s" %ever,
#             print ('(商品有%s'+str(number)+'种)').lstrip() ,

def find_pname(data):  #获取每一页商品链接
    soup=BeautifulSoup(data)
    p_name=soup.find_all('div',{'class':'p-name'})
    for i in p_name:
        print i.a['href']
        open_allgoods(i.a['href'])


def comment_spider(url,name):                                                                            #抓取商品评论
    while(True):
        sponse = usual_open(url)
        soup = BeautifulSoup(sponse,fromEncoding="gb18030")
        next = soup.find_all('a', {'class':'next'})
        data = soup.find_all('div',{'data-widget':'tab-content'})
        if (len(next)!=0):
            print 1,
            # print len(next),next[0]["href"],
            fp=open("%s.txt"%name,"a")
            for i in data:
                fp.write(i.encode('utf-8'))
            fp.close()
            url=next[0]["href"]
            continue
        else:
            print "没有找到评论"
            break
def open_allgoods(url):                            #获取商品基本信息
    response = usual_open(url)
    soup = BeautifulSoup(response)
    message = soup.find('div',{'id':'name'})
    pricePage = " http://p.3.cn/prices/get?skuid=J_"  #构造获取价格的地址
    priceNumber = re.findall('''/item.jd.com/(.*?).html''', url)
    sss = usual_open(pricePage+priceNumber[0])
    ssss=re.findall('''"p":"(.*)",''',sss)           #获取价格
    comment_url ="http://club.jd.com/review/"+priceNumber[0]+"-0-1-0.html"
    print comment_url
    comment_spider(comment_url,priceNumber[0])
    fp= open ("%s.txt"%priceNumber[0],"a")
    fp.writelines( message.get_text().strip()+ssss[0])
    fp.close()



















