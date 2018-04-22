
<h1><em><strong>A STUDY ON " THE IRIS FLOWER DATA SET " </h1></em></strong><br/>

</br>



<h2><em> PROJECT REPORT - Submitted by: </h2></em>
<h3><em> Valerie Walsh - Student Number: G00364748 </h3></em>

</br>

<h3> Programming & Scripting - Higher Diploma in Data Analytics - Galway Mayo I.T. </h3> </br>
<h3>Submission Date: April 2018 </h3> </br>

</br>

<h2><em>Table of Contents </h2></em>

1.	Introduction <br>
1.1.	Statement of Work <br>
1.2.	Technology Used <br>
2.	Discussion <br>
2.1.	Background <br>
2.2.	 Preparation <br>
2.3.	 Investigation <br>
3.	Summary <br>
4.	Appendix <br>
5.	Bibliography <br>
</br>


<h2><strong> 1.	Introduction </h2></strong> <br>

This repository has been created for me to record and show my work as I build and submit my project.
I created a gitignore file and a LICENCE (Apache) based on my knowledge of creating my original repository for my weekly course tasks.

The purpose of this project is to investigate "The Iris Flower Data Set" [1] and prove my understanding of the data set and explain its importance to machine learning. This has been undertaken as apart of a final submission for a course subject as apart of my Diploma in Computer Science with Data Analytics.
I intend to investigate, research and produce my findings via this submission. My goal for this project is to provide education within the field of machine learning so as to provide knowledge to those interested in understanding it in more detail.
This project has been approached with the intention of researching all information of the Iris Flower Data Set, write and run scripts to test the set within Python and then provide written support of my view of the data set.
[1] https://sourceforge.net/projects/irisdss/files/IRIS.csv/download
</br>
<h2><strong>1.1) Statement of Work </h2></strong> <br>


This is a statement to confirm that the submitted work is all my own which has been formulated with the aid of online research where all references have been included and mentioned where appropriate.
Valerie Walsh </br>

<h2><strong> 1.2) Technology Used</h2></strong> <br>

