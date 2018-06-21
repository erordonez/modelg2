import pandas as pd
from matplotlib import pyplot as plt
from processdata import Prepare
from scene1 import Scene1
from scene2 import Scene2
from scene3 import Scene3
from scene4 import Scene4
import numpy

df=pd.read_csv('DT.csv') #read data from csv file

todelete = '_id' #Mongodb index name to be deleted
validdate='2018-05-01 00:00:00' #Date when valid date starts
dateindex=5 #column where date is stored
temperature1=3 #column where temperature 1 is stored
temperature2=4 #column where temperature 2 is stored

dfx=Prepare.prepare(df,todelete,dateindex,validdate,temperature1,temperature2) #procesisng data to eliminate innecesary data

#Building Scenary 1
frequency = '1H'
keyvalue='Time'
timedelta=1
df1=Scene1.scene1(dfx,frequency,keyvalue)
df2=Scene1.Fscene1(df1.ix[:,1],timedelta)

#Building Scenary 2
tcolumn=3
df3=Scene2.scene2(dfx,tcolumn)
df4=Scene2.Fscene2(df3.ix[:,1])

#Building Scenary 3
hcolumn=2
df5=Scene3.scene3(dfx,hcolumn)
df6=Scene3.Fscene3(df5.ix[:,1])

#Building Scenary 4
hcolumn2=2
df7=Scene4.scene4(dfx,hcolumn2)

#printing Scenaries tables
print(df2)
print(df4)
print(df6)
print(df7)