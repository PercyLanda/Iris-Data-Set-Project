# Valerie Walsh 2018-04-22
# Iris Data Set project
# Reference: Topic 7 videos
# Calculate the min of each column

import numpy
data = numpy.genfromtxt('iris.csv', delimiter=',')

minfirstcol = numpy.min(data[:,0])
minsecondcol = numpy.min(data[:,1])
minthirdcol = numpy.min(data[:,2])
minforthcol = numpy.min(data[:,3])

print('\n')

print("First column min is:", minfirstcol)

print("Second column min is:", minsecondcol)

print("Third column min is:", minthirdcol)

print("Forth column min is:", minforthcol)

print('\n')

#Or alternatively you could request a print out of all the columns such as;

print("The min of each column is:", minfirstcol, minsecondcol, minthirdcol, minforthcol)

print('\n')
