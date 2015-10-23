# -*- coding:utf-8 -*-
import urllib2
import random
from pybloom import BloomFilter
from bs4 import BeautifulSoup
class Open():
    
    
    
    #def __init__(self):
        
       
    @staticmethod
    def urlunique():
        
        fp = open(u'代理.txt','r')
        ips = fp.readlines()
        return ips
        
    
    @staticmethod
    def useproxy(url):                #使用代理
        ip1 = '101.226.249.237:80'
        proxy = {"http":ip1}        
        proxy_support = urllib2.ProxyHandler(proxy)           
        opener = urllib2.build_opener(proxy_support)           
        urllib2.install_opener(opener)
        i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
        req = urllib2.Request(url,headers=i_headers)
        html = urllib2.urlopen(req)
        print html.getcode()
        return html.read()
    
    @staticmethod
    def openurl(url):                    #不使用代理
        try:
            i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
            req = urllib2.Request(url,headers=i_headers)
            html = urllib2.urlopen(req)
            print html.getcode()
            
            return html.read()
        except Exception,e:
            
            print e
    @staticmethod
    def buildsoup(response):    #构造beautifulsoup
        return BeautifulSoup(response.decode('gb2312','ignore'))
    
