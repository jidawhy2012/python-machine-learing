# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 09:06:00 2018

@author: Administrator
"""

nmax=50
n=int(input('请输入人数:\n'))
num=[]
for i in range(n):
    num.append(i+1)
print(num)
    
i=0
k=0
m=0
while m<n-1:
    if num[i]!=0:
        k+=1
    if k==3:
        num[i]=0
        k=0
        m+=1
    i+=1
    if i==n:
        i=0
i=0
while num[i]==0:
    i+=1
print(num[i])
            