# Dependencies
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import pandas as pd

# Prepare the graphics where we will display the results
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Read and load the dataframe values
dataframe = pd.read_csv(r"dataframe.txt", sep='\t')
dataframe.head()
print dataframe.describe()

# Estructura de datos para alimentar el algoritmo.
X = np.array(dataframe[["x","y","delay"]])
#y = np.array(dataframe['delay'])
X.shape

# Ejecucion de Kmeans para obtener los centroides. K=3, obtenido mediante kmeans_elbow.py
kmeans = KMeans(n_clusters=3).fit(X)
labels = kmeans.predict(X)
C = kmeans.cluster_centers_

# Grafico para dibuujar los centroides
colores=['red','green','blue']
asignar=[]
for row in labels:
    asignar.append(colores[row])

 # Obtener valores y dibujarlos entorno los centroides obtenidos
fig = plt.figure()
f1 = dataframe['x'].values
f2 = dataframe['y'].values
 
plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
plt.show()
