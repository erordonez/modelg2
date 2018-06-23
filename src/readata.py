import pandas as pd
from processdata import Prepare
from scene1 import Scenary
from method2 import Method2

########################Parameters to be set by user##########################
period='10min'      #Period of time to evaluated
historyStep=5       #Number of time steps to go back
testPercentage=0.2  #Fraction of data to be taken as Teste data
##############################################################################

##################Parameters to set according with available##################
todelete = '_id'                #Mongodb index name to be deleted
validdate='2018-05-01 00:00:00' #Date when valid date starts
dateindex='Time'                #Column where date is stored
temperature1='TemperaturaDHT'   #Column where temperature 1 is stored
temperature2='TemperaturaLM35'  #Column where temperature 2 is stored
columntime='Time'               #Column Name containing the new resampled Time
method = 2                      #Method to be used to generate scenaries
##############################################################################

###############################Reading csv file###############################
df=pd.read_csv('../Data/DT2.csv') #read data from csv file
##############################################################################

###########################Processing Data####################################
#Procesisng data to eliminate innecesary data and calculating aditional data
dfx=Prepare.prepare(df,dateindex,validdate,temperature1,temperature2)
##############################################################################

########################Creating Test and Training Data#######################
test=dfx.sample(frac=testPercentage,random_state=1)
train = dfx.drop(test.index)
dfx_train=Scenary.resampleData(train,period,columntime)
dfx_test=Scenary.resampleData(test,period,columntime)
##############################################################################
print(len(train.index))
print(len(test.index))

##########################Assembly posible scenaries##########################
if method==1:
    # Only concentration
    data01=Scenary.scene1(dfx_train,historyStep,'ConcentracionCO2')
    data01.to_csv('../Scenaries/Method1/CO2/CO2only.csv')

    data01 = Scenary.scene1(dfx_train, historyStep, 'ConcentracionCO')
    data01.to_csv('../Scenaries/Method1/CO/COonly.csv')

    # Concentration and one variable
    data02=Scenary.scene2(dfx_train,historyStep,'Temperatura','ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/CO2andTemperature.csv')
    data02 = Scenary.scene2(dfx_train, historyStep, 'Humedad', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/CO2andHumedad.csv')

    data02 = Scenary.scene2(dfx_train, historyStep, 'Temperatura', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/COandTemperature.csv')
    data02 = Scenary.scene2(dfx_train, historyStep, 'Humedad', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/COandHumedad.csv')

    #Concentration and two variables
    data03=Scenary.scene3(dfx_train,historyStep,'Error','Temperatura','ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/CO2andErrorTemperature.csv')
    data03 = Scenary.scene3(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/CO2andHumedadTemperature.csv')

    data03 = Scenary.scene3(dfx_train, historyStep, 'Error', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/COandErrorTemperature.csv')
    data03 = Scenary.scene3(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/COandHumedadTemperature.csv')

    #Concentration and three varaibles
    data04=Scenary.scene4(dfx_train,historyStep,'Error','Temperatura','Humedad','ConcentracionCO2')
    data04.to_csv('../Scenaries/Method1/CO2/CO2andHumedadErrorTemperature.csv')

    data04 = Scenary.scene4(dfx_train, historyStep, 'Error', 'Temperatura', 'Humedad', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method1/CO/COandHumedadErrorTemperature.csv')

    #Saving testing data
    dfx_test.to_csv('../Scenaries/Method1/testData.csv')

    print('Successfully Generated with Method 1')

if method==2:
    # Only concentration
    data01 = Method2.method01(dfx_train,historyStep,'ConcentracionCO2')
    data01.to_csv('../Scenaries/Method2/CO2/CO2only.csv')

    data01 = Method2.method01(dfx_train,historyStep,'ConcentracionCO')
    data01.to_csv('../Scenaries/Method2/CO/COonly.csv')

    # Concentration and one variable
    data02 =Method2.method02(dfx_train,historyStep,'Temperatura','ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/CO2andTemperature.csv')
    data02 =Method2.method02(dfx_train,historyStep,'Humedad','ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/CO2andHumedad.csv')

    data02 =Method2.method02(dfx_train,historyStep,'Temperatura','ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/COandTemperature.csv')
    data02 =Method2.method02(dfx_train,historyStep,'Humedad','ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/COandHumedad.csv')

    # Concentration and two variables
    data03 =Method2.method03(dfx_train,historyStep,'Error','Temperatura','ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/CO2andErrorTemperature.csv')
    data03 =Method2.method03(dfx_train,historyStep,'Humedad','Temperatura','ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/CO2andHumedadTemperature.csv')

    data03 =Method2.method03(dfx_train,historyStep,'Error','Temperatura','ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/COandErrorTemperature.csv')
    data03 = Method2.method03(dfx_train,historyStep,'Humedad','Temperatura','ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/COandHumedadTemperature.csv')

    # Concentration and three varaibles
    data04 =Method2.method04(dfx_train,historyStep,'Humedad','Error','Temperatura','ConcentracionCO2')
    data04.to_csv('../Scenaries/Method2/CO2/CO2andHumedadErrorTemperature.csv')

    data04 =Method2.method04(dfx_train,historyStep,'Humedad','Error','Temperatura','ConcentracionCO')
    data04.to_csv('../Scenaries/Method2/CO/COandHumedadErrorTemperature.csv')

    # Saving testing data
    dfx_test.to_csv('../Scenaries/Method2/testData.csv')

    print('Successfully Generated with Method 2')