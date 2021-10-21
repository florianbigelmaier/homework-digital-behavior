import matplotlib.pyplot as plt
import pandas as pd


sample_data = pd.read_csv('usage-times.csv')

type(sample_data)


x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]



plt.plot(x, y)
plt.plot(x, z)

plt.title("Amount of hours per week spent on each app")


plt.xlabel("week")
plt.ylabel("time [h]")

plt.legend(["Instagram", "WhatsApp"])

plt.show()
