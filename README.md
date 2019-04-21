# Descripción
Aplicación para detectar analizar los retrasos en las paradas de autobus de la EMT e identificar zonas con conflictos circulatorios

# Requisitos
Python 2.7.15

# Instalación
python pip install

# Ejecución

## Dataframe
python .\dataframe.py

## Kmeans
python .\kmeans_elbow.py

python .\kmeans_draw.py

# Funcionamiento

## Dataframe
1. Lectura del fichero EMT_tiempos_espera.txt
2. Cálculo de la diferencia entre tiempo real y tiempo estimado
3. Cálculo del porcentaje de desviación
4. Filtrado de las paradas que tienen retrasos
5. Agrupación de los datos por parda y retrasos diarios
6. Selección del 40% de las paradas que acumulan mayores retrasos
7. Cruze de datos con su geo-posición en el fichero EMT_coordenadas_paradas.txt
8. Escritura del fichero dataframe.txt para el análisis de cluster

## Kmeans
1. Carga de los valores "x", "y", "delay" desde el fichero dataframe.txt
2. Utilización de Kmeans para agrupar y obtener los clusters de paradas con comportamiento similar
3. Cálculo del número de clusters idoneo. Obtención del score del modelo y visualización del "codo" (elbow)
4. Alimentar el modelo Kmeans con los datos del dataframe.txt y utilizando la "k" (codo) obtenida
5. Dibujar los centroides de los 3 clusters con las paradas agrupadas a su alrededor