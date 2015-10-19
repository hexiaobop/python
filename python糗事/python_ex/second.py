# coding=utf-8   #
#http://www.cc98.org/hottopic.asp 网址不能登入    抓取的是糗事百科
import urllib2
import re
def usual_open(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(url, headers = headers)
    return urllib2.urlopen(req).read()
def screen(response):
    ss=re.findall('''<div class="author clearfix">.*?<a class="bds_renren renren">''', response,re.S)
    print "这一页有"+str(len(ss))+"个"
    for i in ss:
        all_data(i)
def all_data(data):
    list=[]
    ss=re.findall(r'''<a href=".*">(.*?) </a>''', data,re.S)
    ss1=re.findall(r'''<div class="content".*?>(.*?)</div>''', data,re.S)
    ss3=re.findall(r'''<span class="stats-vote"><i class="number">(.*?)</i>(.*?)</span>''',data,re.S)
    ss4=re.findall(r'''<i class="number">(.*?)</i> ''',data,re.S)
    print "发布者：",ss[0]
    print "内容：",ss1[0].strip()
    print  ss3[0][0],ss3[0][1],ss4[1],"回复/评论"
    print ''
url="http://www.qiushibaike.com/"
respon=usual_open(url)
screen(respon)

