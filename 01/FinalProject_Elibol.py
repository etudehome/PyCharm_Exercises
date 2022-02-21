
### Nesibe Elibol ##############################################
### Programmieren mit Python ###################################

# --- Installation der benötigten Module --------#
import json
import csv
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
import tkinter as tk
from tkinter.filedialog import askopenfilename

import plotly.offline as py
from plotly.graph_objs import *
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import mplcursors

########################################################################################################
#-- Öffnen der CSV-Datei mit dem Dateipfad
arbeit = pd.read_csv("C:/Users/elibo/PycharmProjects/pythonProject2/WDIData.csv")

#-- Datenvorbereitung bzw. -bereinigung -------------#
arbeit = arbeit.loc[arbeit["Indicator Name"] == 'Unemployment, total (% of total labor force) (national estimate)']

#-- Länder beginnen ab der Reihe 49, Unwesentliches entfernen
arbeit = arbeit.iloc[49:]

#-- DataFrame auf die wesentlichen Variablen subsetten
arbeit.isnull().sum()
arbeit = arbeit[["Country", "Code", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]]
df = arbeit.dropna()

#-- Umwandlung des Datensatzes von Wide- to Long-Format! Notwendig für den Slider!
df_long = pd.melt(df, id_vars=['Country', "Code"], var_name='year', value_name='unemployment')


#-------------------------------- Erstellung des Plots --------------------------------------------------#
#-- Erstellung eines Choropleth

data_slider = []
for year in df_long["year"].unique():
    df_long2 = df_long[(df_long["year"] == year)]
    data = dict(
        type='choropleth',
        locations=df_long2['Country'],
        z=df_long2['unemployment'],
        locationmode='country names',
        colorscale="jet",
        text='</br>Arbeitslosenquote liegt bei ' + df_long2['unemployment'].astype(str),
        marker=dict(
            line=dict(color='rgb(255,255,255)', width=1)),
        colorbar=dict(title="Arbeitslosigkeit in Prozent,"))
    data_slider.append(data)

steps = []
for i in range(len(data_slider)):
    step = dict(method='restyle',
                args=['visible', [False] * len(data_slider)],
                label='Jahr {}'.format(i + 2010))
    step['args'][1][i] = True
    steps.append(step)
sliders = [dict(active=0, steps=steps)]
layout = dict(title="<br>Arbeitslosenquote weltweit von 2010 bis 2018",
              geo=dict(scope='world', projection={'type': 'natural earth'}), sliders=sliders)

fig = dict(data=data_slider, layout=layout)
py.iplot(fig, filename="file.html")

############################################################################################################
#---------------- Erstellung einer World Map mit cartopy und json-Datei -----------------------------------

root = tk.Tk()
fname = tk.StringVar()

#---- Definieren einer Funktion für den Scatter Plot -----------------------#
def myplot():
    # Öffnen der json- Datei
    with open(fname.get(), encoding="utf8") as f:
        world = json.load(f)

    lons, lats, ids = [], [], []
    for wo in world["features"]:
        lon = wo["geometry"]["coordinates"][0]
        lat = wo["geometry"]["coordinates"][1]
        title = wo["properties"]["ISO3_CODE"]
        lons.append(lon)
        lats.append(lat)
        ids.append(title)

    mydata = list(zip(lons, lats, ids))
    mydata = pd.DataFrame(mydata)
    mydata = mydata.rename(columns={0: "lons", 1: "lats", 2: "Code"})

#-- Achtung! Hier befindet sich die Datei mit den Arbeitslosenquote
#-- Ziel: eine gemeinsame Liste mit den Koordinaten und der Zielvariable zu erstellen

    mydata2 = df.rename(columns={"2015": "year2015"})
    mydata2 = mydata2[["Country", "year2015", "Code"]]
    mydata2 = pd.merge(mydata, mydata2, on="Code")

    ax = plt.axes(projection=ccrs.PlateCarree())

#-- Vergrößerung mit hoch 2, einem konstaten Faktor die Liste
    spoint = [sp ** 2 for sp in mydata2["year2015"][:]]

    scpl = ax.scatter(mydata2["lons"], mydata2["lats"], marker="o", c=mydata2["year2015"], s=spoint, alpha=1.0,
                      cmap="turbo",
                      edgecolors="b", transform=ccrs.PlateCarree())
    plt.title("Arbeitslosenquote weltweit von 2015, in %")
    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.OCEAN)
    ax.add_feature(cartopy.feature.COASTLINE)
    ax.add_feature(cartopy.feature.BORDERS, linestyle=':')

    cur = mplcursors.cursor()

    for i, txt in enumerate(mydata2["year2015"]):
        if mydata2["year2015"][i] >= 15:
            ax.annotate(txt, xy=(mydata2["lons"][i], mydata2["lats"][i]), xytext=(2, 3),
            textcoords="offset points", ha="left", va="bottom", clip_on=True, fontsize=12)

    ax.grid()
    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    ax.set_xlabel("longitude")
    ax.set_ylabel("latitide")
    ax.legend()
    plt.colorbar(scpl)
    plt.show()

#-- Funktion zum Aufrufen der Datei
def getfilename():
    fname.set(askopenfilename(filetypes=[("json files", "*.geojson"), ("All files", "*.*")],
                              initialdir=r"C:/Users/elibo/PycharmProject2/pythonProject2",
                              initialfile=r"CNTR_LB_2020_4326.geojson"))
    b2.config(state='normal')
######################################################################################################################
#-- Tkinter Interface
#-- Erstellung der Buttons
l1 = tk.Label(root, text="Plotter")
l1.pack(fill=tk.BOTH, expand=1, ipadx=100, ipady=5)
b1 = tk.Button(root, text="Select File", command=getfilename, underline=7)
b1.pack(fill=tk.BOTH, expand=2, padx=40)
b2 = tk.Button(root, text="Show Plot", state='disabled', command=myplot, underline=0)
b2.pack(fill=tk.BOTH, expand=2, padx=40)

b3 = tk.Button(root, text="Quit", command=root.quit)
b3.pack(fill=tk.BOTH, expand=1, padx=80, pady=7)

root.mainloop()
