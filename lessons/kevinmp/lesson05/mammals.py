# linear regression for standard brain - body data
regr = linear_model.LinearRegression()
body = [[x] for x in mammals['body'].values]
brain = mammals['brain'].values
regr.fit(body, brain)
regr.score(body, brain)
plt.scatter(body, brain)
plt.plot(body, regr.predict(body), color='blue', linewidth=3)
plt.show()

# linear regression for natural log brain - body data
log_body = [[x] for x in mammals['log_body'].values]
log_brain = mammals['log_brain'].values
regr.fit(log_body, log_brain)
regr.score(log_body, log_brain)
plt.scatter(log_body, log_brain)
plt.plot(log_body, regr.predict(log_body), color='blue', linewidth=3)
plt.show()

# linear regression plotting log vs non-log brain - body data
regr = linear_model.LinearRegression()
regr2 = linear_model.LinearRegression()
body = [[x] for x in mammals['body'].values]
brain = mammals['brain'].values
regr.fit(body, brain)
regr.score(body, brain)
log_body = [[x] for x in mammals['log_body'].values]
log_brain = mammals['log_brain'].values
regr2.fit(log_body, log_brain)
regr2.score(log_body, log_brain)
plt.scatter(body, brain)
plt.scatter(log_body, log_brain)
plt.plot(body, regr.predict(body), color='red', linewidth=3)
plt.plot(exp(log_body), exp(regr2.predict(log_body)), color='blue', linewidth=3)
plt.show()

