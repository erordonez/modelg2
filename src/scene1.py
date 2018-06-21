
import pandas as pd

class Scene1():
    def scene1(data,freq1,key1):
        scene01 = data.groupby([pd.Grouper(freq=freq1, key=key1)]).mean() #group data for every hour
        hours = scene01.index.hour #retrieve the hour from date column
        scene01['Hour']=hours #store hours in a new column in the dataframe
        scene01=scene01.groupby('Hour').mean() #create an average values for every hour of any day
        return scene01


    def Fscene1(data, deltah):
        scne01= pd.DataFrame(columns=['Hour','Hour-5','Hour-4','Hour-3','Hour-2','Hour-1','Target'])
        scne01['Hour']=range(5,24,deltah) #generate the hour index
        for i in range(0,19): #fill the scenary dataframe
            for j in range (0,6):
                scne01.ix[i,j+1]=data[i+j]
        return scne01

