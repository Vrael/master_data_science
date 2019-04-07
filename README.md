# Descripción
Aplicación para detectar analizar los retrasos en las paradas de autobus de la EMT e identificar zonas con conflictos circulatorios

# Requisitos
Python 2.7.15

# Instalación
python pip install

# Ejecución
python .\dataframe.py

# Funcionamiento
1. Lectura del fichero EMT_tiempos_espera.txt
2. Cálculo de la diferencia entre tiempo real y tiempo estimado
3. Cálculo del porcentaje de desviación
4. Filtrado de las paradas que tienen retrasos
5. Agrupación de los datos por parda y retrasos diarios
6. Selección del 40% de las paradas que acumulan mayores retrasos
7. Cruze de datos con su geo-posición en el fichero EMT_coordenadas_paradas.txt
8. Escritura del fichero dataframe.txt para el análisis de cluster