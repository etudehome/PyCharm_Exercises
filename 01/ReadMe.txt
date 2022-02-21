####### Dokumentation  ############

#Inhaltsverzeichnis:
1. Projektbeschreibung 
2. Installation der Software
3. Inhalte
4. Installation der Module
5. "Run" Programm
6. Fehlerbehandlung

## 1. Projektbeschreibung:
Das Projekt beschäftigt sich mit der Visualisierung der Arbeitslosigkeit mithilfe einer Weltkarte. 
Ziel ist es einen Überblick über die Arbeitslosigkeit weltweit zu schaffen. Andere visuelle Darstellungen, wie Linien- und Balkendiagramme verschaffen dem Betrachter 
verschaffen dem Betrachter eine detaillierte Ansicht der Arbeitslosigkeit in den Ländern, aber nur auf eine begrenzte Anzahl an Ländern. Als Ergänzung hierfür 
soll das Projekt als Ergänzung dazu dienen und eine Ansicht aller Länder anhand einer Weltkarte verschaffen. Zudem sollen zwei Arten von Darstellungen verglichen 
werden um den passenden Plot für die Thematik zufinden. 

## 2. Installation der Software
:
Für die Verwendung des Code wird mind. Python 3.3 benötigt. Für das Projekt wurde Anaconda,Pycharm installiert und verwendet. 


## 3. Inhalte:

Daten:
	- WDIData.csv (aus https://ourworldindata.org/)
	- CNTR_LB_2020_4326.geojson (aus https://ec.europa.eu/eurostat/data/database)


Softwarecode:
	- Projekt_Elibol.py
	- der Code enthält eine reihenweise Beschreibung 

## 4. Installation 


Benötigte Module: 
	- import json
	- import csv
	- import pandas as pd
	- import plotly.graph_objs as go
	- import plotly.io as pio
	- import tkinter as tk
	- from tkinter.filedialog import askopenfilename
	- import plotly.offline as py
	- from plotly.graph_objs import *
	- import matplotlib.pyplot as plt
	- import cartopy
	- import cartopy.crs as ccrs
	- import mplcursors


## 5. "Run" Program

Nach der Installation von Pycharm kann der Code mit den Daten geladen werden. 


	Code Beispiel:


	arbeit = pd.read_csv("--Pfad/WDIData.csv")
	arbeit = arbeit.loc[arbeit["Indicator Name"] == 'Unemployment, total (% of total labor force) (national estimate)']
	arbeit = arbeit.iloc[49:]

	Output:

	               Country Code   2005   2017
	73552          Albania  ALB  14.10  13.62
	74995          Algeria  DZA  15.27  13.57
	82210        Argentina  ARG  11.51   8.35
	86539        Australia  AUS   5.03   5.59
	87982          Austria  AUT   5.63   5.50
	...                ...  ...    ...    ...
	350608  United Kingdom  GBR   4.75   4.33
	352051   United States  USA   5.08   4.36
	353494         Uruguay  URY  12.01   7.89
	354937      Uzbekistan  UZB   0.30   5.80
	362152          Zambia  ZMB  15.90  11.63

	[89 rows x 4 columns]
     	             	   Country Code   2005   2017
	340507                Turkey  TUR  10.64  10.82
	346279                Uganda  UGA   1.90  10.09
	347722               Ukraine  UKR   7.18   9.50
	349165  United Arab Emirates  ARE   3.12   2.46
	350608        United Kingdom  GBR   4.75   4.33
	352051         United States  USA   5.08   4.36
	353494               Uruguay  URY  12.01   7.89
	354937            Uzbekistan  UZB   0.30   5.80
	362152                Zambia  ZMB  15.90  11.63


## 6.Fehlerbehandlung

Es sind keine Fehler bekannt. 

## 7.Maintainers

Nesibe Elibol (elibol.nesibe@gmail.com)









