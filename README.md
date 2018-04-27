
<h1 align="center"><em><strong>A STUDY ON " THE IRIS FLOWER DATA SET " </h1></em></strong><br/>

</br>


<h2 align="center"><em> PROJECT REPORT - Submitted by: </h2></em>
<h3 align="center"><em> Valerie Walsh - Student Number: G00364748 </h3></em>

</br>

<h3 align="center"> Programming & Scripting - Higher Diploma in Data Analytics - Galway Mayo I.T. </h3> </br>
<h3 align="center">Submission Date: 29th April 2018 </h3> </br>

<p align="center">
<img height="350" width="500" src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/iris%20flower.png"
<reference: https://xantheunwinart.deviantart.com/art/iris-flower-289614269>
</p>

<br>
<br>
<br>
<br>

<h2><em>Table of Contents </h2></em>

1.	Introduction <br>
1.1.	Statement of Work <br>
1.2.	Technology Used <br>
2.	Discussion <br>
2.1.	Background <br>
2.2.	 Preparation <br>
2.3.	 Investigation <br>
3.	Summary <br>
3.1 Findings <br>
3.2 Development <br>
3.3 Errors Encountered <br>
4.	Appendix <br>
5.	Bibliography <br>
</br>


<h2><strong> 1.	Introduction </h2></strong> <br>

This repository has been created to record and show my work as I build and submit my project.
In this repository I started out by creating a ReadMe File, a gitignore file and a LICENCE (Apache). I chose these based on my knowledge of creating my original repository for my weekly course tasks.

The purpose of this project is to investigate "The Iris Flower Data Set" and prove my understanding of the data set and explain its importance to machine learning. This project is being undertaken as apart of a final submission for the subject 'Programming and Scripting' as apart of my Diploma in Computer Science with Data Analytics.

I intend to investigate, research and produce my findings via this submission. My goal for this project is to provide education within the field of machine learning so as to provide knowledge to those interested in understanding it in more detail.
This project has been approached with the intention of researching all information of the Iris Flower Data Set, write and run scripts to test the set within Python and then provide written support of my view and knowledge of the data set.

</br>
<h3><strong>1.1) Statement of Work </h3></strong> <br>

This is a statement to confirm that the submitted work is my own which has been formulated with the aid of online research, where all references have been included and mentioned where appropriate.
Valerie Walsh </br>


<h3><strong> 1.2) Technology Used</h3></strong> <br>

* Anaconda
* Visual Studio Code
* Python Programming Language
* GitHub
* Moodle page - internal college site used to access class notes and videos 

Prior to writing and running any scripts, you will want to ensure that the required software is installed. For this project I used the softwares called Anaconda [1] and Visual Studio Code[2].  I have used both pieces of software throughout my course to date and find them extremely user-friendly.
The Python Programming Language is another download which is heavily utilised and although I must admit it is not the most user-friendly, I am learning to work with it. The key to using Python is to ensure to use what Python recognises e.g. scripts / commands etc and you should work great together. [3].

Since this is the platform for uploading my work, I feel its fitting to mention GitHub [4] as another resource of technology used. GitHub is been described on Wikipedia with this explaination: </br>

<em> "GitHub (originally known as Logical Awesome LLC)[3] is a web-based hosting service for version control using git. It is mostly used for computer code. It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.
GitHub offers plans for both private repositories and free accounts which are commonly used to host open-source software projects. As of April 2017, GitHub reports having almost 20 million users and 57 million repositories,making it the largest host of source code in the world."</em> [5]

I also relied heavily on the weekly videos supplied by our lecturer via the Moodle page. I found these invaluable based on the knowledge and skills which they provided to me. In addition to the course information, I also heavily utilised the class 'Discussion Forum' to post queries which were resolved by class members.

<br>

<h2><strong>2. Discussion</h2></strong>
<h3><strong>2.1 Background</h3></strong> <br>

