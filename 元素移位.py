# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 13:06:06 2018

@author:haoyu
"""

# 方法一
#n=int(input('整数n为:\n'))
#m=int(input('向后移动m个位置:\n'))
#
#def move(array,n,m):
#    array_end=array[n-1]
#    for i in range(n-1,-1,-1):
#        array[i]=array[i-1]
#    array[0]=array_end
#    m-=1
#    if m>0:
#        move(array,n,m)
#        
#number=[]
#for i in range(n):
#    number.append(int(input('输入一个数字:\n')))
#print('原始列表:',number)
#move(number,n,m)
#print('移动之后:',number)  


#方法二
n=int(input('整数n为:\n'))
m=int(input('向后移动m个位置:\n'))
array=[]
for i in range(n):
    array.append(int(input('输入一个数字:\n')))
print('原始列表:',array)
array_end=array[n-1]
while m>0:
    array_end=array[n-1]
    for i in range(n-1,-1,-1):
        array[i]=array[i-1]
    array[0]=array_end
#    print('第%d步后:array'%m,array)
    m-=1
print('移动之后:',array)