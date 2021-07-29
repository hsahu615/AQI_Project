import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
def aqi_year(n):
    average = []
    for rows in pd.read_csv('AQI/aqi'+n+'.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i
            elif type(i) is str:
                if i!='NoData' and i!='InVld' and i!='---' and i!='PwrFail':
                    add_var = add_var + float(i)
        avg = add_var/24
        average.append(avg)
    return average
if __name__ == '__main__':
    f = plt.figure(figsize=(25,12))
    aqi2013 = aqi_year('2013')
    aqi2014 = aqi_year('2014')
    aqi2015 = aqi_year('2015')
    aqi2016 = aqi_year('2016')
    plt.plot(range(0,len(aqi2013)), aqi2013,label = "2013")
    plt.plot(range(0,len(aqi2014)), aqi2014,label = "2014")
    plt.plot(range(0,len(aqi2015)), aqi2015,label = "2015")
    plt.plot(range(0,len(aqi2016)), aqi2016,label = "2016")
    plt.legend(fontsize = 16)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid()