import pandas as pd
import numpy as np

class Scenary():
    def resampleData(data,period,timeColumn,continuos):
        resampled = data.resample(period,on=timeColumn).mean() #Resample the data for given time period
        resampled['Hour'] = resampled.index.time #Retrieve the hour
        if continuos=='Yes':
            scene01 = resampled  # Create an average values for every time step of any day
        else:
            scene01 = resampled.groupby('Hour').mean()  # Create an average values for every time step of any day
        return scene01
        return scene01

    def scene1(data,steps,concentracion): #Build scenary with varaible to be estimated
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long],columns=range(0,steps+1))
        for i in range (0,long-steps):
            temp = data.ix[data.index[i:i + steps+1], concentracion].values
            temp2 = np.transpose(temp)
            scene.ix[scene.index[i]] = temp2
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time'] = scene.index.hour * 100 + scene.index.minute
        return scene

    def scene2(data, steps, variable1,variable2):  #Build scenary with two variables
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, 2*steps))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp1=data.ix[data.index[i:i + steps], variable2].values
            temp2 = np.ravel(np.column_stack((temp,temp1)))
            temp3 = np.transpose(temp2)
            scene.ix[scene.index[i]] = temp3
        scene.ix[scene.index[0:long - steps], 2 * steps] = data.ix[data.index[steps:long], variable2]
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time'] = scene.index.hour * 100 + scene.index.minute
        return scene

    def scene3(data, steps, variable1, variable2,variable3):  #Build scenary with three variables
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, 3 * steps))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp2 = data.ix[data.index[i:i + steps], variable2].values
            temp3=data.ix[data.index[i:i + steps], variable3].values
            temp4 = np.ravel(np.column_stack((temp,temp2,temp3)))
            temp5 = np.transpose(temp4)
            scene.ix[scene.index[i]] = temp5
        scene.ix[scene.index[0:long - steps], 3 * steps] = data.ix[data.index[steps:long], variable3]
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time'] = scene.index.hour * 100 + scene.index.minute
        return scene

    def scene4(data, steps, variable1, variable2, variable3, variable4):  #Build scenary with three variables
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, 4 * steps))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp2 = data.ix[data.index[i:i + steps], variable2].values
            temp3=data.ix[data.index[i:i + steps], variable3].values
            temp4 = data.ix[data.index[i:i + steps], variable4].values
            temp5 = np.ravel(np.column_stack((temp,temp2,temp3,temp4)))
            temp6 = np.transpose(temp5)
            scene.ix[scene.index[i]] = temp6
        scene.ix[scene.index[0:long - steps], 4 * steps] = data.ix[data.index[steps:long], variable4]
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time'] = scene.index.hour * 100 + scene.index.minute
        return scene

    def scene5(data, steps, variable1, variable2, variable3, variable4,variable5):  #Build scenary with three variables
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, 5 * steps))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp2 = data.ix[data.index[i:i + steps], variable2].values
            temp3=data.ix[data.index[i:i + steps], variable3].values
            temp4 = data.ix[data.index[i:i + steps], variable4].values
            temp5 = data.ix[data.index[i:i + steps], variable5].values
            temp6 = np.ravel(np.column_stack((temp,temp2,temp3,temp4,temp5)))
            temp7 = np.transpose(temp6)
            scene.ix[scene.index[i]] = temp7
        scene.ix[scene.index[0:long - steps], 5 * steps] = data.ix[data.index[steps:long], variable5]
        scene['Year'] = scene.index.year
        scene['Month'] = scene.index.month
        scene['Day'] = scene.index.day
        scene['Time'] = scene.index.hour * 100 + scene.index.minute
        return scene