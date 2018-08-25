# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 09:28:56 2018

@author: haoyu
"""
#问题描述
#企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
#利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元
#的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
#40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60
#万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从
#键盘输入当月利润I，求应发放奖金总数？
#方法一：暴力求解
award_10=1
award_20=0.75
award_40=1
award_60=0.6
award_100=0.6
profile=float(input("当月利润为："))
if profile<=10:
    rew=profile*0.01
if 10<profile<=20:
    rew=award_10+(profile-10)*0.075
if 20<profile<=40:
    rew=award_10+award_20+(profile-20)*0.05
if 40<profile<=60:
    rew=award_10+award_20+award_40+(profile-40)*0.03
if 60<profile<=100:
    rew=award_10+award_20+award_40+award_60+(profile-60)*0.015
if profile>100:
    rew=award_10+award_20+award_40+award_60+award_100+(profile-100)*0.01
print("当月提成为：",rew)

#方法二：算法求解
i=int(input("净利润:"))
arr=[100,60,40,20,10,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print(i,'-',arr[idx],'*',rat[idx],'=',(i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)






