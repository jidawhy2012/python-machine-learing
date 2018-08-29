# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 14:58:43 2018

@author: Administrator
"""
#方法一：
ol=int(input('please input a number:\n'))
while ol%2==0 or ol%5==0:
    ol=int(input('please input a number:\n'))

i=1
while i:
    a=int(i*'9')
    if a%ol==0:
        print("%d个9可以被%d整除：%d" %(i,ol,a))
        break
    i=i+1


#方法二：
zi=int(input('please input a number:\n'))
n1=1
c9=1
m9=9
sum=9
while n1!=0:
    if sum%zi==0:
        n1=0
    else:
        m9*=10
        sum+=m9
        c9+=1
print('%d个9可以被%d整除:%d'%(c9,zi,sum))