from queue import Empty
import pandas as pd
import os
import csv

temperature = list()
humidity = list()

def openfile(date):
    try:
        df = pd.read_csv(f'../Bouwsensoren/Website/dates/{date}', header=None)
        data = df.values.tolist()
        return(data)

    except:
        return('file not found')

def sortfile(data):
    temperature.clear()
    class sensor():
        def __init__(self, sensorDATA):
            self.sensorDATA = sensorDATA
            sensorDATA = sensorDATA.split(";")
            self.ID = sensorDATA[0]

            temperature.append(sensorDATA[1])
            humidity.append(sensorDATA[2])


    for i in range (len(data)):
        for t in range (len(data[i])):
            sensor(data[i][t])
        
    for i in range (len(temperature)):
        temperature[i] = int(temperature[i])

    for i in range (len(humidity)):
        humidity[i] = int(humidity[i])
       
    # data kan uitgebreid worden, gewoon for-loop bijplaatsen   
    return(temperature, humidity)

def getvalues(date):
    print(sortfile(openfile(date)))
    return(sortfile(openfile(date)))

