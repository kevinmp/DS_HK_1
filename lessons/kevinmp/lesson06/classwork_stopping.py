import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, feature_selection

cars = pd.read_csv('cars1920.csv')
speed = cars[['speed']]
distance = cars[['dist']]

print "Feature selection:", feature_selection.univariate_selection.f_regression(speed, distance)

lregr = linear_model.LinearRegression()
lregr.fit(speed, distance)
print "Linear Regerssion Score: ", lregr.score(speed,distance)


rregr = linear_model.Ridge()
rregr.fit(speed, distance)
print "Ridge Regerssion Score: ", rregr.score(speed,distance)

plt.scatter(speed, distance)
plt.plot(speed, lregr.predict(speed), color='blue')
plt.plot(speed, rregr.predict(speed), color='red')
plt.show()
