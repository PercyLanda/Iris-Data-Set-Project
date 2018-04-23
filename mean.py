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

# Reference: https://www.tutorialspoint.com/python/list_min.htm
# An alternative and cleaner solution which I found to the above is;

print("The mean of each column is:", meanfirstcol, meansecondcol, meanthirdcol, meanforthcol)

print('\n')
