# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 22:44:03 2025
@author: Huzur Bilgisayar
"""
import pandas as pd 
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
veriler=pd.read_csv("C://Users//Huzur Bilgisayar//makine öğrenmesi//veriler.csv")#veri adresi windows
from sklearn.preprocessing import LabelEncoder

# Kategorik veriler (Ülkeler)
ulkeler = ["TR", "US", "FR", "DE", "TR", "US", "FR"]

# LabelEncoder nesnesini oluştur
le = LabelEncoder()

# Veriyi sayılara çevir
encoded_ulkeler = le.fit_transform(ulkeler)

print(encoded_ulkeler)

#japonyayıda ekledik
veriler.loc[22,"ulke"]="jb"
veriler.loc[22,"cinsiyet"]="k"
veriler.loc[22,"boy"]=175
veriler.loc[22,"kilo"]=78
veriler.loc[22,"yas"]=90

ulke=veriler.iloc[:,0:1].values#(Ülke sütunu) seçiyor ve NumPy dizisine çeviriyor.
print(ulke)

ln=preprocessing.LabelEncoder()#LabelEncoder, kategorik verileri sayıya dönüştürür
ulke[:,0]=ln.fit_transform(veriler.iloc[:,0])
ohe=preprocessing.OneHotEncoder()#bunları binary (0 ve 1) formatına çevireceğiz.
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)