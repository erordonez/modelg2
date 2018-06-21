import pandas as pd

class Scene2():
    def scene2(data,x):
        datax=data.ix[:,x].round(1) #round the temperature to reduce the number of values
        data.ix[:,x]=datax #include rounded temperature in dataframe
        scene02 = data.groupby('TemperaturaDHT').mean() #group concentration values according with temperature values
        return scene02


    def Fscene2(data):
        a=len(data.axes[0]) #determine the number of rows of the dataframe
        scne02= pd.DataFrame(columns=['Temp','Temp-5','Temp-4','Temp-3','Temp-2','Temp-1','Target'])
        b=len(scne02.axes[1]) #dtermine the number of columns of the scenary dtaframe
        scne02['Temp']=data.index[b-1:a] #fill the scenary dataframe with temperature values
        for i in range(0,a-b+1): #fill the scenary dataframe with concentration values
            for j in range (0,b-1):
                scne02.ix[i,j+1]=data[data.index[i+j]]
        return scne02