The Iris Flower Data Set [6] was created by Ronald Fisher in 1936. It is described as a multivariate data set as an example of linear discriminant analysis. It is a data set which consists of 50 samples taken from three species of the Iris flower. The four features used for this data set include the length and width of the sepals and petals.

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Ronald%20Fisher%20image.jpg">
</p>

Here is the background and the creation of the Iris Flower Data Set as per its Wikipedia page:
<br><br>
<em>“The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper “The use of multiple measurements in taxonomic problems” as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, picked on the same day and measured at the same time by the same person with the same apparatus".
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.”</em>[6]

The Iris Flower Data Set itself is extremely popular and utilized as a testing tool within machine learning. Part of its popularity I believe, is due to its reliabillity and ease of use. 
One contributor on Stackflow descirbed the reasons for its high accuracy: <br><br>
<em>"(a) there are few features to begin with and (b) that there are high linear correlations with class, would all point to a less complex, linear function as being the appropriate predictive model-- by using a single hidden node, you are very nearly using a linear model.
It can also be noted that, in the absence of any hidden layer (i.e., just input and output nodes), and when the logistic transfer function is used, this is equivalent to logistic regression."</em> [7]
<br><br>
While another contributor responded to the same post with a sample test for the data set: <br><br>
<em>" The Iris data set can even be predicted with a very high accuracy (96%) by using just three simple rules on only one attribute:
If Petal.Width = (0.0976,0.791] then Species = setosa
If Petal.Width = (0.791,1.63]   then Species = versicolor
If Petal.Width = (1.63,2.5]     then Species = virginica " </em> <br> [7]

<br><br>
<h3><strong>2.2 Preparation</h3></strong> <br>

Prior to commencing this project, I took the advice of our lecturer and I made a decision to create a project management plan so that I could remain organised and on-top of the work while also ensuring to show regular contributions to my repository with updates and edits.

My project management plan:
- Create the repository with my chosen title 'Iris Data Set Project - 'https://github.com/vwalsh86/Iris-Data-Set-Project'
- Research the topic of interest online and document all references / links that may be used in the project via my ReadMe file.
- Create a folder locally on my laptop where I added images, files and also a Word document. This document was where I predominantly wrote the text based content for the project before inserting it into the ReadMe file
- Created a dedicated reference section within ReadMe where I ensured to add all links to ensure correct recognition is given for supporting work
- Created specifically dedicated folders on my repository to add files to as I work
- Ensure to regularly update the ReadMe file to ensure accuracy and cover all content

The main reason for taking this approach is due to the fact that life can always take over and you can end up running out of time and submitting poor quality work. This is something I hope to have avoided due to the above plan.
<br><br>
There are additional libraries available to use within Visual Studio Code (VSC), which I found useful when running my code e.g. NumPy, Matplotlib and Pandas. In order to ensure that these are available to you, I would recommend running a script in VSC  which checks the libraries are available. I have provided two images from my own system of me completing this.

Firstly the code that I ran: 

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/test-script-code.PNG">
</p>

And secondly, the output from VSC showing the libraries and their versions:

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/test-script-output.PNG">
</p>

I obtained the list of these libraries via an online source, see reference [8]


<h3><strong>2.3 Investigation</h3></strong> <br>

As previously mentioned, my goal for this project was to create and run some codes to prove my knowledge of the topic while also providing information to those interested in learning of the same.
<br>

Below are the scripts and outputs for each attribute that I have chosen to investigate. I have chosen to include an image of each so as to allow you to review the workings easier and how they relate to each output.
The first image of each section is the script I wrote in Python and the second image is the output via Visual Studio Code.

<h3><em>Exploring the Data</h3></em>

For the first script, I wanted an output of some simple statistics about the data.
I chose to run multiple codes in the one script to show the overview of information in one section.

Below there are two images so as to show all the code included.

<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Basic_script1.png">
</p>

