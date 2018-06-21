import pandas as pd

class Prepare():
    def prepare(data, id, x,datef,temp1,temp2):
        data1=data.drop(columns=[id]) #eliminate Mongodb index from dataframe
        datex=data1.ix[:,x] #retrieve column with date data
        datex=pd.to_datetime(datex) #transform date from object to timestamp
        data1.ix[:,x]=datex #include date in timestamp format in dataframe
        data1=data1[data1.Time[:]>datef] #eliminate inicial not valid data
        data1=data1.reset_index(level=0, drop=True) #restart index from dataframe
        tempa=(data1.ix[:,temp1]+data1.ix[:,temp2])/2 #calculating average temperature
        data1.ix[:,temp1]=tempa #include average temperature in dataframe
        data1=data1.drop(data1.columns[[temp2]], axis=1) #eliminate original temperature columns
        return data1