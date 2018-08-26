# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 22:16:09 2018

@author: Administrator
"""
#方法一
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return (a)
print(fib(20))
        
#方法二
def f(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return (f(n-1)+f(n-2))
    
    
print(f(20))

#方法三
def fib(n):
    if n==1:
        return[1]
    if n==2:
        return[1,1]
    fibs=[1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs


print(fib(30))
    
    
    
    
    
    
    
    
    
    