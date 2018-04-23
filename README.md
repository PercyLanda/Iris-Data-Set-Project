
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

This repository has been created to record and show my work as I build and submit my project.
I created a gitignore file and a LICENCE (Apache) based on my knowledge of creating my original repository for my weekly course tasks.

The purpose of this project is to investigate "The Iris Flower Data Set" and prove my understanding of the data set and explain its importance to machine learning. This project is being undertaken as apart of a final submission for the subject 'Programming and Scripting' as apart of my Diploma in Computer Science with Data Analytics.

I intend to investigate, research and produce my findings via this submission. My goal for this project is to provide education within the field of machine learning so as to provide knowledge to those interested in understanding it in more detail.
This project has been approached with the intention of researching all information of the Iris Flower Data Set, write and run scripts to test the set within Python and then provide written support of my view and knowledge of the data set.

</br>
<h2><strong>1.1) Statement of Work </h2></strong> <br>

This is a statement to confirm that the submitted work is my own which has been formulated with the aid of online research, where all references have been included and mentioned where appropriate.
Valerie Walsh </br>


<h2><strong> 1.2) Technology Used</h2></strong> <br>

* Anaconda
* Visual Studio Code
* Python Programming Language
* GitHub
* Moodle page - internal college site used to access class notes and videos 

Prior to writing and running any scripts, you will want to ensure that the required software is installed. For this project I used the softwares called Anaconda [1] and Visual Studio Code[2].  I have used both pieces of software throughout my course to date and find them extremely user-friendly.
The Python Programming Language is another download which is heavily utilised and although I must admit it is not the most user-friendly, I am learning to work with it. The key to using Python is to ensure to use what Python recognises e.g. scripts / commands etc and you should work great together. [3].

Since this is the platform for uploading my work, I feel its fitting to mention GitHub [4] as another resource of technology used. GitHub is been described on Wikipedia with this explaination: </br>

<em> GitHub (originally known as Logical Awesome LLC)[3] is a web-based hosting service for version control using git. It is mostly used for computer code. It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.
GitHub offers plans for both private repositories and free accounts[5] which are commonly used to host open-source software projects.[6] As of April 2017, GitHub reports having almost 20 million users and 57 million repositories,making it the largest host of source code in the world.</em>

I also relied heavily on the weekly videos supplied by our lecturer via the Moodle page. I found these invaluable based on the knowledge and skills which they provided to me. 

<br>

