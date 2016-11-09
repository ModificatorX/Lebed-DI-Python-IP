import re
f1=open('access.log', 'r')
s=set()
s1=set()
sl={}
for line in f1.readlines():
    result=re.findall(r'^[0-2]{0,1}[0-9]{0,1}[0-9]\.[0-2]{0,1}[0-9]{0,1}[0-9]\.[0-2]{0,1}[0-9]{0,1}[0-9]\.\d*', line)
    result1=re.findall(r'^([0-2]{0,1}[0-9]{0,1}[0-9]\.[0-2]{0,1}[0-9]{0,1}[0-9]\.[0-2]{0,1}[0-9]{0,1}[0-9])\.\d*', line)
    s.update(result)
    s1.update(result1)           
for i in s1:
    for j in s:
        if re.match(i, j):
            sl.setdefault(i, []).append(j)#({i:[j]})    
for i in sl:
    print (i,':', sl.get(i))
a=input()

