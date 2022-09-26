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
print(customer.astype(np.object).isnull().any())
print('---------------------')
#Anteriormente se hizo la verificación de valores faltantes, al parecer ninguna caracteristica clave tiene valores faltantes 
#los datos dupliplicados ahora se eliminan. 
# Acontinuación se comprueba las estadisticas del conjunto de datos
print('Conjuntos de datos de la información del cliente')
print(customer.describe())
print('-----------------------------')
print('Conjuntos de datos de la información de gastos mensuales')
print(spends_Month.describe())
print('-----------------------------')
print('Conjuntos de datos de la información de comprador de bicicletas')
print(buyer_bike.describe())
print('-----------------------------')
#Recuento de los valores unicos y devuelve la frecuencia relativa dividiendo todos los valores por la sumas de los valores. 
print(buyer_bike.BikeBuyer.value_counts(normalize=True))
print('-----------------------------')
#Se va unirá la columna del comprador de la bicicleta a la información del cliente para una tabla combinada. 
# Para el desafío de datos de prueba no se proporciona AveMonthSpend por lo tanto no es una característica viable.
print('Tabla convinada, columna del comprador de la bicicleta a la información del cliente')
combinar = customer.merge(buyer_bike, on='CustomerID', how='left')
print(combinar.head())