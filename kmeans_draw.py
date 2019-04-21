"""
********* Kmeans_draw ************
Autores: 
Marc Aguilar de Llorens
Francisco Burgos Valdes

Descripcion:
Programa para dibujar los diferentes clusters de paradas en funcion de sus tiempos de espera
Sklearn con Kmeans para agrupar y obtener los centroides
Matplotlib para dibujar los graficos en 2D
"""

# Dependencies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Prepare los graficos donde mostrar los resultados
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

# Leer los valores del fichero de dataframe
dataframe = pd.read_csv(r"dataframe.txt", sep='\t')
dataframe.head()
print dataframe.describe()

# Estructura de datos para alimentar el algoritmo.
X = np.array(dataframe[["x","y","delay"]])
#y = np.array(dataframe['delay'])
print X.shape

# Ejecucion de Kmeans para obtener los centroides. K=3, obtenido mediante kmeans_elbow.py 
kmeans = KMeans(n_clusters=3).fit(X)
labels = kmeans.predict(X)
C = kmeans.cluster_centers_

# Grafico para dibuujar los 3 centroides
colores=['red','green','blue']
asignar=[]
for row in labels:
    asignar.append(colores[row])

 # Obtener valores para dibujarlos entorno los centroides obtenidos
fig = plt.figure()
f1 = dataframe['x'].values
f2 = dataframe['y'].values
 
# Algoritmo de K-Means con K=3. Las 22 paradas en funcion de las coordenadas X,Y, agrupadas por delay
print C[:,2] 
plt.scatter(f1, f2, c=asignar, s=70)
plt.scatter(C[:, 0], C[:, 1], marker='*', c=colores, s=1000)
plt.show()


