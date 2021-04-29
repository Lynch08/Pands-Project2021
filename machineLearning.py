
#This is an example of machine learning using a decision tree classifier algorithm on the IrisData Set
#Author: Enda Lynch
#Code Adapted from former pands student Gareth Duffy - see citation #12 in README

from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()
data= iris.data
target = iris.target

# classification model - decision tree classifier algorithm
classType = tree.DecisionTreeClassifier() 

# Model will use the existing Iris data to "learn" or "train itself" to make a prediction
classType = classType.fit(data, target) # classType.fit method uses existing Iris data to predict "target" species

# Test the classifier model

seplen = input("Please enter sepal length: ") # Input user prompt
sepwid = input("Please enter sepal width: ")
petlen = input("Please enter petal length: ")
petwid = input("Please enter petal width: ")

attrArr = [float(seplen), float(sepwid), float(petlen), float(petwid)]
flower = [attrArr]

flowerType = " " 

if classType.predict(flower) == [0]: # .predict function will estimate based on newly inputted flower measurements.
	flowerType = "Setosa"
elif classType.predict(flower) == [1]:
	flowerType = "Versicolor"
elif classType.predict(flower) == [2]:
	flowerType = "Virginica"

scores = cross_val_score(classType, data, target, cv=10)

result = "The flower is most likely an Iris " + flowerType # Output from Iris classifier learning model
acc = "Accuracy of prediction: %.2f (+/- %.2f)" % (scores.mean()*100, scores.std()*200) # gives us an accuracy score with confidence intervals

print(result) #Prints result
print(acc) # Prints out accuracy estimate 