<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Basic_script2.png">
</p>

<br>
<br>

As per the script above, it includes: 
- An overview of the data i.e. how much is in the set in terms of colums and rows.
- The beginning of the data, it is worth noting that you can select the number of lines of data you want it to output.
- A table of statistics for the data e.g. mean, min, max.
- The distribution of data in terms of 'class' - I am aware that it is well known that this particular data set has 3 classes and 50 samples for each but I felt this script would be worthwhile including to show the calculations.
- A script requesting random values of the data set to be outputted.
- Another script requesting random value but this script has limiters set for the outputs.
<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Basic_Data.png">
</p>

<br>

<h3><strong>Calculating the Min, Max and Mean of each column:</strong></h3>

I wrote a seperate code script for each of these attributes and originally I was happy with them and the scripts outputted what I wanted.
However after further research when writing other scripts, I realised that I could improve these codes and merge the 4 column's together into one line of output. This would not only save me time and having to write additional lines of code but it would also making the script look neater.

I have chosen to include both outputs in the script to show you the difference between each option.
With the above in mind, you could remove the code in lines 13-27 to allow the one liner be the output instead in each of the codes.

<h4>Calculating the Minimum</h4>

The below is outputted in the same order as the data file is written: Petal Length, Petal Width, Sepal Length, Sepal Width
<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Min%20Code.png">
</p>
<br>
 
<br>
<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/min.png">
</p>

<br>

<h4>Calculating the Maximum</h4>
<br>

With the maximum outputs from my script, you can see that there is a similar result for both the Petal Length and Sepal Length of 7.9 and 6.9.
Whereas when we calculated the minimum there was a bigger difference between their results: Petal Length 4.3 and Sepal Length 1.0
The petal length is the largest output, followed by sepal length, petal width and sepal width.
<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Max%20code.png">
</p>

<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/max.png">
</p>

<br>

<h4>Calculating the Mean</h4>

<br>
<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Mean%20code.png">
</p>

<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/mean.png">
</p>

<br>
<br>

<h3>Discussing the Min, Max and Mean</h3>

Having reviewed the above information it is clear to see that there is a bigger range of data calculated in the form of sepal lengths among the flowers measured. The sepal length ranges from 1.0 - 6.9 where there is a difference of approx. 5.9cm between the min and max values. 
This would be the category that covers the largest range of the data.
Whereas the other categories range is as follows:
Petal Length - 3.6cm
Petal Width - 2.4cm
Sepal Width - 2.4cm

One explaination for such a big range when it comes to 'Sepal Length' is that the 3 different flower types possibly fall into different sizes on the spectrum e.g  Setosa could be 0-2cm, Versicolor 2-5cm, Virginica 3-6cm. And these differences would have an effect when calcaulating the mean with a larger range to calculate from.
The other areas of data seem to have less of a range where their min, max and means seem to range relatively close to one another.

<br> 

<h3><strong>Visual Graphs of Univariable Data</h3></strong>

<h4>Histogram</h4>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Historgram%20code.png">
</p>
<br>

Having produced histograms for this data, I chose to compare it against the output of the mean attribute.
The mean may not always be a clear or accurate representation of the data, although it does calculate the average figure of the overall data collection, it does not always provide a fair figure. This is where a histogram provides a more accurate depiction by showing a visual breakdown of where the data lies.
<br>
For example, the mean of the <em>Sepal length</em> is 5.843333 but as per the histogram you can see the majority of the data collected ranges from approx 1cm - 6.8cm.

<br>

Also another comparison is the mean of the <em>Petal length</em> is calculated at 3.75866 but the histogram shows a large amount of the data measured at 1cm ad then another cluster at 4-5cm.
This backs the theory that visual data is always going to show you a clearer distribution and representation of the data.

<br>
<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Data%20Visualisation/Histograms.png">
</p>

<br>

<h4>Box and Whisker Plots</h4>

