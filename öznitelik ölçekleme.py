# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:08:26 2025"""
import pandas as pd 
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
veriler=pd.read_csv("C://Users//Huzur Bilgisayar//makine öğrenmesi//veriler.csv")
print(veriler)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()#nesne oluştu
X_train=sc.fit_transform(x_train)#biribirine daha yakın yapmak için kulllanılıyor
X_test=sc.fit_transform(x_test)


