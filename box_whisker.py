# Valerie Walsh 22-04-2018
# Iris Data Set Project - scripts
# Reference: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Code for Box and Whisker Plots of Iris Data Set 

# Load libraries required 
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as p

# Load dataset
url = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
p.show()
