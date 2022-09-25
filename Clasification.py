import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.random as nr
import math

#Leer DataSets
customer = pd.read_csv('./BD/AdvWorksCusts.csv')
spends_Month = pd.read_csv('./BD/AW_AveMonthSpend.csv')
buyer_bike = pd.read_csv('./BD/AW_BikeBuyer.csv')

#De aquí en adelante haremos una limpiza de datos

#Eliminar Datos duplicados 
print('Duplicados BD información del Cliente')
print(customer.shape)
print(customer.CustomerID.unique().shape)
print('---------------------')
customer.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)
print(customer.shape)
print(customer.CustomerID.unique().shape)

print('Duplicados BD Gastos Mensuales')
print(spends_Month.shape)
print(spends_Month.CustomerID.unique().shape)
print('---------------------')
spends_Month.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)
print(spends_Month.shape)
print(spends_Month.CustomerID.unique().shape)

print('Duplicados BD Comprador Bicicletas')
print(buyer_bike.shape)
print(buyer_bike.CustomerID.unique().shape)
print('---------------------')
buyer_bike.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)
print(buyer_bike.shape)
print(buyer_bike.CustomerID.unique().shape)
print('---------Datos Faltantes------------')
#Comprobación de datos faltantes 
print(buyer_bike.astype(object).isnull().any())
print('---------------------')
print(buyer_bike.astype(object).isnull().any())
print('---------------------')
print(customer.astype(object).isnull().any())