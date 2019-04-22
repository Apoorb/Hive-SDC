# -*- coding: utf-8 -*-
"""
Spyder Editor

Develop Heatmap, surface and timeseries plot
"""
import pandas as pd
from pandas import Series
from matplotlib import pyplot as plt
import boto3 #Need to read and write files to aws s3 bucket
from io import BytesIO as StringIO 
import numpy as np
import seaborn as sns

#Data I got from a Report
client=boto3.client('s3')
obj=client.get_object(Bucket='prod-sdc-tti-911061262852-us-east-1-bucket',Key='abibeka/Data/MergeRwisVolDat.csv')
dat=pd.read_csv(obj['Body'])
dat=dat.drop(columns='Unnamed: 0')
dat.head()

#********************************************************************#
sns.set(rc={'figure.figsize':(12,8)})
(Series(dat[dat.deviceId==396].TotVeh)).plot()
plt.xticks(rotation=45)
plt.style.use('seaborn-darkgrid')
plt.show()
#ax.set_xlim('2018-02-01 00:00:00','2018-02-28 00:00:00')

maskA = (dat.Direction=='EB') & (dat.DateTime=='2018-02-01 09:00:00')
sns.lineplot(y='TotVeh',x='Milepost',data=dat[maskA])
plt.xticks(rotation=45)
plt.style.use('seaborn-darkgrid')
plt.show()
#********************************************************************#
dat2 = dat.loc[:,['Milepost','DateTime','TotVeh','Direction']].copy()
dat2.head()
HeatMapDat=dat2[dat2.Direction=='WB'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(100,40)})
sns_plot=sns.heatmap(HeatMapDat,cmap='YlOrRd')
fig = sns_plot.get_figure()
fig.savefig('Z:/apoorb/WBHeatMapVol.jpg')
plt.show()


HeatMapDat=dat2[dat2.Direction=='EB'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(100,40)})
sns_plot=sns.heatmap(HeatMapDat,cmap='YlOrRd')
fig = sns_plot.get_figure()
fig.savefig('Z:/apoorb/EBHeatMapVol.jpg')


#********************************************************************#
start_date = '2018-02-01'
end_date = '2018-02-07'
mask =(dat['DateTime']>start_date) & (dat['DateTime']<=end_date)
dat2 = dat.loc[mask,['Milepost','DateTime','TotVeh','Direction']].copy()
dat2.head()
HeatMapDat=dat2[dat2.Direction=='WB'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(100,20)})
sns_plot=sns.heatmap(HeatMapDat,cmap='YlOrRd',linewidths=0.5)
fig = sns_plot.get_figure()
fig.savefig('Z:/apoorb/WBHeatMapVol_7Days.jpg')
plt.show()


HeatMapDat=dat2[dat2.Direction=='EB'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(100,20)})
sns_plot=sns.heatmap(HeatMapDat,cmap='YlOrRd',linewidths=0.5)
fig = sns_plot.get_figure()
fig.savefig('Z:/apoorb/EBHeatMapVol_7Days.jpg')
plt.show()

