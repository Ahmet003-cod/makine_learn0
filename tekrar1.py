# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:42:51 2025

@author: Huzur Bilgisayar
"""
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer #veri doldurma kütüphanesi
from sklearn import preprocessing
veriler=pd.read_csv("C://Users//Huzur Bilgisayar//makine öğrenmesi//veriler.csv")
ulke=veriler.iloc[:,0:1].values
le=preprocessing.LabelEncoder()#nesne oluştu
ulke[:,0]=le.fit_transform(veriler.iloc[:,0])#harf sayisila çevirdi
ohe=preprocessing.OneHotEncoder()#binary nesnesi oluştu
ulke=ohe.fit_transform(ulke).toarray()
sonuc=pd.DataFrame(data=ulke,index=range(22),columns=["tr","fr","us"])
print(sonuc)
yas=veriler.iloc[:,1:4]
imputer=SimpleImputer(missing_values=np.nan,strategy="median")
yas[:]=imputer.fit_transform(yas)
print(yas)
sonuc1=pd.DataFrame(data=yas,index=range(22),columns=["boy","kilo","yas"])
cinsiyet=veriler.iloc[:,-1].values
print(cinsiyet)
sonuc2=pd.DataFrame(data=cinsiyet,index=range(22),columns=["cinsiyet"])
brl=pd.concat([sonuc,sonuc1,sonuc2],axis=1)
print(brl)