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

print("Loading data...")
data = pd.read_excel("data/01. Master_Latest data_Control clones_LP.xlsx", engine='openpyxl')
data_extracted_features = pd.read_excel("data/01. Master_Latest data_Control clones_LP.xlsx", usecols=['Batch number', 'Genotype Neuron', 'Div calculated', 'Culture treatment', 'Capacitance', 'Input Resistance', 'Resting membrane potential ', 'Maximum firing ', 'Calculated input resistance', 'Rheobase', 'EPSC freq'])
#data_extracted_features.head()
# print("Loading violinplot...")
# sns.violinplot(data=data_extracted_features, x="Batch number", y="Div calculated")
# plt.xlabel("Batch number")
# plt.ylabel("Div calculated")
# plt.title("Ephys no na violinplot")
# plt.show()

#voor en na preproceesing distributie van de data bekijken. 
# Plot data (per feature) distributie voor en na om te kijken hoe je impute method invloed heeft op de data.  
# glm 

print("Preprocessing data...")
print(data_extracted_features)  
#data_extracted_features = data_extracted_features.dropna()
print(data_extracted_features)  
range_filter = data_extracted_features[data_extracted_features['EPSC freq'].str.contains('>') == True]     
data_extracted_features = data_extracted_features.drop(range_filter.index)
print(data_extracted_features)  

print("Splitting data...")
X_train, X_test= train_test_split(data_extracted_features, test_size=0.2, random_state=51)
#print(X_train)
#print(X_test)   

print("Loading violinplot...")
# kwartielen erin plotten
# sns.violinplot(data=data_extracted_features, x="Batch number", y="Genotype Neuron")
sns.violinplot(data=data_extracted_features, x="Batch number", y="Div calculated")
plt.xlabel("Batch number")
plt.ylabel("Div calculated")
plt.title("Ephys no na violinplot")
# plt.show()


# print("Loading scatterplot...")
# g = sns.FacetGrid(data_extracted_features, col="Batch number", hue="Genotype Neuron")
# g.map(sns.scatterplot, "", "Div calculated", alpha=.7)
# g.add_legend()
# plt.show()    

# sns.scatterplot(data=data_extracted_features, x="Batch number", y="Div calculated", hue="Genotype Neuron")           
# plt.show()  
# pca = PCA(n_components=2)
# pca.fit(data_extracted_features)
