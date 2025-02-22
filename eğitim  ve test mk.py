# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:15:10 2025

@author: Huzur Bilgisayar
"""

import pandas as pd 
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
veriler=pd.read_csv("C://Users//Huzur Bilgisayar//makine öğrenmesi//veriler.csv")
from sklearn.model_selection import train_test_split


# 1️⃣ Örnek veri kümesi oluşturalım
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]  # Bağımsız değişkenler (Özellikler)
Y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]           # Bağımlı değişkenler (Hedef değerler)

# 2️⃣ Veriyi eğitim (%70) ve test (%30) olarak ayıralım
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.30, random_state=0)

# 3️⃣ Sonuçları ekrana yazdıralım
print("Eğitim Verisi (X_train):", X_train)#eğitim bağımsız değişken
print("Eğitim Etiketleri (Y_train):", Y_train)
print("Test Verisi (X_test):", X_test)
print("Test Etiketleri (Y_test):", Y_test)

