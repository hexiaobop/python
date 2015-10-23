# -*- coding:utf-8 -*-
import threading
from read import *
from Threads import MyThread
import thread
import time
url = 'http://yuedu.baidu.com/book/list/0?od=1&show=0&pn=8940'

bai = BaiDuReading(url)
thread.start_new_thread(bai.everypageurl, ())
#print bai.queue.get()

print bai.queue.qsize()
threads=[]
while(not bai.queue.empty()):
    print bai.queue.qsize()
    if len(threads)>10:
        for i in threads:
            
            i.start()
        
        threads=[]
        
    else:
    
        url = bai.queue.get()    
        thre = MyThread(url)
        threads.append(thre)


    


