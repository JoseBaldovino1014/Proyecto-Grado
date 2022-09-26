import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.random as nr
import math

# load datasets
custs= pd.read_csv('./data/AdvWorksCusts.csv')
spend_Month = pd.read_csv('./data/AW_AveMonthSpend.csv')
buyer_bike = pd.read_csv('./data/AW_BikeBuyer.csv')

# remove duplicates AdvWorksCusts.csv

print(custs.shape)
print(custs.CustomerID.unique().shape)
custs.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)
print(custs.shape)
print(custs.CustomerID.unique().shape)

# remove duplicates AW_AveMonthSpend.csv
print(spend_Month.shape)
print(spend_Month.CustomerID.unique().shape)
spend_Month.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)
print(spend_Month.shape)
print(spend_Month.CustomerID.unique().shape)

# remove duplicates AW_BikeBuyer
print(buyer_bike.shape)
print(buyer_bike.CustomerID.unique().shape)
buyer_bike.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)
print(buyer_bike.shape)
print(buyer_bike.CustomerID.unique().shape)

# check for missing values
print(buyer_bike.astype(np.object).isnull()).any()
print(spend_Month.astype(np.object).isnull()).any()
print(custs.astype(np.object).isnull()).any()