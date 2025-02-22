# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:25:40 2025"""
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer#eksik verileri doldurmak için kullanılır
veriler=pd.read_csv("C://Users//Huzur Bilgisayar//makine öğrenmesi//veriler.csv")
#ayrı ayrı verilere ayırma ekleme
veriler.loc[10,"yas"]=10
veriler.loc[15,"yas"]=56
veriler.loc[20,"yas"]=20
#veri ekleme
veriler.loc[22,"ulke"]="jb"
veriler.loc[22,"cinsiyet"]="k"
veriler.loc[22,"boy"]=175
veriler.loc[22,"kilo"]=78
veriler.loc[22,"yas"]=90

# Eksik verileri içeren örnek veri
data = np.array([[1, 2, np.nan], 
                 [5, np.nan, 3], 
                 [4, 6, 9]])
# Ortalama ile eksik değerleri dolduran imputer nesnesi
imputer=SimpleImputer(strategy="mean")#eksik verilerin ortalamasini alniyor
imputer=SimpleImputer(strategy="median")#eksik verelerin ortancası alınması
imputer=SimpleImputer(strategy="most_frequent")#eksik verelerin en çok tekrarın alınması
# Veriyi dönüştürme (eksik değerleri doldurma)
veri_letimi=imputer.fit_transform(data)
print(veri_letimi)
#csv veri eksiği
yas=veriler.iloc[:,1:4]
print(veriler)
imputer=SimpleImputer(missing_values=np.nan,strategy="median")#ortanca

imputer=SimpleImputer(missing_values=np.nan,strategy="mean")#Art ortalama

imputer=SimpleImputer(missing_values=np.nan,strategy="constant",fill_value=60)#<sabit

yas[:]=imputer.fit_transform(yas)
print(yas)


