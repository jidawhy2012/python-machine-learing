# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:48:52 2018

@author: haoyu
"""

#笨办法       
person = {"li":18,"wang":50,"zhang":20,"sun":22}
tup=list(person.items())
ls=[]
for i in range(len(tup)):
    ls.append(tup[i][1])
print(ls)
j=ls.index(max(ls))
print(tup[j])
#巧办法
person = {"li":18,"wang":50,"zhang":20,"sun":22}
m='li'
for key in person.keys():
    if person[m]<person[key]:
        m=key
print(m,person[m])
#一句话
from operator import itemgetter
person = {"li":18,"wang":50,"zhang":20,"sun":22}
lp=sorted(person.items(),key=itemgetter(1),reverse=True)
print(lp[0])
