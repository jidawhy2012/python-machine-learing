# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 12:42:57 2018

@author: haoyu
"""
#题目：输入某年某月某日，判断这一天是这一年的第几天？
y=int(input("年:"))
m=int(input("月:"))
d=int(input("日:"))
m_day=[31,28,31,30,31,30,31,31,30,31,30,31]
if 0<m<=12:
    day=d
    for i in range(0,m-1):
        day+=m_day[i]
    if m>2:
        if (y%400==0) or (y%4==0 and y%100!=0):
            day=day+1
    print(day)
else:
    print("输入错误!")
    

    
    