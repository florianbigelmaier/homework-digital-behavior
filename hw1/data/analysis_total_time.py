import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


sample_data = pd.read_csv('total-time.csv')


plt.figure(figsize = (12,7))

X = np.arange(len(sample_data.amount))

plt.bar(X, sample_data.amount, align='center',color='#014983', width = 0.7)

plt.title("Amount of daily hours spent on the smartphone (weekly mean)")

plt.xticks([i for i in range(3)], ['Week 39', 'Week 40', 'Week 41'])

plt.legend(['total time'])

plt.xlabel("Calendar week")
plt.ylabel("time [h]")

plt.savefig('usage-times-total.png')
plt.show()