For this project I heavy utilized the Python Programming Language [1] and GitHub [2] , along with various online resources which have been referenced at each mention. { [1] https://www.python.org/ , [2] https://github.com/ } </br>

Prior to writing and running any scripts, you will want to ensure that the required software is installed. For this project I used the software called Anaconda. I have used this software throughout my course to date and find it extremely user-friendly. Anaconda can be downloaded via: ‘https://www.anaconda.com/’.

Throughout the usage of Anaconda and Python, I have used built in libraries which I imported when appropriate.
I have created a folder titled Screenshots and inside this there is a screenshot showing the libraries I imported at the beginning of this project. I obtained this list from another source online which can be found here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ .
I also relied heavily on the use of Numpy for completing calculations and plotting.

<h2><strong>2. Discussion</h2></strong>
<h2><strong>2.1 Background</h2></strong> <br>

The Iris Flower Data Set was created by Ronald Fisher in 1936. It is described as a multivariate data set as an example of linear discriminant analysis. It is a data set which consists of 50 samples taken from three species of the Iris flower. The four features used for this data set include the length and width of the sepals and petals.

The background and the creation of the Iris Flower Data Set is documented on the Wikipedia page for this topic [1]:
“The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper “The use of multiple measurements in taxonomic problems” as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, picked on the same day and measured at the same time by the same person with the same apparatus".
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.”
[1] https://en.wikipedia.org/wiki/Iris_flower_data_set

The Iris Flower Data Set itself is extremely popular and utilized as a testing tool within machine learning. Part of its popularity I believe, is due to its reliabillity and ease of use. 
One contributor on Stackflow descirbed the reasons for its high accuracy: <br>
<em>"(a) there are few features to begin with and (b) that there are high linear correlations with class, would all point to a less complex, linear function as being the appropriate predictive model-- by using a single hidden node, you are very nearly using a linear model.
It can also be noted that, in the absence of any hidden layer (i.e., just input and output nodes), and when the logistic transfer function is used, this is equivalent to logistic regression."</em>
<br><br>
While another contributor responded to the same post with a sample test for the data set: <br>
<em>" The Iris data set can even be predicted with a very high accuracy (96%) by using just three simple rules on only one attribute:
If Petal.Width = (0.0976,0.791] then Species = setosa
If Petal.Width = (0.791,1.63]   then Species = versicolor
If Petal.Width = (1.63,2.5]     then Species = virginica " </em> <br>
[2] https://stackoverflow.com/questions/36967126/why-do-i-get-good-accuracy-with-iris-dataset-with-a-single-hidden-node
<br><br>
<h2><strong>2.2 Preparation</h2></strong> <br>

During my research, I found a website tutorial which provides a step-by-step guide preparation guide for beginners to Machine Learning with Python and also runs similar scripts to what I want to achieve in my own project. You will see further references of this site throughout my project where I will work with and add to those scripts to create my own outputs: [1] - https://machinelearningmastery.com/machine-learning-in-python-step-by-step/


<h2><strong>2.3 Investigation</h2></strong> <br>

Prior to producing this project, I made a decision to create a project management plan so that I was organised and could show regular contributions to my repository.
My plan included:
- Create the repository
- Research the topic of interest online and document all references / links that may be used in the project 
- Created a Word document on my laptop, where I predominantly wrote the text based content for the project before inserting it into the ReadMe file
- Created a dedicated reference section within ReadMe where I ensured to add all links to ensure correct recognition is given for supporting work
- Created specially dedicated folders to add files to as I work
- Ensure to regularly update the ReadMe file to ensure accuracy 


<h2><strong>3. Summary</h2></strong> <br>

To summarize my findings, I come to notice similar points being made about the Iris Data Set from those who have completed similar research:  
- This is a popular data set for use within Machine Learning
- Due to its small size (4 algorithms and 150 rows) it easily fits into memory (and on an A4 page) { https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ }
- High accuracy levels 

I have learned a great deal since having undertaken this project. Prior to commencing this course in January, I had no previous programming experience and found the weekly tasks challenging. 
With this project and the time limit given, I did find it daunting but also extensively rewarding. 
The videos supplied on the Moodle page were invaluable based on the knowledge and skills it provided to me.
Also it is amazing how many open sites are avaiable and the extent to which the Iris Data Set is used in modern machine learning. 
I am proud of the work which I have produced to date and look foward to adding to it as my knowledge progresses.

During my research, I did come across some indepth scripts and code which I believe would have added to my project but as I do not understand the work, I feel it would be slightly 'over my head' to explain it, should I need to. 
I have however included the references so that they will be there for further review.

<h2><strong>4. Appendix</h2></strong> <br>

My appendix for this project is located within the repository itself. 


<h2><strong>5. Bibliography</h2></strong> <br>

https://stackoverflow.com/questions/14494747/add-images-to-readme-md-on-github - how to add images to ReadMe file

https://gist.github.com/curran/a08a1080b88344b0c8a7 - GitHub info on python 

https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ - Step by step of how to do a project with python 

https://rpubs.com/rpadebet/269829 - Using R but interesting project steps layout 

https://gist.github.com/naufraghi/457394 - Python and Iris Data Set (possibly too in-depth)

https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342 - Analysis of Iris Data Set & some history 

https://plot.ly/python/histograms/ - Python histograms - how to

https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data Histograms - How to 

https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib

https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5#skiponboarding

https://www.tutorialspoint.com/python/python_lists.htm  - how to lists max min 


EXAMPLES OF DATA print outs

https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

http://www.learn4master.com/algorithms/visualize-iris-dataset-using-python

https://www.kaggle.com/benhamner/python-data-visualizations

http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

https://stackoverflow.com/questions/21548750/plotting-histograms-against-classes-in-pandas-matplotlib

