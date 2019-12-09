# -*- coding: utf-8 -*-"""

# Hierarchical Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/media/abh/NEW/BTECH/DWDM/Assignment 5/iris.csv')
X = dataset.iloc[:,0:4].values
y = dataset.iloc[:,[4]].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Using the dendrogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram Plotter')
plt.xlabel('Petals/Sepals')
plt.ylabel('Euclidean distances')
plt.show()

# Fitting Hierarchical Clustering to the dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

for i in range(0,len(y_hc)):
    if y_hc[i]==1:
        y_hc[i]=0
    elif y_hc[i]==0:
        y_hc[i]=1
    
#y_hc=labelencoder_y.transform(y_hc)
# Visualising the clusters
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.legend()
plt.show()

from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y, y_hc)
accuracy = accuracy_score(y, y_hc)
print("Hierarchical Clustering accuracy")
print(accuracy)
print("Hierarchical Clustering matrix")
print(cm)
