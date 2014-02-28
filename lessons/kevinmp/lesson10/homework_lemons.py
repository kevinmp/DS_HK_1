import pandas as pd
from sklearn import tree, cross_validation

# read csv data
train = pd.read_csv('lemon_training.csv')

# drop nan and non-numeric data
train = train.dropna(axis=1)
train = train._get_numeric_data()

# pull out the result set and remove the unneeded columns
values = train['IsBadBuy']
del train['RefId']
del train['IsBadBuy']

clf = tree.DecisionTreeClassifier()
clf.fit(train, values)
print "Score on training data set:", clf.score(train, values)
print "Cross validation score on training data set:", cross_validation.cross_val_score(clf, train, values)