Box Plots are defined on Wikipedia as a good method of showing an accurate view of data:
<br><em>"Outliers may be plotted as individual points. Box plots are non-parametric: they display variation in samples of a statistical population without making any assumptions of the underlying statistical distribution. The spacings between the different parts of the box indicate the degree of dispersion (spread) and skewness in the data, and show outliers."</em> [9]

A advantage that a Box & Whisker Plots has over Histograms is that:
<em>"They take up less space and are therefore particularly useful for comparing distributions between several groups or sets of data."</em> [9]
<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Box%20and%20Whisker%20plot%20code.png">
</p>
<br>
A very interesting step-by-step explaination of what a Box Plot is and also how to create it is found on reference [10].
The Box Plots which I have produced below show the distribution of data for each attribute. <br>
There is a larger range for Petal Length and Petal Width in comparison to the size of the box plot for the Sepal data. The mean of these box's also shows that the mean is now found in the middle but in the higher side of the range.

<br>
<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Data%20Visualisation/Box%20Whisker%20Plots.png">
</p>
<br>

<h4>Pie Chart</h4>

I have included a Pie Chart in my project as I wanted to gain a better understanding of creating graphs via Python. Due to the fact that we already know the data collection, it is expected to have equal measures in all the ranges.<br>

Below is a script I wrote with the help of reference [11]
<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/pie.png">
</p>
<br>

Based on the equal allocation of data for each section with this data set, we can see an even distribution of data with each section of this pie chart.

<br>
<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/pie%20output.png">
</p>

<br>
<br>

<h3>Multivariate Plot</h3>

<h4>Scattor Plot Matrix</h4>

A description of how you view a scatterplot is explained as: <em>"You interpret a scatterplot by looking for trends in the data as you go from left to right"</em> [12] <br>

* If an uphill pattern is viewed as the graph moves left to right, it indicates that a postive relationship exists between the X and Y axis. And as the X-axis value increases the Y-axis value also tends to increase. <br>
* On the other side of this, if the data resembles a downhill pattern then this indicates a negative relationship where as the X-axis increases the Y-axis value tends to decrease. <br>
* If no pattern can be determined based on the data output then no relationship exists between X and Y. <br>
<em>"Note that the scatterplot only suggests a linear relationship between the two sets of values. It does not suggest that an increase in the Y-axis causes the X-axis data to increase." [12]
<br>
"A linear relationship between X and Y exists when the pattern of X– and Y-values resembles a line, either uphill (with a positive slope) or downhill (with a negative slope)." [12]
<br>
"Scatterplots show possible associations or relationships between two variables. However, just because your graph or chart shows something is going on, it doesn’t mean that a cause-and-effect relationship exists."</em> [12]
<br>

As this is my first scatter plot, I researched information to fully understand outputs and the reasons for such.
<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Scattor%20plot%20code.png">
</p>

<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Data%20Visualisation/Scatter%20Plot%20Matrix.png">
</p>

<br>

Based on the above description in relation to uphill or downhill patterns and what they mean, I have concluded the following based on each attribute: <br>

<h6>Sepal Width</h6>
- There is no relationship of any description found between Petal Width and Petal Length.

- A potential to argue a relationship with Sepal Length is present however based on the output, the trend is extremely sporadic. The data goes into an uphill trend but then it drops low and starts again.

<h6>Sepal Length</h6>
- I believe that a positive relationship is present with Petal Length as there is an uphill trend visible.

- Petal Width as although there is a poor start to the data, it does trend upwards as it progresses.
- There is no relationship found with the Sepal Width as the data is scattered as opposed to following one specific trend.

<br>
<h6>Petal Length</h6>
- I found that there is a positive relationship with Petal Width and Sepal Length.
- The data with Sepal Width has no pattern to report, therefore no relationship is present.

