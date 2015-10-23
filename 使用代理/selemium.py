
# -*- coding: utf-8 -*-
import urllib2

import urllib





def pro(ip1,url):
    
    print ip1
        
    proxy = {"http":ip1}
        
    proxy_support = urllib2.ProxyHandler(proxy)
        
    opener = urllib2.build_opener(
    proxy_support)
        
    urllib2.install_opener(opener)
        
    for j in range(100):
        i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
        req = urllib2.Request(url,headers=i_headers)
        html = urllib2.urlopen(req)        
        print html.getcode()
fp = open(u"代理.txt","r")
ips = fp.readlines()
print ips

for i in range(1,10):
    
    urllib.urlopen("http://www.itrip.com/ouzhou/")
    

for i in ips:
    
    for j in range(1,10):
        
        pro(i,"http://www.itrip.com/ouzhou/")



