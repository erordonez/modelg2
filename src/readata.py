import pandas as pd
from processdata import Prepare
from scene1 import Scenary
from method2 import Method2

########################Parameters to be set by user##########################
period='30min'        #Period of time to evaluated
continuos='Yes'     #Evaluate if use an average or an continuos data generation
historyStep=5       #Number of time steps to go back
testPercentage=0.2  #Fraction of data to be taken as Teste data
method=2
##############################################################################

##################Parameters to set according with available##################
#todelete = '_id'               #Mongodb index name to be deleted
validdate='2018-05-01 00:00:00' #Date when valid date starts
dateindex='Time'                #Column where date is stored
temperature1='TemperaturaDHT'   #Column where temperature 1 is stored
temperature2='TemperaturaLM35'  #Column where temperature 2 is stored
columntime='Time'               #Column Name containing the new resampled Time
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
dfx_train=Scenary.resampleData(train,period,columntime,continuos)
dfx_test=Scenary.resampleData(test,period,columntime,continuos)
##############################################################################

##########################Assembly posible scenaries##########################
if method == 1:
    # Only concentration
    data01=Scenary.scene1(dfx_train,historyStep,'ConcentracionCO2')
    data01.to_csv('../Scenaries/Method1/CO2/CO2only.csv',index=False)

    data01 = Scenary.scene1(dfx_train, historyStep, 'ConcentracionCO')
    data01.to_csv('../Scenaries/Method1/CO/COonly.csv',index=False)

        #Test
    data01 = Scenary.scene1(dfx_test, historyStep, 'ConcentracionCO2')
    data01.to_csv('../Scenaries/Method1/CO2/test/CO2only.csv',index=False)

    data01 = Scenary.scene1(dfx_test, historyStep, 'ConcentracionCO')
    data01.to_csv('../Scenaries/Method1/CO/test/COonly.csv',index=False)

    # Concentration CO and Concentration CO2
    data02=Scenary.scene2(dfx_train,historyStep,'ConcentracionCO','ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/CO2andCO.csv',index=False)

    data02 = Scenary.scene2(dfx_train, historyStep, 'Temperatura', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/CO2andTemperature.csv',index=False)

    data02 = Scenary.scene2(dfx_train, historyStep, 'Humedad', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/CO2andHumedad.csv',index=False)

    data02 = Scenary.scene2(dfx_train, historyStep, 'Error', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/CO2andError.csv',index=False)

    data02 = Scenary.scene2(dfx_train, historyStep, 'ConcentracionCO2', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/COandCO2.csv',index=False)

    data02 = Scenary.scene2(dfx_train, historyStep, 'Temperatura', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/COandTemperatura.csv',index=False)

    data02 = Scenary.scene2(dfx_train, historyStep, 'Humedad', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/COandHumedad.csv',index=False)

    data02 = Scenary.scene2(dfx_train, historyStep, 'Error', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/COandError.csv',index=False)

        #Test
    data02 = Scenary.scene2(dfx_test, historyStep, 'ConcentracionCO', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/test/CO2andCO.csv',index=False)

    data02 = Scenary.scene2(dfx_test, historyStep, 'Temperatura', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/test/CO2andTemperature.csv',index=False)

    data02 = Scenary.scene2(dfx_test, historyStep, 'Humedad', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/test/CO2andHumedad.csv',index=False)

    data02 = Scenary.scene2(dfx_test, historyStep, 'Error', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method1/CO2/test/CO2andError.csv',index=False)

    data02 = Scenary.scene2(dfx_test, historyStep, 'ConcentracionCO2', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/test/COandCO2.csv',index=False)

    data02 = Scenary.scene2(dfx_test, historyStep, 'Temperatura', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/test/COandTemperatura.csv',index=False)

    data02 = Scenary.scene2(dfx_test, historyStep, 'Humedad', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/test/COandHumedad.csv',index=False)

    data02 = Scenary.scene2(dfx_test, historyStep, 'Error', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method1/CO/test/COandError.csv',index=False)

    #Concentration and two variables
    data03=Scenary.scene3(dfx_train,historyStep,'Temperatura','ConcentracionCO','ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/CO2andCOandTemperature.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Error', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/CO2andCOandError.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Humedad', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/CO2andCOandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/CO2andTemperatureandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Error', 'Temperatura', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/CO2andErrorandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Error', 'Humedad', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/CO2andErrorandHumedad.csv',index=False)
        #
    data03 = Scenary.scene3(dfx_train, historyStep, 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/COandCO2andTemperature.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Error', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/COandCO2andError.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Humedad', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/COandCO2andHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/COandTemperatureandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Error', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/COandErrorandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_train, historyStep, 'Error', 'Humedad', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/COandErrorandHumedad.csv',index=False)


        #Test
    data03 = Scenary.scene3(dfx_test, historyStep, 'Temperatura', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/test/CO2andCOandTemperature.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Error', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/test/CO2andCOandError.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Humedad', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/test/CO2andCOandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/test/CO2andTemperatureandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Error', 'Temperatura', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/test/CO2andErrorandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Error', 'Humedad', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method1/CO2/test/CO2andErrorandHumedad.csv',index=False)
        #
    data03 = Scenary.scene3(dfx_test, historyStep, 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/test/COandCO2andTemperature.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Error', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/test/COandCO2andError.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Humedad', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/test/COandCO2andHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/test/COandTemperatureandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Error', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/test/COandErrorandHumedad.csv',index=False)

    data03 = Scenary.scene3(dfx_test, historyStep, 'Error', 'Humedad', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method1/CO/test/COandErrorandHumedad.csv',index=False)


    #Concentration and three varaibles
    data04=Scenary.scene4(dfx_train,historyStep,'Error','Temperatura','ConcentracionCO','ConcentracionCO2')
    data04.to_csv('../Scenaries/Method1/CO2/CO2andCOandTemperatureandError.csv',index=False)

    data04 = Scenary.scene4(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method1/CO2/CO2andCOandTemperatureandHumedad.csv',index=False)

    data04 = Scenary.scene4(dfx_train, historyStep, 'Humedad', 'Error', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method1/CO2/CO2andCOandErrorandHumedad.csv',index=False)

    data04 = Scenary.scene4(dfx_train, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method1/CO2/CO2andTemperatureandErrorandHumedad.csv',index=False)
        #
    data04 = Scenary.scene4(dfx_train, historyStep, 'Error', 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method1/CO/COandCO2andTemperatureandError.csv',index=False)

    data04 = Scenary.scene4(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method1/CO/COandCO2andTemperatureandHumed.csv',index=False)

    data04 = Scenary.scene4(dfx_train, historyStep, 'Humedad', 'Error', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method1/CO/COandCO2andErrorandHumedad.csv',index=False)

    data04 = Scenary.scene4(dfx_train, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method1/CO/COandTemperatureandErrorandHumedad.csv',index=False)

        #Test

    data04 = Scenary.scene4(dfx_test, historyStep, 'Error', 'Temperatura', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method1/CO2/test/CO2andCOandTemperatureandError.csv',index=False)

    data04 = Scenary.scene4(dfx_test, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method1/CO2/test/CO2andCOandTemperatureandHumedad.csv',index=False)

    data04 = Scenary.scene4(dfx_test, historyStep, 'Humedad', 'Error', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method1/CO2/test/CO2andCOandErrorandHumedad.csv',index=False)

    data04 = Scenary.scene4(dfx_test, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method1/CO2/test/CO2andTemperatureandErrorandHumedad.csv',index=False)
    #
    data04 = Scenary.scene4(dfx_test, historyStep, 'Error', 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method1/CO/test/COandCO2andTemperatureandError.csv',index=False)

    data04 = Scenary.scene4(dfx_test, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method1/CO/test/COandCO2andTemperatureandHumed.csv',index=False)

    data04 = Scenary.scene4(dfx_test, historyStep, 'Humedad', 'Error', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method1/CO/test/COandCO2andErrorandHumedad.csv',index=False)

    data04 = Scenary.scene4(dfx_test, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method1/CO/test/COandTemperatureandErrorandHumedad.csv',index=False)

    #Concentration and four variables

    data05 = Scenary.scene5(dfx_train, historyStep, 'Humedad', 'Error', 'Temperatura','ConcentracionCO','ConcentracionCO2')
    data05.to_csv('../Scenaries/Method1/CO2/CO2andall.csv',index=False)

    data05 = Scenary.scene5(dfx_train, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO2','ConcentracionCO')
    data05.to_csv('../Scenaries/Method1/CO/COandall.csv',index=False)

        #Test
    data05 = Scenary.scene5(dfx_test, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO','ConcentracionCO2')
    data05.to_csv('../Scenaries/Method1/CO2/test/CO2andall.csv',index=False)

    data05 = Scenary.scene5(dfx_test, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO2','ConcentracionCO')
    data05.to_csv('../Scenaries/Method1/CO/test/COandall.csv',index=False)

    print('Successfully Generated with Method 1')

if method==2:

    # Only concentration
    data01=Method2.method01(dfx_train,historyStep,'ConcentracionCO2')
    data01.to_csv('../Scenaries/Method2/CO2/CO2only.csv',index=False)

    data01 = Method2.method01(dfx_train, historyStep, 'ConcentracionCO')
    data01.to_csv('../Scenaries/Method2/CO/COonly.csv',index=False)

        #Test
    data01 = Method2.method01(dfx_test, historyStep, 'ConcentracionCO2')
    data01.to_csv('../Scenaries/Method2/CO2/test/CO2only.csv',index=False)

    data01 = Method2.method01(dfx_test, historyStep, 'ConcentracionCO')
    data01.to_csv('../Scenaries/Method2/CO/test/COonly.csv',index=False)

    # Concentration CO and Concentration CO2
    data02=Method2.method02(dfx_train,historyStep,'ConcentracionCO','ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/CO2andCO.csv',index=False)

    data02 = Method2.method02(dfx_train, historyStep, 'Temperatura', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/CO2andTemperature.csv',index=False)

    data02 = Method2.method02(dfx_train, historyStep, 'Humedad', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/CO2andHumedad.csv',index=False)

    data02 = Method2.method02(dfx_train, historyStep, 'Error', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/CO2andError.csv',index=False)

    data02 = Method2.method02(dfx_train, historyStep, 'ConcentracionCO2', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/COandCO2.csv',index=False)

    data02 = Method2.method02(dfx_train, historyStep, 'Temperatura', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/COandTemperatura.csv',index=False)

    data02 = Method2.method02(dfx_train, historyStep, 'Humedad', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/COandHumedad.csv',index=False)

    data02 = Method2.method02(dfx_train, historyStep, 'Error', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/COandError.csv',index=False)

        #Test
    data02 = Method2.method02(dfx_test, historyStep, 'ConcentracionCO', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/test/CO2andCO.csv',index=False)

    data02 = Method2.method02(dfx_test, historyStep, 'Temperatura', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/test/CO2andTemperature.csv',index=False)

    data02 = Method2.method02(dfx_test, historyStep, 'Humedad', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/test/CO2andHumedad.csv',index=False)

    data02 = Method2.method02(dfx_test, historyStep, 'Error', 'ConcentracionCO2')
    data02.to_csv('../Scenaries/Method2/CO2/test/CO2andError.csv',index=False)

    data02 = Method2.method02(dfx_test, historyStep, 'ConcentracionCO2', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/test/COandCO2.csv',index=False)

    data02 = Method2.method02(dfx_test, historyStep, 'Temperatura', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/test/COandTemperatura.csv',index=False)

    data02 = Method2.method02(dfx_test, historyStep, 'Humedad', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/test/COandHumedad.csv',index=False)

    data02 = Method2.method02(dfx_test, historyStep, 'Error', 'ConcentracionCO')
    data02.to_csv('../Scenaries/Method2/CO/test/COandError.csv',index=False)

    #Concentration and two variables
    data03=Method2.method03(dfx_train,historyStep,'Temperatura','ConcentracionCO','ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/CO2andCOandTemperature.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Error', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/CO2andCOandError.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Humedad', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/CO2andCOandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/CO2andTemperatureandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Error', 'Temperatura', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/CO2andErrorandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Error', 'Humedad', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/CO2andErrorandHumedad.csv',index=False)
        #
    data03 = Method2.method03(dfx_train, historyStep, 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/COandCO2andTemperature.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Error', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/COandCO2andError.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Humedad', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/COandCO2andHumedad.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/COandTemperatureandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Error', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/COandErrorandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_train, historyStep, 'Error', 'Humedad', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/COandErrorandHumedad.csv',index=False)


        #Test
    data03 = Method2.method03(dfx_test, historyStep, 'Temperatura', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/test/CO2andCOandTemperature.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Error', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/test/CO2andCOandError.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Humedad', 'ConcentracionCO', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/test/CO2andCOandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/test/CO2andTemperatureandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Error', 'Temperatura', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/test/CO2andErrorandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Error', 'Humedad', 'ConcentracionCO2')
    data03.to_csv('../Scenaries/Method2/CO2/test/CO2andErrorandHumedad.csv',index=False)
        #
    data03 = Method2.method03(dfx_test, historyStep, 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/test/COandCO2andTemperature.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Error', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/test/COandCO2andError.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Humedad', 'ConcentracionCO2', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/test/COandCO2andHumedad.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/test/COandTemperatureandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Error', 'Temperatura', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/test/COandErrorandHumedad.csv',index=False)

    data03 = Method2.method03(dfx_test, historyStep, 'Error', 'Humedad', 'ConcentracionCO')
    data03.to_csv('../Scenaries/Method2/CO/test/COandErrorandHumedad.csv',index=False)


    #Concentration and three varaibles
    data04=Method2.method04(dfx_train,historyStep,'Error','Temperatura','ConcentracionCO','ConcentracionCO2')
    data04.to_csv('../Scenaries/Method2/CO2/CO2andCOandTemperatureandError.csv',index=False)

    data04 = Method2.method04(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method2/CO2/CO2andCOandTemperatureandHumedad.csv',index=False)

    data04 = Method2.method04(dfx_train, historyStep, 'Humedad', 'Error', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method2/CO2/CO2andCOandErrorandHumedad.csv',index=False)

    data04 = Method2.method04(dfx_train, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method2/CO2/CO2andTemperatureandErrorandHumedad.csv',index=False)
        #
    data04 = Method2.method04(dfx_train, historyStep, 'Error', 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method2/CO/COandCO2andTemperatureandError.csv',index=False)

    data04 = Method2.method04(dfx_train, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method2/CO/COandCO2andTemperatureandHumed.csv',index=False)

    data04 = Method2.method04(dfx_train, historyStep, 'Humedad', 'Error', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method2/CO/COandCO2andErrorandHumedad.csv',index=False)

    data04 = Method2.method04(dfx_train, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method2/CO/COandTemperatureandErrorandHumedad.csv',index=False)

        #Test

    data04 = Method2.method04(dfx_test, historyStep, 'Error', 'Temperatura', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method2/CO2/test/CO2andCOandTemperatureandError.csv',index=False)

    data04 = Method2.method04(dfx_test, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method2/CO2/test/CO2andCOandTemperatureandHumedad.csv',index=False)

    data04 = Method2.method04(dfx_test, historyStep, 'Humedad', 'Error', 'ConcentracionCO', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method2/CO2/test/CO2andCOandErrorandHumedad.csv',index=False)

    data04 = Method2.method04(dfx_test, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO2')
    data04.to_csv('../Scenaries/Method2/CO2/test/CO2andTemperatureandErrorandHumedad.csv',index=False)
    #
    data04 = Method2.method04(dfx_test, historyStep, 'Error', 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method2/CO/test/COandCO2andTemperatureandError.csv',index=False)

    data04 = Method2.method04(dfx_test, historyStep, 'Humedad', 'Temperatura', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method2/CO/test/COandCO2andTemperatureandHumed.csv',index=False)

    data04 = Method2.method04(dfx_test, historyStep, 'Humedad', 'Error', 'ConcentracionCO2', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method2/CO/test/COandCO2andErrorandHumedad.csv',index=False)

    data04 = Method2.method04(dfx_test, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO')
    data04.to_csv('../Scenaries/Method2/CO/test/COandTemperatureandErrorandHumedad.csv',index=False)

    #Concentration and four variables

    data05 = Method2.method05(dfx_train, historyStep, 'Humedad', 'Error', 'Temperatura','ConcentracionCO','ConcentracionCO2')
    data05.to_csv('../Scenaries/Method2/CO2/CO2andall.csv',index=False)

    data05 = Method2.method05(dfx_train, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO2','ConcentracionCO')
    data05.to_csv('../Scenaries/Method2/CO/COandall.csv',index=False)

        #Test
    data05 = Method2.method05(dfx_test, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO','ConcentracionCO2')
    data05.to_csv('../Scenaries/Method2/CO2/test/CO2andall.csv',index=False)

    data05 = Method2.method05(dfx_test, historyStep, 'Humedad', 'Error', 'Temperatura', 'ConcentracionCO2','ConcentracionCO')
    data05.to_csv('../Scenaries/Method2/CO/test/COandall.csv',index=False)

    print('Successfully Generated with Method 2')
##############################################################################