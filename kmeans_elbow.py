"""
********* Kmeans_elbow ************
Autores: 
Marc Aguilar de Llorens
Francisco Burgos Valdes

Descripcion:
Programa para dibujar la curva de valoracion del modelo, en funcion del numero de centroides y obtener el valor "de codo" a utlizar
Sklearn para poder aplicar Kmenas al dataframe
"""

# Dependencies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Cargar los valores del dataframe
dataframe = pd.read_csv(r"dataframe.txt", sep='\t')
dataframe.head()
print dataframe.describe()

# Estructura de datos para alimentar el algoritmo.
X = np.array(dataframe[["x","y", "delay"]])
X.shape

# Calcular el valor "k", el codo para Kmeans
Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
kmeans
score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]
score
plt.plot(Nc,score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()