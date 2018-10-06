# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:05:37 2018

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

class Perceptron():
    def __init__(self,eta=0.01,n_iter=10):
        self.eta=eta
        self.n_iter=n_iter
    def fit(self,x,y):
        self.w_=np.zeros(1+x.shape[1])
        self.errors_=[]
        for _ in range(self.n_iter):
            errors=0
            for xi,target in zip(x,y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:]+=update*xi
                self.w_[0]+=update
                errors+=int(update !=0)
            self.errors_.append(errors)
        return self
    def net_input(self,x):
        return np.dot(x,self.w_[1:])+self.w_[0]
    def predict(self,x):
        return np.where(self.net_input(x)>=0.0,1,-1)
    

ppn=Perceptron(eta=0.1,n_iter=10)
ppn.fit(X,y)
plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='o')  
plt.xlabel('Epochs')
plt.ylabel('Number of misclassifications')
plt.show()  
    
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
    
    
plot_decision_regions(x,y,classifier=ppn)
plt.xlabel('sepal length [cm]')
plt.ylabel('petal length [cm]')
plt.legend(loc='upper left')

plt.show()














    
