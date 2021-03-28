# Pands-Project2021
Project Repository for Programming and Scripting Module GMIT - 2021

### Introduction
This is a project that is going to look at the data that is commonly known as the Iris Flower Dataset or Fishers Iris dataset. 
During the research phase for this project I found that the study of this dataset seems to be the initial starting point for any would-be statistician or individual interested in studying Machine Learning and/or data visualisation.
The Dataset came to the public forefront in 1936 when statistician Sir Ronal Aylmer Fisher published his report “The Use of Multiple Measurements in Taxonomic Problems” in the journal Annals of Eugenics.
It should be noted that Fisher did not collect the data himself, the data-source was credited to Dr Edgar Anderson who collected the data at the Gaspé Peninsula in Canada.   

The dataset in itself is relatively small - 3 classes (different Iris Species - Iris Setosa, Iris Versicolour and Iris Virginica) with 50 samples of each and 4 variables of each sample (the length and width of the sepal and the length and width of the petal in centimetres). 
One species, Iris Setosa, is "linearly separable" from the other two. This means that we can draw a line between Iris Setosa samples and samples corresponding to the other two species.

From initial research it was clear that this dataset has been analysed in depth by thousands of scholars before me and there was going to be many ways to look at and represent this data.   

https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 
https://github.com/venky14/Machine-Learning-with-Iris-Dataset
https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x

### Planned Project Outcomes
1. To break the project down into small managable tasks  
2. To gain an understanding of the data presented in the Iris Data set
3. To integrate the skills I had aquired over the first 10 weeks of the programming and scripting module to analyse the data and display the findings
4. To expand my knowledge of the python libaries and tools to make the code as simple and readable as possible for the reader
5. To learn how to best optimise my time between research, programming, problem-solving and analysing.  

### The Repository Content
  - README File that contains a description of the dataset and its history. Also includes the tools used in the completion of the project and an explanation of the code and how I proceeded to analyse the data
  - Iris data file. This is the data set that was analysed. This was read by the programs using the PANDAS liberary in python.
  - The prgrams that I used in analysing and displaying the data. These included comments to show my understanding of the code and the were vital when documenting my analytical process.

### Initial Research
As this was my first programming project I found the initial research of this dataset a little daunting.
There were so many ways that that this data had been previously researched and visualised in a range of disiplines - Statistics, Machine Learning, Data Representation, Data Visulaisation to name a few. It was difficult to wrap my head around how this seemingly simple set of flower types and their four common, but variable attributes, were a recognised building block of some of the most intricate and complex tools that are used in computing and data science today.
After some initial headscratching google searchs I decided to start at the beginning and have a look at Fishers origial report - this helped a little as it really showed me he was just looking at these 150 flowers as a specific data set and not trying to gleen any information that was not already supplied by the numbers provided to him, even if some of the mathamathics involved was beyond my comprehension. From my reading of the original report, Fisher seemed to be outlining that by interpreting the data from these 3 species of Iris', we could identify the species of any of these iris' by using the measurements of the Sepal and Petal. 
This gave me a little confidence in the sense that I should just start from the begining with no preconcieved notions about what data was going to show me and just begin to use the skills I had aquired in my short time learning python to generate a picture of what the data was trying to display. I could dive into the further uses for how the method of my analysis could be used in other applications at a later time.

Once I felt I had done adaquete research on what the data was I decided to try some simple code to output some plots, if for nothing else to have some "physical" evidence that I was making progress. The first decision I had to make was how did I want to have the data stored. I decided CSV was my best option - I was familiar with the CSV format from some light database work I had done in my professional life (importing and exporting data mainly - no real analysis) and this would be the format I would be continuing to use professionaly, so that decision was one of the easier ones I would make.
From there I did some more research and reviewed some previous labs that had touched on CSV data during the course. There was so much I decided to create a new bookmarks foler in Chrome called "Pandas Project Bookmarks" - and I edited the names so it was clear what the bookmark was for(this was not always clear by the URL or given heading).

### First Analysis
 The first thing I did  was jump into making histograms and scatter plots and try to study them to get some insight into the data.  I quickly realised this was a mistake as I was not really able to analyse the pictures as I had not summarised the basic data behind the graphs I was generating.
 I found an extremly useful function in the pandas libary called describe().  This gave me some basic statistics on the data set such as mean, max, min and standard deviations.
 From these figures I could begin to do some early analysis.
  - The biggest gap between the min and max values were in the petal lengths and sepal lengths - this held through with the varience in the standard diviation.
  - From the Mean data I could see that sepal lenght and widths were, in relitive terms, significatly larger than the petal counterparts
  - Standard Deviations showed that there was slightly higher varience in the petal lenght and width than the sepal lenght and width - because of this higher varience level I began to wonder if the petal data was going to show me a clearer picture of the difference between species than the sepal data - more analyis would be required.

  
 
  



### Citations
https://www.datacamp.com/community/tutorials/histograms-matplotlib 
https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d 
https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x 
https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/ 
https://www.kaggle.com/vasanthreddy/data-visualisation-of-iris-dataset 