<br>
<h6>Petal Width</h6>
- A strong positive relationship is visible with the Petal Length data.
- There is a relationship present with Sepal Length and Sepal Width but the uphill trend only starts further into the data.

<br>

<h4>3D Scatter Plot</h4>

Having created the above scatter plot, I wanted to give a 3D scatter plot a shot.
Unfortunately I was unable to successfully create a 3D based on the data set info, but I did find an interesting 3D scatter plot script online which was created with random values so I have ran this script to include in this project as I hope to revisit and use the data values in the future. Reference [13]

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/3D%20scatter%20code.png">
</p>
<br>
The above code has set value limits of 50 and the script requests random outputs so the below image shows those outputs:
<br>

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/3D%20Scatter.png">
</p>

<br>
<br>

<h2><strong>3. Summary</h2></strong> <br>

I have come to understand that the area of programming is an extremely indepth and complex one, where there are various methods to calculate the same information.
My investigations have only touched the surface with this area and over time I believe that I will be able to revisit and improve my scripts.<br>
Based on my investigations, I have also come to the understanding that graphs are the most reliable method of output when it comes to having a clear and detailed breakdown of the distribution of data. <br>
I have also achieved what I set out to do at the beginning of this project, which was to understand the data set while also learning methods of how to manipulate the data through writing and executing scripts.<br>
In my investigations, I did come across more complex scripts which I wanted to pursue however based on my knowledge and timescale, I chose to reference these in my investigations and I hope to revisit this in the future to execute myself. 

<br>

<h3>3.1 Findings</h3>

To summarize my findings, I come to notice similar points being made about the Iris Data Set from those who have completed similar research:  
- This is a popular data set for use within Machine Learning
- Due to its small size (4 algorithms and 150 rows) it easily fits into memory (and on an A4 page)
- High accuracy levels 


Also it is amazing how many open sites are avaiable and the extent to which the Iris Data Set is used in modern machine learning. 

<br>

<h3>3.2 Development</h3>
I have learned a great deal since having undertaken this project. Prior to commencing this course in January, I had no previous programming experience and found the weekly tasks challenging. 
With this project I was required to go out of my comfort zone where I found myself spending considerable time running, testing and tweaking code to produce results. But I am very proud of the content that I have produced, I found it both daunting and extensively rewarding. 

<br>
During my research, I did come across some indepth scripts and code which I believe would have added to my project but given the timeframe and my current skill level, I felt it would be slightly 'over my head' to explain it should I need to. 

<br>
Upon completing this project I have gained new knowledge and skills which will help me to grow as a developer and more confidence entering into semester 2 of this course later this year.

<br>
Some of the newly attained skills include:

- Discovering and using new libraries within VSC i.e. NumPy, Pandas, Matplotllib.

- Learning how to produce and create visual outputs i.e. histograms, scatter plots, box plots, and also understanding the outputs of each and what they represent.

- Returning to previously written scripts to tweak or improve them based on newly found knowledge e.g. calculating the min and max values.

- Using iPython as an active terminal to test code and outputs before committing them to scripts. 

- Learning new terminology within GitHub itself i.e. learning what 'forking a project' means. This would lead me to believe that my work was seen as a good standard for someone to wish to reference it. 

- Also learning new tips and tricks with using NumPy in Visual Studio Code - using the 'tab' key to view commands available with NumPy.

- I discovered another way to add spacing within Python scripts ('\n') which allowed me to make the script cleaner looking. 

- I have become more confidence with the software of Python and GitHub, and I look forward to adding to it further as my knowledge progresses.
<br><br>

<h3>3.3 Errors Encountered</h3>
There was plenty of errors encountered while creating this project but I shall aim to keep them to a summary for this part of my project.
- Adding images to ReadMe is something that caused me great frustration. I had found the option online to add it via ![image](image.file.name) but this did not work, I attempted to add via a direct link and finally after a week of trying to resolve myself, I posted for help on the internal course Discussion Forum and thankfully my prayeres were answered.

