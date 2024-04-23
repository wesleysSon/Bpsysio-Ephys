#imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Loading dataset into the workflow. 
    #`data` variable contains the whole dataset. 
    #`data_extracted_features` contains certain from the whole dataset.

data = pd.read_excel("data/01. Master_Latest data_Control clones_LP.xlsx", engine='openpyxl')
data_extracted_features = pd.read_excel("data/01. Master_Latest data_Control clones_LP.xlsx", usecols=['Batch number', 'Genotype Neuron', 'Div calculated', 'Culture treatment', 'Capacitance', 'Input Resistance', 'Resting membrane potential ', 'Maximum firing ', 'Calculated input resistance', 'Rheobase'])
#data_extracted_features.head()
data_extracted_features_nona = data_extracted_features.dropna()
#print(data_extracted_features.dropna())

sns.violinplot(data=data_extracted_features_nona, x="Batch number", y="Div calculated")
plt.xlabel("Batch number")
plt.ylabel("Div calculated")
plt.title("Ephys no na violinplot")
plt.show()
