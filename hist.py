# Valerie Walsh 22-04-2018
# Iris Data Set project scripts
# Running a code to create a histogram of the data 

# Reference: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/


# Load libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as p

# Load dataset
url = "iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# histograms
dataset.hist()
p.show()
