# Valerie Walsh 2018-04-22
# Iris Flower Data Set

#Min of each column

import numpy
data = numpy.genfromtxt('iris.csv', delimiter=',')

minfirstcol = numpy.min(data[:,0])
minsecondcol = numpy.min(data[:,1])
minthirdcol = numpy.min(data[:,2])
minforthcol = numpy.min(data[:,3])

print("First column min is:", minfirstcol)

print("Second column min is:", minsecondcol)

print("Third column min is:", minthirdcol)

print("Forth column min is:", minforthcol)
