# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:50:41 2018

@author: Administrator
"""
#方法一
i=0
j=1
x=0
while(i<5):
    x=4*j
    for i in range(5):
        if(x%4!=0):
            break
        else:
            i=i+1
            
        x=(x/4)*5+1
    j=j+1
    
print(x)


#笨方法
start,end,m1=0,100,0
while m1==0:
    end=end*2
    for i in range(start,end):
        m5=5*i+1
        if m5%4==0:
            m4=(m5/4)*5+1
            if m4%4==0:
                m3=(m4/4)*5+1
                if m3%4==0:
                    m2=(m3/4)*5+1
                    if m2%4==0:
                        m1=(m2/4)*5+1
                        break
    start=i
print(m1)