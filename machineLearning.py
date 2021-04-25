
from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()
data= iris.data
target = iris.target

# classification model
classType = tree.DecisionTreeClassifier() 

# Train the model with the existing Iris data
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
acc = "Accuracy: %.2f (+/- %.2f)" % (scores.mean()*100, scores.std()*200) # gives us an accuracy score with confidence intervals

print(result, end= ', ') # "end=" used to place a space after the displayed string instead of a newline.
print(acc) # Prints out accuracy estimate 
