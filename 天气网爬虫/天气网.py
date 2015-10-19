
import re
from bs4 import BeautifulSoup,Comment  ##��Ҫ��װ��
import urllib2
import time

class Weather_Today:
    
    def __init__(self):#��ʼ��
        self.firstPage='http://www.weather.com.cn/live/'   ##��ҳ
        self.titlePage="http://www.weather.com.cn/textFC/hb.shtml" ##��ȡ��������ַ
        self.data=[ ]
        self.mainHref=[ ]
        self.l=0
        self.weather=[ ]
        




  
    def OpenFirst(self,myUrl):   ##����ҳ����ȡ
        
        
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'   
        headers = { 'User-Agent' : user_agent }   
        req = urllib2.Request(myUrl, headers=headers)   
        myResponse = urllib2.urlopen(req)  
        myPage = myResponse.read()
      
        return myPage
    def GetTitle(self):              
        my=self.OpenFirst(self.titlePage)
        soup=BeautifulSoup(my)
        first=soup.find("div",{"class":"conMidtab"}) ##find�Ľ��Ϊ������������
        for k in first.table("tr")[0]:              
            thOne=k.get_text()
            self.weather.append(thOne)
            self.weather.append("     ")
        
        self.weather.append("\n")
        self.weather.append("                      ")
        for k in first.table("tr")[1]:
            thOne=k.get_text()
            self.weather.append(thOne)
        
        self.weather.insert(17,"      ")
        self.weather.append("\n")
       
        
         
  
    def OpenPart(self):
        while self.l<8:
        
            
            e=self.OpenFirst(self.mainHref[self.l])
            self.AllRead(self.weather)
            self.FindAll(e)
            
            self.l=self.l+1
       
        
           

    def FindAll(self,myPage):     ##��ȡ��Ҫ����
        td=[ ]
        
        
        
        soup=BeautifulSoup(myPage)
        comments=soup.find_all("a",text="����".decode("gb2312"))
        [comment.extract() for comment in comments]
               
        
       
        first=soup.find("div",{"class":"conMidtab"})
     
        for i in range(len(first)):
            
            m=first.contents[i]
            trTag=(m("tr"))
           
            for p in trTag[2:len(trTag)+1]:
                if len(p)==9:
                    
                    for tdd in p:
    
                        e="%7s"%tdd.get_text()
                        print e,
                        self.data.append(e)
       
                    print " "
                    self.data.append("\n")
                else:
                    print"        ",
                    self.data.append("        ")
                    for tdd in p:
                    
                         f="%7s"%tdd.get_text()
                         print f,
                         self.data.append(f)
                    print "  "
                    self.data.append("\n")
            print '\n'+'\n'
            self.data.append("\n")
                         
      
       
       
      
    def FindMain(self,myPage):      ##���Ұ˸�������ַ  
        
        
        soup=BeautifulSoup(myPage)
        s0="��������".decode("gb2312")
        s1="��������".decode("gb2312")
        s2="���е���".decode("gb2312")
        s3="���ϵ���".decode("gb2312")
        s4="��������".decode("gb2312")
        s5="���ϵ���".decode("gb2312")
        s6="��������".decode("gb2312")
        s7="�۰�̨����".decode("gb2312")
        ss=[s0,s1,s2,s3,s4,s5,s6,s7]
        mainLodition=soup.find_all("a",text=ss)
        print mainLodition
     
        for i in mainLodition:
            i1=i.get("href")
            self.mainHref.append(i1,)
            i2=i.get_text()

    def AllRead(self,list): ##����self.weather�����б�
        
        for i in list:
             print i,
    def OpenFile(self):   ##���浽�ļ�
        opF=open(" ����.txt","w")
        for one in self.weather:
            opF.write(one.encode("utf-8"))
        opF.close()
        opF=open(" ����.txt","a")
        for two in self.data:
            opF.write(two.encode("utf-8"))
        opF.close()
            

s=Weather_Today()
s.GetTitle()
s1=s.OpenFirst(s.firstPage)
s.FindMain(s1)
s.OpenPart()
s.OpenFile()
print "�ļ��ѱ��浽����.txt�ļ�"


        
            
