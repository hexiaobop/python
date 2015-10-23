#coding：utf8
from pybloom import BloomFilter

fp = open('代理.txt','r')
list = fp.readlines()
f = BloomFilter(capacity=10000, error_rate=0.001)

for i in list:
        
        print type(i)
        
        print i

        _a= f.add(i)



print len(f)
print '120.198.237.5:8080\n' in f    #
if  f.add('120.198.237.5:8080\n'):
        
        print "有了"


print len(f)
