import pandas as pd
import numpy as np

class Scenary():
    def resampleData(data,period,timeColumn):
        resampled = data.resample(period,on=timeColumn).mean() #Resample the data for given time period
        resampled['Hour'] = resampled.index.time #Retrieve the hour
        scene01=resampled.groupby('Hour').mean() #Create an average values for every time step of any day
        return scene01


    def scene1(data,steps,concentracion): #Build scenary with varaible to be estimated
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long],columns=range(0,steps+1))
        for i in range (0,long-steps):
            temp = data.ix[data.index[i:i + steps], concentracion].values
            temp = np.append(temp, ['0'])
            temp2 = np.transpose(temp)
            scene.ix[scene.index[i]] = temp2
        scene.ix[scene.index[0:long - steps], steps] = data.ix[data.index[steps:long], concentracion]
        return scene

    def scene2(data, steps, variable1, concentracion):  #Build scenary with one variable
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, steps+2))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp = np.append(temp, ['0'])
            temp = np.append(temp, ['0'])
            temp1 = np.transpose(temp)
            scene.ix[scene.index[i]] = temp1
        scene.ix[scene.index[0:long - steps], steps] = data.ix[data.index[steps:long],variable1]
        scene.ix[scene.index[0:long - steps], steps+1] = data.ix[data.index[steps:long], concentracion]
        return scene

    def scene3(data, steps, variable1,variable2, concentracion):  #Build scenary with two variables
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, 2*steps+3))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp1=data.ix[data.index[i:i + steps], variable2].values
            temp2 = np.ravel(np.column_stack((temp,temp1)))
            temp2 = np.append(temp2, ['0'])
            temp2 = np.append(temp2, ['0'])
            temp2 = np.append(temp2, ['0'])
            temp3 = np.transpose(temp2)
            scene.ix[scene.index[i]] = temp3
        scene.ix[scene.index[0:long - steps], 2*steps] = data.ix[data.index[steps:long], variable1]
        scene.ix[scene.index[0:long - steps], 2*steps + 1] = data.ix[data.index[steps:long], variable2]
        scene.ix[scene.index[0:long - steps], 2*steps + 2] = data.ix[data.index[steps:long], concentracion]
        return scene

    def scene4(data, steps, variable1, variable2,variable3, concentracion):  #Build scenary with three variables
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, 3 * steps+4))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp2 = data.ix[data.index[i:i + steps], variable2].values
            temp3=data.ix[data.index[i:i + steps], variable3].values
            temp4 = np.ravel(np.column_stack((temp,temp2,temp3)))
            temp4 = np.append(temp4, ['0'])
            temp4 = np.append(temp4, ['0'])
            temp4 = np.append(temp4, ['0'])
            temp4 = np.append(temp4, ['0'])
            temp5 = np.transpose(temp4)
            scene.ix[scene.index[i]] = temp5
        scene.ix[scene.index[0:long - steps], 3 * steps] = data.ix[data.index[steps:long], variable1]
        scene.ix[scene.index[0:long - steps], 3 * steps + 1] = data.ix[data.index[steps:long], variable2]
        scene.ix[scene.index[0:long - steps], 3 * steps + 2] = data.ix[data.index[steps:long], variable3]
        scene.ix[scene.index[0:long - steps], 3 * steps + 3] = data.ix[data.index[steps:long], concentracion]
        return scene