- When creating Box & Whisker plots, I wanted to play around with the layout and see could I get them to appear one per line instead of 2 and 2 so I tried to play with the layout(2,2) part of the code but unfortunately I did not get any further with it

- Writing scripts is something that is still quite new to me so I constantly encounter errors within VSC when I try to get an output. This can be something as simple as forgetting the bracket or " but I am aware this is 100% based on user error and with time I know that I can overcome this obstacle which is adding alot to the length of time it takes me to produce scripts. Thankfully with the internet being as large as it is, I generally find assistance through some open source to resolve my issue.

- Another issue I ran into that threw me was getting errors when I copied code from MS Word into Visual Studio Code. I was writing my scripts within MS Word as my open 'jotter' on my laptop. For some unknown reason when you copy and paste from Word into VSC, you will get inundated with error messages about invald syntax when there is no error. I deleted and manually typed in the same code to resolve this issue and I have included a screenshot showing the errors here:

<p align="left">
<img src="https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/Screenshots/Copy%20and%20paste%20errors.PNG">
</p>

* I had also hoped to create a section to evaluate algorithms however I was unable to get the scripts to run. I have included the .py file in the repository to show my attempts, the file is titled 'validation.py': https://github.com/vwalsh86/Iris-Data-Set-Project/blob/master/validation.py

<br>

<h2><strong>4. Appendix</h2></strong> <br>

<em>All images for this project can be found within the contents of the repository</em>
<br>

<h2><strong>5. Bibliography</h2></strong> <br>

[1] https://www.anaconda.com/ <br>
[2] https://code.visualstudio.com/ <br>
[3] https://www.python.org/ <br>
[4] https://github.com/ <br>
[5] https://en.wikipedia.org/wiki/GitHub <br>
[6] https://en.wikipedia.org/wiki/Iris_flower_data_set <br>
[7] https://stackoverflow.com/questions/36967126/why-do-i-get-good-accuracy-with-iris-dataset-with-a-single-hidden-node <br>
[8] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/ <br>
[9] https://en.wikipedia.org/wiki/Box_plot <br>
[10] https://www.wikihow.com/Make-a-Box-and-Whisker-Plot
[11] https://pythonspot.com/matplotlib-pie-chart/ <br>
[12] http://www.dummies.com/education/math/statistics/how-to-interpret-a-scatterplot/ <br>
[13] https://stackoverflow.com/questions/1985856/how-to-make-a-3d-scatter-plot-in-python <br>

- Image on cover page: https://xantheunwinart.deviantart.com/art/iris-flower-289614269


<br>

<strong><em>Additional references reviewed but not utilised in my project</strong></em>

- https://stackoverflow.com/questions/14494747/add-images-to-readme-md-on-github 

- https://gist.github.com/curran/a08a1080b88344b0c8a7 

- https://rpubs.com/rpadebet/269829 

- https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342  

- https://plot.ly/python/histograms/

- https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data  

- https://stackoverflow.com/questions/45721083/unable-to-plot-4-histograms-of-iris-dataset-features-using-matplotlib

- https://campus.datacamp.com/courses/statistical-thinking-in-python-part-1/graphical-exploratory-data-analysis?ex=5#skiponboarding

- https://www.tutorialspoint.com/python/python_lists.htm  

- https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation

- http://www.learn4master.com/algorithms/visualize-iris-dataset-using-python

- https://www.kaggle.com/benhamner/python-data-visualizations

- http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

- https://stackoverflow.com/questions/21548750/plotting-histograms-against-classes-in-pandas-matplotlib

* https://github.com/bensooraj/Making-predictions-on-the-Iris-Dataset/blob/master/Making%20predictions%20on%20the%20Iris%20Dataset.ipynb
* https://www.kaggle.com/vikrishnan/iris-dataset/data
* https://www.kaggle.com/benhamner/python-data-visualizations
