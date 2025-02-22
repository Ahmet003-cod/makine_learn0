# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:14:52 2025
@author: Huzur Bilgisayar
"""
import pandas as pd 
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
veriler=pd.read_csv("C://Users//Huzur Bilgisayar//makine öğrenmesi//veriler.csv")#veri adresi windows
ulke=veriler.iloc[:,0:1].values#(Ülke sütunu) seçiyor ve NumPy dizisine çeviriyor.
print(ulke)
print()
ln=preprocessing.LabelEncoder()#LabelEncoder, kategorik verileri sayıya dönüştürür
ulke[:,0]=ln.fit_transform(veriler.iloc[:,0])
ohe=preprocessing.OneHotEncoder()#bunları binary (0 ve 1) formatına çevireceğiz.
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

sonuc=pd.DataFrame(data=ulke,index=range(22),columns=("tr","fr","us"))
print(sonuc)
print()
yas=veriler.iloc[:,1:4]
imputer=SimpleImputer(missing_values=np.nan,strategy="median")#ortanca
yas[:]=imputer.fit_transform(yas)
sonuc2=pd.DataFrame(data=yas,index=range(22),columns=["boy","kilo","yas"])
print(sonuc2)
print()
cinsiyet=veriler.iloc[:,-1].values
print(cinsiyet)
print()
sonuc3=pd.DataFrame(data=cinsiyet,index=range(22),columns=["cinsiyet"])
print(sonuc3)
print()
#veri birleşimi
s=pd.concat([sonuc,sonuc2],axis=1)#concat sayesinde birleşme oldu
print(s)
print()
#birleşin birleşimi
s3=pd.concat([sonuc3],axis=0)
birleşim=pd.concat([s,s3],axis=1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(s,sonuc3,test_size=0.50,random_state=0)
from sklearn.preprocessing import StandardScaler
#öznitelik ölçekleme
sc=StandardScaler()#nesne oluştu
X_train=sc.fit_transform(x_train)#biribirine daha yakın yapmak için kulllanılıyor
X_test=sc.fit_transform(x_test)













