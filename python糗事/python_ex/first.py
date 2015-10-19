# coding=utf-8   #

class Bob:
    def input_all(self):
        while(1):                                                             #判断子弹数不大于气球数
            n_k = raw_input("请输入气球个数和子弹数量（子弹数不大于气球数）:")
            str = n_k.split()                                                   #存气球和子弹数的列表
            if(int(str[1])>int(str[0])):
                print "子弹数不大于气球数"
                continue
            else:
                break
        while(1):
            fraction = raw_input("输入 "+str[0]+" 个气球的分数:")
            lis = fraction.split()                                              #存分数的列表
            print len(lis)
            if(int(str[0])!=len(lis)):
                print "输入个数不正确"
                continue
            else:
                break
        self.deal_data(int(str[1]), lis)
    def deal_data(self,k,lis):

        li2 = []
        for i in lis:
            li2.append(int(i))
        li2.sort(reverse=True)
        print "Bob的分数：",sum(li2[0:k])

b=Bob()
b.input_all()
#复杂度算不来
