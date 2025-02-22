# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:48:30 2025

@author: Huzur Bilgisayar
"""

import pandas as pd
import numpy as np
veriler=pd.read_csv("C://Users//Huzur Bilgisayar//makine öğrenmesi//veriler.csv")
#print(veriler)
x=10
import math
class hesap_makinesi():
    def toplama(self,a,b):
        return a+b
    def çarpma(self,a,b):
        return a*b
    def bölme(self,a,b):
        return a/b
    def çıkarma(self,a,b):
        return a-b
    def üs_alma(self,a,b):
        return pow(a,b)
    def kare_kök(self,a):
        return math.sqrt(a)
    def mutlak_deger(self,b):
        return abs(b)
işlem=hesap_makinesi()
print("toplama=",işlem.toplama(5,6))
print("çarpım=",işlem.çarpma(9,8))
print("bölüm=",işlem.bölme(78,6))
print("çıkarma=",işlem.çıkarma(9,-1))
print("üs alınmış hali=",işlem.üs_alma(9,2))
print("a'nın karekök alınmış hali=",işlem.kare_kök(81))
print("a'nın karekök alınmış hali=",işlem.mutlak_deger(-12))