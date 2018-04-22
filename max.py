# Valerie Walsh 2018-04-22
# Iris Flower Data Set

#Max of each column

import numpy
data = numpy.genfromtxt('iris.csv', delimiter=',')

maxfirstcol = numpy.max(data[:,0])
maxsecondcol = numpy.max(data[:,1])
maxthirdcol = numpy.max(data[:,2])
maxforthcol = numpy.max(data[:,3])

print("First column max is:", maxfirstcol)

print("Second column max is:", maxsecondcol)

print("Third column max is:", maxthirdcol)

print("Forth column max is:", maxforthcol)
