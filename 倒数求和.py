# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 15:27:07 2018

@author: Administrator
"""

def fn(n):
    if n==0:
        sum_n=0
    if n%2==0:
        ls=list(range(2,n+1,2))
    if n%2!=0:
        ls=list(range(1,n+1,2))
    sum_n=0
    for i in range(len(ls)):
        sum_n+=(1/ls[i])
    return(sum_n)
    
    
n=int(input('please input a number:\n'))   
print(fn(n))
    