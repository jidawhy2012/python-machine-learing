# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:45:48 2018

@author: haoyu
"""

def inp(numbers):
    for i in range(6):
        numbers.append(int(input('输入一个数字:\n')))
p=0
def arr_max(array):
    max=0
    for i in range(1,len(array)-1):
        p=i
        if array[p]>array[max]:
            max=p
    k=max
    array[0],array[k]=array[k],array[0]

def arr_min(array):
    min=0
    for i in range(1,len(array)-1):
        p=i
        if array[p]<array[min]:
            min=p
            
    l=min
    array[5],array[l]=array[l],array[5]
    
def outp(numbers):
    for i in range(len(numbers)):
        print(numbers[i])
        
        
if __name__=='__main__':
    array=[]
    inp(array)
    arr_max(array)
    arr_min(array)
    print('计算结果：')
    outp(array)
        
        