<em>{ [1] ‘https://www.anaconda.com/’,  [2] https://code.visualstudio.com/, [3] https://www.python.org/, [4] https://github.com/ }</em>

<h2><strong>2. Discussion</h2></strong>
<h2><strong>2.1 Background</h2></strong> <br>

The Iris Flower Data Set [5] was created by Ronald Fisher in 1936. It is described as a multivariate data set as an example of linear discriminant analysis. It is a data set which consists of 50 samples taken from three species of the Iris flower. The four features used for this data set include the length and width of the sepals and petals.

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Ronald%20Fisher%20image.jpg">
</p>

Here is the background and the creation of the Iris Flower Data Set as per its Wikipedia page:
<br><br>
<em>“The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper “The use of multiple measurements in taxonomic problems” as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, picked on the same day and measured at the same time by the same person with the same apparatus".
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.”</em>[6]

{ [5] https://en.wikipedia.org/wiki/Iris_flower_data_set , [6] https://en.wikipedia.org/wiki/Iris_flower_data_set }


<br><br>
<h2><strong>2.2 Preparation</h2></strong> <br>

Prior to commencing this project, I took the advice of our lecturer and I made a decision to create a project management plan so that I could remain organised and on-top of the work while also ensuring to show regular contributions to my repository with updates and edits.

My project management plan:
- Create the repository with my chosen title 'Iris Data Set Project - 'https://github.com/vwalsh86/Iris-Data-Set-Project'
- Research the topic of interest online and document all references / links that may be used in the project via my ReadMe file.
- Create a folder locally on my laptop where I added images, files and also a Word document. This document was where I predominantly wrote the text based content for the project before inserting it into the ReadMe file
- Created a dedicated reference section within ReadMe where I ensured to add all links to ensure correct recognition is given for supporting work
- Created specifically dedicated folders on my repository to add files to as I work
- Ensure to regularly update the ReadMe file to ensure accuracy and cover all content

The main reason for taking this approach is due to the fact that life can always take over and you can end up running out of time and submitting poor quality work. This is something I hope to have avoided due to the above plan.
<br>
There are additional libraries available to use within Visual Studio Code (VSC), which I found useful when running my code e.g. NumPy, Matplotlib and Pandas. In order to ensure that these are available to you, I would recommend running a script in VSC  which checks the libraries are available. I have provided two images from my own system of me completing this.

Firstly the code that I ran: 

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/test-script-code.PNG">
</p>

And secondly, the output from VSC showing the libraries and their versions:

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/test-script-output.PNG">
</p>

I obtained the list of these libraries via this online source: [7] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ .


<h2><strong>2.3 Investigation</h2></strong> <br>

The Iris Flower Data Set itself is extremely popular and utilized as a testing tool within machine learning. Part of its popularity I believe, is due to its reliabillity and ease of use. 
One contributor on Stackflow descirbed the reasons for its high accuracy: <br><br>
<em>"(a) there are few features to begin with and (b) that there are high linear correlations with class, would all point to a less complex, linear function as being the appropriate predictive model-- by using a single hidden node, you are very nearly using a linear model.
It can also be noted that, in the absence of any hidden layer (i.e., just input and output nodes), and when the logistic transfer function is used, this is equivalent to logistic regression."</em>
<br><br>
While another contributor responded to the same post with a sample test for the data set: <br><br>
<em>" The Iris data set can even be predicted with a very high accuracy (96%) by using just three simple rules on only one attribute:
If Petal.Width = (0.0976,0.791] then Species = setosa
If Petal.Width = (0.791,1.63]   then Species = versicolor
If Petal.Width = (1.63,2.5]     then Species = virginica " </em> <br>
[2] https://stackoverflow.com/questions/36967126/why-do-i-get-good-accuracy-with-iris-dataset-with-a-single-hidden-node

As previously mentioned, my goal for this project was to create and run some codes to prove my knowledge of the topic while also providing information to those interested in learning of the same.


The basic output functions for numerical data such; 
1) how much data is in the file 

2) the 
- The min, max and mean of each column which I have 

<h3><em>Visual graphs of the univariable data</h3></em>

<h4>Histograms</h4>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Data%20Visualisation/Histograms.png">
</p>

<h4>Box and Whisker Plots</h4>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Data%20Visualisation/Box%20Whisker%20Plots.png">
</p>

<h4>Scattor Plot Matrix</h4>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Data%20Visualisation/Scatter%20Plot%20Matrix.png">
</p>

<h4> Improvements</h4>
Improve some previously created scripts as I learned better methods of writing and running the scripts </h3>

<h2><strong>3. Summary</h2></strong> <br>

To summarize my findings, I come to notice similar points being made about the Iris Data Set from those who have completed similar research:  
- This is a popular data set for use within Machine Learning
- Due to its small size (4 algorithms and 150 rows) it easily fits into memory (and on an A4 page) { https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ }
- High accuracy levels 

I have learned a great deal since having undertaken this project. Prior to commencing this course in January, I had no previous programming experience and found the weekly tasks challenging. 
With this project I was required to go out of my comfort zone where I found myself spending considerable time running, testing and tweaking code to produce results. But I am very proud of the content that I have produced, I found it both daunting and extensively rewarding. 
I have gained new skills and confidence with software which was quite new to me (Python and GitHub) and I look forward to adding to it further as my knowledge progresses.

Also it is amazing how many open sites are avaiable and the extent to which the Iris Data Set is used in modern machine learning. 

During my research, I did come across some indepth scripts and code which I believe would have added to my project but given the timeframe and my current skill level, I felt it would be slightly 'over my head' to explain it should I need to. 
I have however included the links as additional references so that they will be there for further review.

<h2><strong>4. Appendix</h2></strong> <br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Ronald%20Fisher%20image.jpg">
</p>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/test-script-output.PNG">
</p>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Copy%20and%20paste%20errors.PNG">
</p>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/test-script-code.PNG">
</p>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/test-script-output.PNG">
</p>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Data%20Visualisation/Box%20Whisker%20Plots.png">
</p>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Data%20Visualisation/Histograms.png">
</p>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Data%20Visualisation/Scatter%20Plot%20Matrix.png">
</p>

<p align="left">
<img src="">
</p>


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

