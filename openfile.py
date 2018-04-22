# Valerie Walsh
# Iris Data Set project*
# Topic 5 Input and Output 07/03/2018
# Exercise Irish Flower Data Set
# The idea to use {:^6} came from reviewing = https://pyformat.info/ - Padding and aligning strings
# The order of the values is as per the wording of the Exercise requirements - Petal length, Petal Width, Sepal Length, Sepal Width
# Made multiple attempts to name the columns but failed, left in the coding to show my attempt - https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas

# *Update 22-04-2018 - Added this file to my repository as this was an exercise on the same data set that I completed back in Week 5's exercise.
# The output produced nice spacing between columns

with open("iris.csv") as f:
    columns = ['Sepal-Length', 'Sepal-Width', 'Petal-Length', 'Petal-Width', 'class']
    for line in f:
        print('{:^6} {:^6} {:^6} {:^6}'.format(line.split(',')[2], line.split(',')[3], line.split(',')[0], line.split(',')[1]))
    
