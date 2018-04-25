import matplotlib.pyplot as plt
 
# Data to plot
labels = 'Iris Setosa', 'Iris Versicolor', 'Iris Virginica'
sizes = [50, 50, 50]
colors = ['blue', 'yellowgreen', 'lightcoral']
explode = (0.1, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.legend( labels, loc="top")
plt.axis('equal')
plt.show()