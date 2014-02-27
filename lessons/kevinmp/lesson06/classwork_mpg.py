import pandas as pd 
import numpy as np
from sklearn import linear_model, feature_selection

cars = pd.read_csv('cars93.csv')
cars = cars.drop('AirBags', axis=1)
cars = cars.drop('DriveTrain', axis=1)
cars = cars.drop('Cylinders', axis=1)
cars = cars.drop('Man.trans.avail', axis=1)
cars = cars.drop('Origin', axis=1)
cars = cars.drop('Make', axis=1)
cars = cars.drop('Manufacturer', axis=1)
cars = cars.drop('Model', axis=1)
cars = cars.drop('Type', axis=1)

cars = cars.dropna()

MPGcity = cars[['MPG.city']]
MPGhighway= cars[['MPG.highway']]
features = cars.drop('MPG.city', axis=1)
features = features.drop('MPG.highway', axis=1)

print "Feature selection (MPG Highway):", feature_selection.univariate_selection.f_regression(features, MPGhighway)
print "Feature selection (MPG City):", feature_selection.univariate_selection.f_regression(features, MPGcity)

# use the best valued features
features = features[['Min.Price','Fuel.tank.capacity','Weight']]

lregr = linear_model.LinearRegression()
lregr.fit(features, MPGcity)
print "Linear Regression Score (MPGcity): ", lregr.score(features,MPGcity)

lregr2 = linear_model.LinearRegression()
lregr2.fit(features, MPGhighway)
print "Linear Regression Score (MPGhighway): ", lregr2.score(features,MPGhighway)
