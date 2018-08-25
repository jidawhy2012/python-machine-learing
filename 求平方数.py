# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 11:37:22 2018

@author: Administrator
"""

#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，
#请问该数是多少？
    
#技巧求解法
start_time=time.perf_counter()  
for i in range(1,85):
    if 168%i==0:
        j=168/i
        if i>j and (i+j)%2==0 and (i-j)%2==0:
            m=(i+j)/2
            n=(i-j)/2
            x=n**2-100
            print(x)
dur=time.perf_counter()-start_time
print(dur)
            
#暴力求解 
import time
start_time=time.perf_counter()           
for x in range(0,2000):
    if ((x+100)%((x+100)**0.5))==0 and ((x+268)%((x+268)**0.5))==0:
        print(x)
dur=time.perf_counter()-start_time
print(dur)