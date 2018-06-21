import pandas as pd

class Scene3():
    def scene3(data,x):
        datax=data.ix[:,x].round(1)#round the humidity to reduce the number of values
        data.ix[:,x]=datax #include rounded humidity in dataframe
        scene03 = data.groupby('Humedad').mean() #group values according with humidity
        return scene03


    def Fscene3(data):
        a=len(data.axes[0])#determine the number of rows of the dataframe
        scne03= pd.DataFrame(columns=['Hum','Hum-5','Hum-4','Hum-3','Hum-2','Hum-1','Target'])
        b=len(scne03.axes[1])#dtermine the number of columns of the scenary dtaframe
        scne03['Hum']=data.index[b-1:a]#fill the scenary dataframe with temperature values
        for i in range(0,a-b+1):#fill the scenary dataframe with concentration values
            for j in range (0,b-1):
                scne03.ix[i,j+1]=data[data.index[i+j]]
        return scne03