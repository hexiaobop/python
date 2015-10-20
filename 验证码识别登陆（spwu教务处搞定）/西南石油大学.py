from pytesser import *
from PIL import Image
import urllib2
import urllib
from  bs4 import BeautifulSoup
import cookielib
import time

login_url='http://jwxt.swpu.edu.cn/loginAction.do'
post_url='http://jwxt.swpu.edu.cn/loginAction.do'

cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
urllib2.install_opener(opener)
urllib2.urlopen(login_url).read()
for index, cookie in enumerate(cj):
    print '[',index, ']',cookie;
time.sleep(1)
#urllib2.urlretrieve('http://jwxt.swpu.edu.cn/validateCodeAction.do?random=0.9542063928674906','yan.jpg')
fp =open('yan.jpg','wb')
urlopne =urllib2.urlopen('http://jwxt.swpu.edu.cn/validateCodeAction.do?random=0.9542063928674906')
fp.write(urlopne .read())
fp.close()
for index, cookie in enumerate(cj):
    print '[',index, ']',cookie;
image = Image.open('yan.jpg')  # Open image object using PIL
yanstring = image_to_string(image)[:4]     # Run tesseract.exe on image
print yanstring[:4]
username='1205030229'
password='KZEBNL'

postdata={'zjh1':'','tips':'','lx':'','evalue':'','eflag':'','fs':'','dzslh':'','zjh':username,'mm':password,'v_yzm':yanstring,
            
    }
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding':'gzip,deflate',
           'Accept-Language':'zh-CN,zh;q=0.8',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
           'Content-Type':'application/x-www-form-urlencoded',
            'Origin:http':'//jwxt.swpu.edu.cn',
           'Referer':'http://jwxt.swpu.edu.cn/loginAction.do',}  
postData=urllib.urlencode(postdata)
print postdata['v_yzm']
request = urllib2.Request(post_url, postData, headers)
print  postData
response = urllib2.urlopen(request)
print request
print response.getcode()
print response.read()

URL='http://jwxt.swpu.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2014-2015%D1%A7%C4%EA%B4%BA(%C1%BD%D1%A7%C6%DA)'
URL1='http://xk1.swpu.edu.cn:9099/gradeLnAllAction.do?type=ln&oper=qbinfo'

responseA = urllib2.urlopen(URL).read()
#print responseA.decode("gbk")

soup=BeautifulSoup(responseA)
print soup.find_all('td',align="center")

s=[' ']
for i in soup.find_all('td',align="center"):
    print i.get_text().strip()
    s.append(i.get_text())
  
   
    


        




