import pandas as pd
from sklearn import naive_bayes, cross_validation, metrics
from sklearn.feature_extraction.text import CountVectorizer

train = pd.read_csv('train-utf8.csv')
values = train['Insult']

vectorizer = CountVectorizer()
train = vectorizer.fit_transform(train['Comment'].values)

nb = naive_bayes.MultinomialNB().fit(train, values)
print "Score on training data set:", nb.score(train, values)
print "Cross validation scores on training data set:", cross_validation.cross_val_score(nb, train, values)
