import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


sample_data = pd.read_csv('usage-times-cat.csv')

#sample_data = sample_data.pivot(index = "week", columns = "app", values = "amount").reset_index().rename_axis(None, axis=1)




#x = sample_data.app
#y = sample_data.amount
#z = sample_data.week

plt.figure(figsize = (12,7))

X = np.arange(len(sample_data.social))

plt.bar(X, sample_data.social, align='center',color='#014983', width = 0.2)
plt.bar(X + 0.2, sample_data.messaging, color = '#F49801', width = 0.2)
plt.bar(X + 0.4, sample_data.browsing, color = '#111111', width = 0.2)
plt.bar(X + 0.6, sample_data.news, color = '#bbbbbb', width = 0.2)

plt.title("Amount of hours per week spent on each app category")

plt.xticks([i + 0.25 for i in range(3)], ['Week 39', 'Week 40', 'Week 41'])

plt.legend(['Social Media Apps', 'Instant Messaging Apps', 'Web Browsers', 'News and Entertainment Apps'])

plt.xlabel("Calendar week")
plt.ylabel("time [h]")

plt.savefig('usage-times.png')
plt.show()



