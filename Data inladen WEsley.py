#importing the necessary libraries for the workflow.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

#Loading dataset into the workflow. 
    #`data` variable contains the whole dataset. 
    #`data_extracted_features` contains a subset of the whole dataset.

data = pd.read_excel("data/01. Master_Latest data_Control clones_LP.xlsx", engine='openpyxl', na_values=['', ' ', '\t', '\n'])
data_extracted_features = pd.read_excel("data/01. Master_Latest data_Control clones_LP.xlsx", usecols=['Batch number', 'Genotype Neuron', 'Div calculated', 'Culture treatment', 'Capacitance', 'Input Resistance', 'Resting membrane potential ', 'Maximum firing ', 'Calculated input resistance', 'Rheobase', 'EPSC freq'])
#data_extracted_features.head()
#data_extracted_features_nona = data_extracted_features.dropna()
print(data_extracted_features)  
#print(data_extracted_features['Batch number'].unique())
#print(data_extracted_features['Genotype Neuron'].unique()) 
#print(data_extracted_features['Div calculated'].unique())
#print(data_extracted_features['Culture treatment'].unique())
#print(data_extracted_features['Capacitance'].unique())
    #print(data_extracted_features['Input Resistance'].unique())
    #Een 'nan' in de kolom  
        #print(data_extracted_features[data_extracted_features['Input Resistance'] == 'nan'])
        #print(data_extracted_features['Input Resistance'].value_counts(ascending=True, dropna=True))    
#print(data_extracted_features['Resting membrane potential '].unique())
    #print(data_extracted_features['Maximum firing '].unique())
    #Een 'nan' in de kolom
        #print(data_extracted_features['Maximum firing '].value_counts())
        #print(data_extracted_features[data_extracted_features['Maximum firing '] == 'nan'])
    #print(data_extracted_features['Calculated input resistance'].unique())
    #Een 'nan' in de kolom
        #print(data_extracted_features['Calculated input resistance'].value_counts())
        #print(data_extracted_features[data_extracted_features['Calculated input resistance'] == 'nan'])
    #print(data_extracted_features['Rheobase'].unique())
        #Een 'nan' in de kolom
        #print(data_extracted_features['Rheobase'].value_counts())  
        #print(data_extracted_features[data_extracted_features['Rheobase'] == 'nan'])
    #print(data_extracted_features['EPSC freq'].unique())   
        #Ranges inputeren

# X_train, X_test= train_test_split(data_extracted_features, test_size=0.2, random_state=42)
# print(X_train)
# print(X_test)   

# sns.violinplot(data=data_extracted_features, x="Batch number", y="Genotype Neuron")
# sns.violinplot(data=data_extracted_features, x="Batch number", y="Div calculated")
# plt.xlabel("Batch number")
# plt.ylabel("Div calculated")
# plt.title("Ephys no na violinplot")
# plt.show()

# X_train, X_test= train_test_split(data_extracted_features, test_size=0.2, random_state=42)
# print(X_train)
# print(X_test)   

# pca = PCA(n_components=2)
# pca.fit(data_extracted_features)
