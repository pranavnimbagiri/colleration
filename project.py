import plotly.express as px
import csv
import numpy as np
def getdatasourse(datapath):
    Coffeeinml=[]
    Sleepinhours=[]
    with open("coffee.csv")as f:
         df=csv.DictReader(f)
         for i in df:
             Coffeeinml.append(float(i["Coffee in ml"]))
             Sleepinhours.append(float(i["sleep in hours"]))
    return{"x": Coffeeinml,"y":Sleepinhours}
def findcorealation(datasource):
    corealation=np.corrcoef(datasource["x"],datasource["y"])
    print('corealation between  Coffeeinml vs Sleepinhours ',corealation[0,1])

def setup():
    datapath='coffee.csv'
    datasource=getdatasourse(datapath)
    findcorealation(datasource)

setup()