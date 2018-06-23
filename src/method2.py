import pandas as pd

class Method2:
    def method01(data,steps,concentracion): #Build scenary with varaible to be estimated
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long])
        for i in range(0,steps+1):
            scene[i]=data.ix[data.index[i:long-steps+i],concentracion].values
        return scene

    def method02(data,steps,variable1,concentracion): #Build scenary with one variable and varaible to be estimated
        long=len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long])
        for i in range(0,steps+1):
            scene[i]=data.ix[data.index[i:long-steps+i],variable1].values
        scene[steps+1]=data.ix[data.index[steps-1:long-1],concentracion].values
        return scene

    def method03(data,steps,variable1,variable2,concentracion): #Build scenary with two variables and varaible to be estimated
        long=len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long])
        for i in range(0,steps+1):
            d=2*i
            scene[d]=data.ix[data.index[i:long-steps+i],variable1].values
            scene[d+1] = data.ix[data.index[i:long - steps + i], variable2].values
        scene[2*steps]=data.ix[data.index[steps-1:long-1],concentracion].values
        return scene

    def method04(data,steps,variable1,variable2,variable3,concentracion): #Build scenary with three variable and varaible to be estimated
        long=len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long])
        for i in range(0,steps+1):
            d=3*i
            scene[d]=data.ix[data.index[i:long-steps+i],variable1].values
            scene[d+1] = data.ix[data.index[i:long - steps + i], variable2].values
            scene[d + 2] = data.ix[data.index[i:long - steps + i], variable3].values
        scene[3*steps]=data.ix[data.index[steps-1:long-1],concentracion].values
        return scene