class Scene4():
    def scene4(data,x):
        datax=data.ix[:,x].round(1) #round the humidity to reduce the number of values
        data.ix[:,x]=datax #include rounded humidity in dataframe
        scene04 = data.groupby('Humedad').mean() #group values according with humidity
        return scene04 #retun the temperature-humidity-concenttration scenary