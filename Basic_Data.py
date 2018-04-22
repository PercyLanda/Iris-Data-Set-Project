# Valerie Walsh - 10-04-2018
# Iris Data Set Project - scripts
# Attempting basic tasks within Python

import pandas


#Load the dataset from the file
open = "iris.csv"
names = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class']
dataset = pandas.read_csv(open, names=names)

# I wasnt happy with the way this file was appearing in output and wanted it to look cleaner
# I found this print function to provide spacing between outputs:
# https://softwareengineering.stackexchange.com/questions/363952/name-and-code-to-space-between-lines-paragraphs
print('\n')

# Display the contents of the data set in the form of rows and columns
print("The amount of rows and colums in this data set are:", dataset.shape)


print('\n')

# An option to view the start of the data set with the number in () being the amount of rows viewable 
print(dataset.head(12))

print('\n')

# A table listing the attributes within the data set including: min, max, mean
print(dataset.describe())

print('\n')

# The amount of rows in each Class 
# Based on the history of the data set, I know there are 50 samples of each
# However based on the learning aspect of the project, I wanted to include this output
print(dataset.groupby('Class').size())

# A script which outputs 10 random numbers from the data set
r = numpy.random.rand(10)
print(r)


