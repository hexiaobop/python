# coding=utf-8   #
import re
import urllib
ss=u"你好".encode("gbk")
fp=open(u"文本处理.txt",'r+')
file2=fp.readlines()
print file2
for i in file2:
    print i.decode("gbk")
    s=re.findall(".*%s.*"%ss,i)
    for j in s:
        print j.decode("gbk")

fp.close()
fp1=open("ss.txt","r+")
q=fp1.readlines()
fp2=open("new.txt","w")
for i in q:
    print i

    fin=re.findall('''class="(.*?)"''',i)
    if len(fin)>0:
        i=i.replace(fin[0],'",style="')
        print "有结果",i.replace(fin[0],"")
        fp2.writelines(i)
    else:
        fp2.writelines(i)


