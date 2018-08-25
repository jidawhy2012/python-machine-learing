# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 16:19:46 2018

@author: Administrator
"""
#x,y,z=eval(input("请输入："))
#ls=[x,y,z]
#print(ls)
lst=list(map(int,input("input:").split()))
print(lst)
for i in range(0,len(lst)-1):
    for j in range(0,len(lst)-i-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)
            