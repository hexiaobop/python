# coding=utf-8   #
__author__ = 'younger'
import datetime
import time
start = time.time()
st1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


from jingdong import input_keyword,open_url,goods_url
s=input_keyword()
open_url(s)
goods_url()
end = time.time()
end1=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print '开始时间：'+st1
print '结束时间:'+end1
print '程序运行时间：',
print end-start
