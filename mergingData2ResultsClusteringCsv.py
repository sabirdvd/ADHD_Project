# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 01:14:40 2016

@author: and_ma
"""

import pandas as pd
import os
import re
import numpy as np

import matplotlib.pyplot as plt
path = "/Users/and_ma/Documents/DataScience/UB_DataScience/DataScience_Project/gitHub/last_sabadoGMM/"

df_A = pd.read_csv(path+"Apatients.csv")
df_B = pd.read_csv(path+"Bpatients.csv")
df_C = pd.read_csv(path+"Cpatients.csv")

df_A['experiment']='A'
df_B['experiment']='B'
df_C['experiment']='C'

df_merge = pd.concat([df_A,df_B,df_C])
df_merge.sort_values(by='patientName', ascending= True, inplace=True) # Dataframe is sorted by cluster type: 0 or 1
df_merge = df_merge.reset_index(drop = True)


#path_data = '/Users/and_ma/Documents/DataScience/UB_DataScience/DataScience_Project/gitHub/'
#train = pd.read_csv(path_data+'supervisedLearningDataSet.csv')

path_gmm = "/Users/and_ma/Documents/DataScience/UB_DataScience/DataScience_Project/gitHub/last_sabadoGMM/gmm/"
## 1. Loading gmm clustering results dataframe
patternFile = r'[\w]+\.csv'


filenames =  filenames = os.listdir(path_gmm)
df_gmm = []
for experiment in filenames:
    if re.match(patternFile,experiment) != None:
        df_temp = pd.read_csv(path_gmm+experiment)
        df_gmm.append(df_temp)        
df_gmm = pd.concat(df_gmm)
df_gmm.sort_values(by='patientName', ascending= True, inplace=True) # Dataframe is sorted by cluster type: 0 or 1
df_gmm = df_gmm.reset_index(drop = True)


#df_gmm.cluster.hist()
df_merge['GMM'] = df_gmm['cluster']
df_merge['patientsGMM'] = df_gmm['patientName']
#df_merge[['patientName','norm64comp_PCA_x','norm64comp_PCA_y']].head()
#df_gmm[['patientName','PCA_x','PCA_y']].head()
df_results =pd.DataFrame({})
df_results = df_merge[['patientName','experiment']]
df_results['cluster_GMM'] = df_gmm['cluster']
df_results['cluster_Hierarchichal'] = df_merge['norm64hierarchical']
df_results['cluster_Kmeans'] = df_merge['norm64kmeans++']
df_results['cluster_Spectral'] = df_merge['norm64spectral']
df_results['PCA_X'] = df_merge['norm64comp_PCA_x']  
df_results['PCA_Y'] = df_merge['norm64comp_PCA_y']

#gmm_cluster = lambda x: 0 if x == 1  else 1
#df_results['cluster_GMM']=df_results['cluster_GMM'].apply(gmm_cluster)

#kmeans_cluster = lambda x: 1 if x == 0 else 0
#df_results['cluster_GMM']=df_results['cluster_GMM'].apply(gmm_cluster)
#df_results['cluster_Kmeans']=df_results['cluster_Kmeans'].apply(kmeans_cluster)

list_clustering = ['cluster_GMM','cluster_Kmeans','cluster_Hierarchichal','cluster_Spectral']
df_results[['cluster_GMM','cluster_Kmeans','cluster_Hierarchichal','cluster_Spectral']].hist()


def mostCommon(df,list_clustering):
    best = []    
    for i in range(df.shape[0]):
        dicc = {'k1':0,'k0':0}
        for j in list_clustering:
            key = 'k'+str(df.loc[i][j])
            dicc[key]+=1
        if dicc['k1']>dicc['k0']:
            best.append(1)
        else:
            best.append(0)    
    return best 

def solapamiento(array1,array2):
    
    return 0
    

def plotCluster_tSNE(data,labels):
    
    
    return 0    

col_best = mostCommon(df_results,list_clustering)    
df_results['Best_Cluster']=np.array(col_best)


## Saving dataframe
#filename = 'resultsClustering.csv'
#if not os.path.exists(filename):
#    df_results.to_csv(filename, sep=',', encoding='utf-8')


