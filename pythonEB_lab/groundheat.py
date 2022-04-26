# -*- coding: utf-8 -*-
"""Groundheat.ipynb



Equation is $Q_g = k_g (dTg)/dz$   or


$Q_g = kg(T_g - T_{sb})/(z_2 - z_1)$

where

$Q_g$ = soil heat conduction flux density ($Wm^{-2}$)

$k_g$ = thermal conductivity of soil, $W m^{-1} ºC^{-1}$

$T_g$ = soil temperature at depth $z_2, ºC$

$T_{sb}$ = soil temperature at depth $z_1 = 0m, ºC$

$z$ = soil depth (m)


"""

# Qg = kg(Tg - Tsb)/(z2 - z1)

# Set up all variables

kg = 2  # This is assumed and will be verified later. Units are (Wm^{-2})
z = 0.1 # Depth of teh sensor in meters

import pandas as pd
import datetime

df = pd.read_csv('CENMET_INPUT_data.csv')
dfIn = df # save a backup

mapping = {dfIn.columns[0]:'year', df.columns[1]: 'month', df.columns[2]:'day', df.columns[3]: 'hour'}
dfIn = dfIn.rename(columns=mapping)
dfIn

# add date time
dfIn['date'] = pd.to_datetime(dfIn[['year', 'month', 'day', 'hour']], format = '%Y/%M/%D %H')

dfIn

N = 11
# Drop first N columns of dataframe
dfIn = dfIn.iloc[: , N:]
dfIn = dfIn.set_index('date')
dfIn.drop(dfIn.columns[[1]], axis = 1, inplace = True) # Drop melt
dfIn.rename(columns = {' soilTemp_10cm':'soilTemp_10cm'}, inplace = True) # there is a space in the column name.
dfIn

#Qg = kg(Tg - Tsb)/(z2 - z1)

dfIn['Qg'] = kg*(dfIn.soilTemp_10cm)/(z) # assume Tg is zero degrees


Qg_out = dfIn

Qg.dtypes

import matplotlib.pyplot as plt
import seaborn as sns


sns.lineplot(data=Qg_out.soilTemp_10cm, color="g")
ax2 = plt.twinx()
sns.lineplot(data=Qg_out.Qg, color="b", ax=ax2)
ax2.invert_yaxis()
