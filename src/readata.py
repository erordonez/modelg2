import pandas as pd
from processdata import Prepare
from scene1 import Scenary

df=pd.read_csv('DT.csv') #read data from csv file

todelete = '_id' #Mongodb index name to be deleted
validdate='2018-05-01 00:00:00' #Date when valid date starts
dateindex='Time' #Column where date is stored
temperature1='TemperaturaDHT' #Column where temperature 1 is stored
temperature2='TemperaturaLM35' #Column where temperature 2 is stored

dfx=Prepare.prepare(df,todelete,dateindex,validdate,temperature1,temperature2) #Procesisng data to eliminate innecesary data and calculating aditional data

testPercentage=0.2
test=dfx.sample(frac=testPercentage,random_state=1)
train = dfx.drop(test.index)

period='10min'
columntime='Time'
dfx_train=Scenary.resampleData(train,period,columntime)#Spliting Data for Modeling and Testing
dfx_test=Scenary.resampleData(test,period,columntime)

print(len(train.index))
print(len(test.index))

historyStep=5 #Number of time steps to go back

data01=Scenary.scene1(dfx_train,historyStep,'ConcentracionCO2')
print(data01)

data02=Scenary.scene2(dfx_train,historyStep,'Temperatura','ConcentracionCO2')
print(data02)

data03=Scenary.scene3(dfx_train,historyStep,'Error','Temperatura','ConcentracionCO2')
print(data03)

data04=Scenary.scene4(dfx_train,historyStep,'Error','Temperatura','Humedad','ConcentracionCO2')
print(data04)

data04.to_csv('datatemp2.csv')




#finaldata=pd.DataFrame(index=dfx2.index[extention:a],columns=range(0,extention)) #Dataframe to store the Scenary DataFrame
#print(finaldata)
#finaldata2=finaldata

#method 1, for one variable
#for i in range(0,a-extention):
#    temarr=dfx2.ix[dfx2.index[i:i+extention],'ConcentracionCO2'].values
#    temparr2=np.transpose(temarr)
#    finaldata.ix[finaldata.index[i]]=temparr2

#print(finaldata)

#for two variables
#for i in range (0,extention):
#    d=2*i
#    temparr3=dfx2.ix[dfx2.index[i:a-extention+i],'ConcentracionCO2'].values
#    temparr4=dfx2.ix[dfx2.index[i:a-extention+i],'Humedad'].values
#    finaldata2.ix[:,d]=temparr3
#    finaldata2.ix[:,d+1]=temparr4
#print(finaldata2)