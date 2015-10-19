
import urllib2
import urllib
from  bs4 import BeautifulSoup
import cookielib
import re
import time
username=''             #填百度账号
password=''             #填 密码   


URL_BAIDU_LOGIN = 'https://passport.baidu.com/v2/api/?login'
tokenurl='https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login'
usertrans=urllib.quote(username) #转码能打开贴吧主页
tiebafirst='http://tieba.baidu.com/home/main?un=%s&fr=index'%usertrans

print tiebafirst
cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
urllib2.install_opener(opener);
reqReturn = urllib2.urlopen(URL_BAIDU_LOGIN );

tokenreturn=urllib2.urlopen(tokenurl).read()
tokenVal=re.findall('''"token" : "(.*?)"''',tokenreturn)
#print tokenVal[0]
#打开网页函数
def open_url(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
    headers = { 'User-Agent' : user_agent } 

    request = urllib2.Request(url,headers=headers)
    return urllib2.urlopen(request).read()

postData = {
    'username' : username,
    'password' : password,
    'u' : 'https://passport.baidu.com/',
    'tpl' : 'pp',
    'token' : tokenVal[0],
    'staticpage' : 'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
    'isPhone' : 'false',
    'charset' : 'UTF-8',
    'callback' : 'parent.bd__pcbs__ra48vi'
    };
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding':'gzip,deflate,sdch',
           'Accept-Language':'zh-CN,zh;q=0.8',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
           'Content-Type':'application/x-www-form-urlencoded',
           }  
postData=urllib.urlencode(postData)


#print postData
request = urllib2.Request(URL_BAIDU_LOGIN, postData,headers )

print urllib2.urlopen(request).read()
#print urllib2.urlopen('http://www.baidu.com').read()
time.sleep(1)


i=1

urlindex1=str('http://tieba.baidu.com/f/like/mylike?&pn=%d'%i)#获取关注贴吧首页
#print urlindex

global careTeibalist
careTeibalist=[]
global tiebaname
tiebaname=[]
#获取所有贴吧关注的贴吧
while(1):
    print type(urlindex1)
    print urlindex1
    liketieba=open_url(urlindex1)
    souplike=BeautifulSoup(liketieba)
    list = souplike.findAll('tr');
    next='下一页'.decode('gb2312')
    nexttieba_url=souplike.find_all('a',text='%s'%next)

    list = list[1:len(list)];

    print '贴吧链接\\t吧名\\t等级';
    for elem in list:
            soup1 = BeautifulSoup(str(elem));
            print soup1.find('a')['href']+ '\t' +soup1.find('a')['title']
            tiebaqiandao_url='http://tieba.baidu.com/'+soup1.find('a')['href']
            careTeibalist.append(tiebaqiandao_url)
            tiebaname.append(soup1.find('a')['title'])

    
    
    if (len(nexttieba_url)!=0):
        
        
            i=i+1
            urlindex1=str('http://tieba.baidu.com/f/like/mylike?&pn=%d'%i)
            print urlindex1
            continue
    else:
        
        break

#判断签到函数
def qianhaocheck(url,name):
    qiandaourl=open_url(url)
    soup1=BeautifulSoup(qiandaourl)
    finish='签到完成'.decode('gb2312')
    a=soup1.find_all('a',title='%s'%finish)
    if(len(a)!=0):
        print "已经签到"
        print '------------------next-------------------------'
        
    else:
        qiandao(url,name)
        qianhaocheck(url,name)
    
        
#签到函数
def qiandao(url,name):
    time.sleep(1)
    tbs='http://tieba.baidu.com/dc/common/imgtbs'
    we=urllib2.urlopen(tbs).read() 
    print we
    wee=re.findall('''{"tbs":"(.*?)"''',we)
    #print wee[0]
    
    postData1 = {
    "ie":"utf-8",
    "tbs":wee[0],
    "kw":name.encode('utf-8'),
    };
    purl='http://tieba.baidu.com/sign/add'


    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Encoding':'gzip,deflate,sdch',
           'Accept-Language':'zh-CN,zh;q=0.8',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
           'Content-Type':'application/x-www-form-urlencoded',
           }
    postData1 = urllib.urlencode(postData1);
    #print postData1
    print ''
    print ''
    
    request = urllib2.Request(purl,postData1,headers)
    
    
    urllib2.urlopen(request)
    print urllib2.urlopen(request).read()
    time.sleep(1)
    print "！！！！！！！！！正在签到若 卡住(captcha_vcode_str!=null)则是遇到验证码，关闭程序等待技术更新！！！！！"
    qingchun=urllib2.urlopen(url).read()
    print urllib2.urlopen('http://tieba.baidu.com/sign/getVcode').read()
    soup1=BeautifulSoup(qingchun)
    soup2=soup1.find('div',{"id":"signstar_wrapper"})
    #print soup2
#实现签到功能

for i in range(0,len(tiebaname)):
    print  tiebaname[i]
    print careTeibalist[i]

for i in range(0,len(tiebaname)):
    #print careTeibalist[i]
    print tiebaname[i]
    qianhaocheck(careTeibalist[i],tiebaname[i])
print "签到完成共有"+str(len(careTeibalist)) +"贴吧"
    

    

    

            














   
    


        




