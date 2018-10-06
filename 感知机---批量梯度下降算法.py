# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:20:15 2018

@author: haoyu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

df=pd.read_csv("iris.data")

df.tail()
y=df.iloc[0:100,4].values
y=np.where(y=='Iris-setosa',-1,1)
X=df.iloc[0:100,[0,2]].values
plt.scatter(X[:49,0],X[:49,1],color='red',marker='o',label='setosa')
plt.scatter(X[49:100,0],X[49:100,1],color='blue',marker='x',label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()

class AdalineGD():
    def __init__(self,eta=0.01,n_iter=50):
        self.eta=eta
        self.n_iter=n_iter
    def fit(self,X,y):
        self.w_=np.zeros(1+X.shape[1])
        self.cost_=[]
        for i in range(self.n_iter):
            output=self.net_input(X)
            errors=(y-output)
            self.w_[1:]+=self.eta*X.T.dot(errors)
            self.w_[0]+=self.eta*errors.sum()
            cost=(errors**2).sum()/2
            self.cost_.append(cost)
        return self
    def net_input(self,X):
        return np.dot(X,self.w_[1:])+self.w_[0]
    def activation(self,X):
        return self.net_input(X)
    def predict(self,X):
        return np.where(self.activation(X)>=0,1,-1)
    
def plot_decision_regions(X,y,classifier,resolution=0.02):
    markers=('s','x','o','^','v')
    colors=('red','blue','lightgreen','gray','cyan')
    cmap=ListedColormap(colors[:len(np.unique(y))])
    
    
    x1_min,x1_max=X[:,0].min()-1,X[:,0].max()+1
    x2_min,x2_max=X[:,1].min()-1,X[:,1].max()+1
    xx1,xx2=np.meshgrid(np.arange(x1_min,x1_max,resolution),
                        np.arange(x2_min,x2_max,resolution))
    Z=classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    Z=Z.reshape(xx1.shape)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())
    
    for idx,cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl,0],y=X[y==cl,1],alpha=0.8,c=cmap(idx),marker=markers[idx],label=cl)
    plt.contourf(xx1,xx2,Z,alpha=0.55,cmap=ListedColormap(('red','blue')))
    

ada1=AdalineGD(n_iter=10,eta=0.01).fit(X,y)
ada2=AdalineGD(n_iter=10,eta=0.0001).fit(X,y)

fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(8,4))
ax[0].plot(range(1,len(ada1.cost_)+1),np.log10(ada1.cost_),marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squared-error)')
ax[0].set_title('Adaline-Learning-rate 0.01')

ax[1].plot(range(1,len(ada2.cost_)+1),np.log10(ada2.cost_),marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('log(Sum-squared-error)')
ax[1].set_title('Adaline-Learning-rate 0.0001')
plt.show()

"""上面取两种学习率0.01和0.001，当学习率为0.01时，显然过大，代价函数跳过了
局部或者全局最小值，导致误差随着迭代次数的增加而增加；当学习率过小时，为了达
到算法收敛的目的，需要非常多的迭代次数，导致算法的求解速度变慢"""
""" 为解决这个问题，下面首先对特征数据进行标准化处理"""


X_std=np.copy(X)
X_std[:,0]=(X[:,0]-X[:,0].mean())/X[:,0].std()
X_std[:,1]=(X[:,1]-X[:,1].mean())/X[:,1].std()

ada=AdalineGD(n_iter=15,eta=0.01)
ada.fit(X_std,y)
plot_decision_regions(X_std,y,classifier=ada)
plt.title('Adline-Gradient Descent')
plt.xlabel('sepal length [standardized]')
plt.ylabel('petal length [standardized]')
plt.legend(loc='upper left')
plt.show()

plt.plot(range(1,len(ada.cost_)+1),ada.cost_,marker='o')
plt.xlabel('Epochs')
plt.ylabel('Sum-squared-error')
plt.show()



















