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
dat2 = dat.loc[:,['Milepost','DateTime','TotVeh','Direction']].copy()
dat2.head()
HeatMapDat=dat2[dat2.Direction=='D'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(12,10)})
fig1,sns_plot1=plt.subplots()
sns_plot1=sns.heatmap(HeatMapDat,cmap='YlOrRd')
sns_plot1.set_title("Westbound (Decreasing Milepost)")
sns_plot1.set_xticklabels(sns_plot1.get_xticklabels(), rotation=30)
sns_plot1.set_yticklabels(sns_plot1.get_yticklabels(), rotation=30)
fig1.savefig('Z:/apoorb/WBHeatMapVol.png')


HeatMapDat=dat2[dat2.Direction=='I'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(12,10)})
fig2, sns_plot2=plt.subplots()
sns_plot2=sns.heatmap(HeatMapDat,cmap='YlOrRd')
sns_plot2.set_title("Eastbound (Increasing Milepost)")
sns_plot2.set_xticklabels(sns_plot2.get_xticklabels(), rotation=30)
sns_plot2.set_yticklabels(sns_plot2.get_yticklabels(), rotation=30)
fig2.savefig('Z:/apoorb/EBHeatMapVol.png')


HeatMapDat=dat2[dat2.Direction=='B'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(12,10)})
fig3,sns_plot3=plt.subplots()
sns_plot3=sns.heatmap(HeatMapDat,cmap='YlOrRd')
sns_plot3.set_title("Both Direction")
sns_plot3.set_xticklabels(sns_plot3.get_xticklabels(), rotation=30)
sns_plot3.set_yticklabels(sns_plot3.get_yticklabels(), rotation=30)
fig3.savefig('Z:/apoorb/WBEBHeatMapVol.png')





HeatMapDat.index.value_counts()
#********************************************************************#
start_date = '2018-02-01'
end_date = '2018-02-07'
mask =(dat['DateTime']>start_date) & (dat['DateTime']<=end_date)
dat3 = dat.loc[mask,['Milepost','DateTime','TotVeh','Direction']].copy()
HeatMapDat=dat3[dat3.Direction=='D'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(12,10)})
fig4,sns_plot4=plt.subplots()
sns_plot4=sns.heatmap(HeatMapDat,cmap='YlOrRd')
sns_plot4.set_title("Westbound (Decreasing Milepost)")
sns_plot4.set_xticklabels(sns_plot4.get_xticklabels(), rotation=30)
sns_plot4.set_yticklabels(sns_plot4.get_yticklabels(), rotation=30)
fig4.savefig('Z:/apoorb/WBHeatMapVol_7Days.png')


HeatMapDat=dat3[dat3.Direction=='I'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(12,10)})
fig5, sns_plot5=plt.subplots()
sns_plot5=sns.heatmap(HeatMapDat,cmap='YlOrRd')
sns_plot5.set_title("Eastbound (Increasing Milepost)")
sns_plot5.set_xticklabels(sns_plot5.get_xticklabels(), rotation=30)
sns_plot5.set_yticklabels(sns_plot5.get_yticklabels(), rotation=30)
fig5.savefig('Z:/apoorb/EBHeatMapVol_7Days.png')


HeatMapDat=dat3[dat3.Direction=='B'].pivot('Milepost','DateTime','TotVeh')
#HeatMapDat_NP=np.array(HeatMapDat)
#HeatMapDat_NP[:,:200].shape
#HeatMapDat_NP=np.random.rand(10,12)
sns.set(rc={'figure.figsize':(12,10)})
fig6,sns_plot6=plt.subplots()
sns_plot6=sns.heatmap(HeatMapDat,cmap='YlOrRd')
sns_plot6.set_title("Both Direction")
sns_plot6.set_xticklabels(sns_plot6.get_xticklabels(), rotation=30)
sns_plot6.set_yticklabels(sns_plot6.get_yticklabels(), rotation=30)
fig6.savefig('Z:/apoorb/WBEBHeatMapVol_7Days.png')




#HeatMapDat=dat2[dat2.Direction=='WB'].pivot('Milepost','DateTime','TotVeh')
##HeatMapDat_NP=np.array(HeatMapDat)
##HeatMapDat_NP[:,:200].shape
##HeatMapDat_NP=np.random.rand(10,12)
#sns.set(rc={'figure.figsize':(100,20)})
#sns_plot=sns.heatmap(HeatMapDat,cmap='YlOrRd',linewidths=0.5)
#fig = sns_plot.get_figure()
#fig.savefig('Z:/apoorb/WBHeatMapVol_7Days.jpg')
#plt.show()
#
#
#HeatMapDat=dat2[dat2.Direction=='EB'].pivot('Milepost','DateTime','TotVeh')
##HeatMapDat_NP=np.array(HeatMapDat)
##HeatMapDat_NP[:,:200].shape
##HeatMapDat_NP=np.random.rand(10,12)
#sns.set(rc={'figure.figsize':(100,20)})
#sns_plot=sns.heatmap(HeatMapDat,cmap='YlOrRd',linewidths=0.5)
#fig = sns_plot.get_figure()
#fig.savefig('Z:/apoorb/EBHeatMapVol_7Days.jpg')
#plt.show()
#

#
#
##********************************************************************#
#sns.set(rc={'figure.figsize':(12,8)})
#(Series(dat[dat.deviceId==384].TotVeh)).plot()
#plt.xticks(rotation=45)
#plt.style.use('seaborn-darkgrid')
#plt.show()
##ax.set_xlim('2018-02-01 00:00:00','2018-02-28 00:00:00')
#
#maskA = (dat.Direction=='I') & (dat.DateTime=='2018-02-01 09:00:00')
#sns.lineplot(y='TotVeh',x='Milepost',data=dat[maskA])
#plt.xticks(rotation=45)
#plt.style.use('seaborn-darkgrid')
#plt.show()
