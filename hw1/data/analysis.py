import matplotlib.pyplot as plt
#import mplleaflet
import pandas as pd
import numpy as np
# Daten einlesen
# gibt einen DataFrame zurück
app_usage = pd.read_csv('usage-times.csv')

# Daten sortieren nach ID und Datum
#app_usage.sort(['app','week in calendar']).head()





# Grafik
plt.figure(figsize=(15,10))
plt.plot(tmin.values, 'blue', label = 'Week 40')
plt.plot(tmax.values, 'red', label = 'Week 41')
plt.xlabel('App')
plt.ylabel('Time in h')
#plt.xticks(range(len(tmin), 20), tmin.index[range(0, len(tmin), 20)], rotation = '45')
#plt.gca().fill_between(range(len(tmin)), tmin['Data_Value'], tmax['Data_Value'], facecolor = 'grey', alpha = 0.2)
plt.title('App Usage', fontsize= 20)


plt.legend(loc = 4, frameon = False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.show()
