# -*- coding: utf-8 -*-
"""MatPlots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/sipsmehta/Machine-Learning/blob/main/Plot/MatPlots.ipynb
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn 
import seaborn as sns

pd.read_csv("/content/Mall_Customers.csv")

df=pd.read_csv("/content/Mall_Customers.csv")

df.head

df.rename(columns={'Genre':'Gender'},inplace=True)

df.head()

df.shape

df.describe()

df.dtypes

df.isnull().sum()

df.drop(["CustomerID"],axis=1,inplace=True)

df.head()

df.rename(columns={'Annual Income (k$)':'Income'},inplace=True)

df.rename(columns={'Spending Score (1-100)':'Spending score'},inplace=True)

df.head()

plt.figure(1,figsize=(15,6))
n=0
for x in ['Age', 'Income', 'Spending score']:
    n += 1
    plt.subplot(1,3,n)
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    sns.distplot(df[x], bins=20)
    plt.title('Distplot of {}'.format(x))
plt.show()

plt.figure(figsize=(15,5))
sns.countplot(y='Gender', data=df)
plt.show()

plt.figure(1,figsize=(15,7))
n=0
for cols in ['Age', 'Income', 'Spending score']:
  n+=1
  plt.subplot(1,3,n)
  sns.set(style="whitegrid")
  plt.subplots_adjust(hspace=0.5, wspace=0.5)
  sns.violinplot(x=cols,y='Gender',data=df)
  plt.ylabel('Gender' if n==1 else '')
  plt.title('Violin Plot')
plt.show()
