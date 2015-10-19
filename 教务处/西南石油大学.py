
import urllib2
import urllib
from  bs4 import BeautifulSoup
import cookielib

login_url='http://xk1.swpu.edu.cn:9099/login.jsp'
post_url='http://xk1.swpu.edu.cn:9099/loginAction.do'

cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
urllib2.install_opener(opener)
reqReturn = urllib2.urlopen(login_url)

username=''
password=''

postdata={'zjh':username,
          'mm':password,
    }
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding':'gzip,deflate,sdch',
           'Accept-Language':'zh-CN,zh;q=0.8',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
           'Content-Type':'application/x-www-form-urlencoded',
           'Referer':'http://xk1.swpu.edu.cn:9099/loginAction.do'}  
postData=urllib.urlencode(postdata)
request = urllib2.Request(post_url, postData, headers)
response = urllib2.urlopen(request)
print response
URL='http://xk1.swpu.edu.cn:9099/bjKbInfoAction.do?oper=bjkb_xx&xzxjxjhh=2014-2015-1-2&xbjh=13010101&xbm=%CA%AF%B9%A41301&xzxjxjhm=2014-2015%D1%A7%C4%EA%C7%EF(%C1%BD%D1%A7%C6%DA)&'
URL1='http://xk1.swpu.edu.cn:9099/gradeLnAllAction.do?type=ln&oper=qbinfo'
responseA = urllib2.urlopen(URL1).read()
# print responseA.decode("gbk")

soup=BeautifulSoup(responseA,fromEncoding="gb18030")
print soup.find_all('td',align="center")

s=[' ']
for i in soup.find_all('td',align="center"):
    print i.get_text().strip()
    s.append(i.get_text())
  
   
    


        




