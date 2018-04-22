# Valerie Walsh 2018-04-22
# Iris Flower Data Set

#Mean of each column

import numpy
data = numpy.genfromtxt('iris.csv', delimiter=',')

meanfirstcol = numpy.mean(data[:,0])
meansecondcol = numpy.mean(data[:,1])
meanthirdcol = numpy.mean(data[:,2])
meanforthcol = numpy.mean(data[:,3])

print("First column is:", meanfirstcol)

print("Second column is:", meansecondcol)

print("Third column is:", meanthirdcol)

print("Forth column is:", meanforthcol)
