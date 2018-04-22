# Valerie Walsh 22-04-2018
# Iris Data Set project
# Reference: Topic 7 videos 
# Calculating the mean of each column

import numpy
data = numpy.genfromtxt('iris.csv', delimiter=',')

meanfirstcol = numpy.mean(data[:,0])
meansecondcol = numpy.mean(data[:,1])
meanthirdcol = numpy.mean(data[:,2])
meanforthcol = numpy.mean(data[:,3])

print('\n')

print("First column is:", meanfirstcol)

print("Second column is:", meansecondcol)

print("Third column is:", meanthirdcol)

print("Forth column is:", meanforthcol)

print('\n')

#Or alternatively you could request a print out of all the columns such as;

print("The mean of each column is:", meanfirstcol, meansecondcol, meanthirdcol, meanforthcol)

print('\n')
