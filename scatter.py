# Valerie Walsh 22-04-2018
# Iris Data Set project
# Creating a scatter plot

# Reference: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as p


# Load dataset
url = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# scatter plot matrix
scatter_matrix(dataset)
p.show()