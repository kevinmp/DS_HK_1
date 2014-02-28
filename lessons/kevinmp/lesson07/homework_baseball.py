import pandas as pd
import numpy as np
from sklearn import linear_model, feature_selection

bb = pd.read_csv('baseball.csv')
# does handedness correlate to salary?
dummies  = pd.get_dummies(bb['bats'],prefix='hand')
features = bb[['G','AB','R','H','X2B','X3B','HR','RBI','SB','CS','BB','SO','IBB','HBP','SH','SF','salary']].join(dummies)
features = features.dropna(axis=0)
salary = features[['salary']]
del features['salary']
print "Feature selection:", feature_selection.univariate_selection.f_regression(features, salary)
lregr = linear_model.LinearRegression()
lregr.fit(features, salary)
print "Linear Regerssion Score: ", lregr.score(features,salary)
print lregr.predict(features)

