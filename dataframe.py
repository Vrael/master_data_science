#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
## Genera un dataframe con los tiempos medios extremos de espera por         ##
## cada parada                                                               ##
###############################################################################

import pandas as pd
import numpy as np

def calculateMaxWaittingBusStops():
	print("\nCalcula diff = estimateWait - realWait. Negativo significa retraso en la parada\n")
	df = pd.read_csv('.\EMT_tiempos_espera.txt', delimiter='\t', comment='#', names=['stop', 'line', 'hour', 'realWait', 'estimateWait'])
	df['delay'] = df['realWait'] - df['estimateWait']
	df['%desviation'] = 100 * (df['estimateWait'] - df['realWait']) / df['estimateWait']
	print(df)
	
	print("\n########################################")
	print("\nSe filtran para dejar solo los retrasos.\n")
	delay = df['delay'] > 0
	print(df[delay])
	
	print("\n########################################")
	print("\nSe agrupan las desviaciones por dia.\n")
	df2 = df[delay].groupby(['stop'], sort=False)[['delay']].sum()
	print(df2)
	
	print("\n########################################")
	count = df2.count()					# total rows grouped by bus stop
	count40 = int(round(40*count/100,0))# 40%
	print("\nSe selecciona el 40% (" + str(count40) + " paradas) con los retrasos mayores\n")
	df3 = df2.nlargest(count40, 'delay')
	print(df3)
	
	print("\n########################################")
	print("\nSe cruza el resultado con las coordenadas de las paradas\n")
	df4 = pd.read_csv('.\EMT_coordenadas_paradas.txt', delimiter='\t', comment='#', names=['stop', 'x', 'y', 'description'])
	merged = df3.merge(df4, on='stop', how='inner')
	print(merged)
	
	del merged['description']
	merged.to_csv('.\dataframe.txt', sep='\t', index=False)

def main():
	calculateMaxWaittingBusStops()

if __name__== "__main__":
  main()
