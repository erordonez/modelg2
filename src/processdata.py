import pandas as pd

class Prepare():
    def prepare(data, id, x,datef,temp1,temp2):

        #data.drop(columns=[id],inplace=True) #Eliminate Mongodb index from dataframe

        datex=data[x] #Retrieve column with date data

        datex=pd.to_datetime(datex) #Transform date from object to timestamp

        data[x]=datex #Include date in timestamp format in dataframe

        data1=data[data.Time[:]>datef] #Eliminate inicial not valid data

        data1 = data1.assign(Temperatura=((data1.loc[:,temp1]+data1.loc[:,temp2])/2).values)

        #Calculating Temperature error
        data1= data1.assign(Error=((((data1.loc[:,temp1])-((data1.loc[:,temp1]+data1.loc[:,temp2])/2 )).abs()
                              +((data1.loc[:,temp1])-((data1.loc[:,temp2]+data1.loc[:,temp2])/2 )).abs())/2).values)

        data1.drop([temp1], axis=1,inplace=True)  # eliminate original temperature columns
        data1.drop([temp2], axis=1, inplace=True)  # eliminate original temperature columns

        return data1