# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 16:55:02 2018

@author: Administrator
"""

n=int(input('please number of input:\n'))
student=[]
for i in range(n):
    student.append(['','',[]])
print(student)
def input_stu(stu):
    for i in range(n):
        stu[i][0]=input('input student num:\n')
        stu[i][1]=input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))
def output_stu(stu):
    for i in range(n):
        print('%6s-%10s'%(stu[i][0],stu[i][1]))
        for j in range(3):
            print('%8d'%(stu[i][2][j]))




input_stu(student)
print(student)
output_stu(student)
