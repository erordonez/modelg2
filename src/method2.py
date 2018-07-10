import pandas as pd
import numpy as np

class Method2:
    def method01(data,steps,concentracion): #Build scenary with varaible to be estimated
        long=len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long])
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time']=scene.index.hour*100+scene.index.minute
        for i in range(0,steps+1):
            scene[i]=data.ix[data.index[i:long-steps+i],concentracion].values
        return scene

    def method02(data,steps,variable1,variable2): #Build scenary with two variables and varaible to be estimated
        long=len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long])
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time']=scene.index.hour*100+scene.index.minute
        for i in range(0,steps):
            d=2*i
            scene[d]=data.ix[data.index[i:long-steps+i],variable1].values
            scene[d+1] = data.ix[data.index[i:long - steps + i], variable2].values
        scene[d + 2] = data.ix[data.index[steps:long], variable2].values
        return scene

    def method03(data,steps,variable1,variable2,variable3): #Build scenary with three variable and varaible to be estimated
        long=len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long])
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time']=scene.index.hour*100+scene.index.minute
        for i in range(0,steps):
            d=3*i
            scene[d]=data.ix[data.index[i:long-steps+i],variable1].values
            scene[d+1] = data.ix[data.index[i:long - steps + i], variable2].values
            scene[d + 2] = data.ix[data.index[i:long - steps + i], variable3].values
        scene[d + 3] = data.ix[data.index[steps:long], variable3].values
        return scene

    def method04(data, steps, variable1, variable2, variable3, variable4):  # Build scenary with three variable and varaible to be estimated
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long])
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time']=scene.index.hour*100+scene.index.minute
        for i in range(0, steps):
            d = 4 * i
            scene[d] = data.ix[data.index[i:long - steps + i], variable1].values
            scene[d + 1] = data.ix[data.index[i:long - steps + i], variable2].values
            scene[d + 2] = data.ix[data.index[i:long - steps + i], variable3].values
            scene[d + 3] = data.ix[data.index[i:long - steps + i], variable4].values
        scene[d + 4] = data.ix[data.index[steps:long], variable4].values
        return scene

    def method05(data, steps, variable1, variable2, variable3, variable4,variable5):  # Build scenary with four variable and varaible to be estimated
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long])
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time']=scene.index.hour*100+scene.index.minute
        for i in range(0, steps):
            d = 5 * i
            scene[d] = data.ix[data.index[i:long - steps + i], variable1].values
            scene[d + 1] = data.ix[data.index[i:long - steps + i], variable2].values
            scene[d + 2] = data.ix[data.index[i:long - steps + i], variable3].values
            scene[d + 3] = data.ix[data.index[i:long - steps + i], variable4].values
            scene[d + 4] = data.ix[data.index[i:long - steps + i], variable5].values
        scene[d + 5] = data.ix[data.index[steps:long], variable5].values
        return scene