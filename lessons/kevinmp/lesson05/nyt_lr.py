# linear regression on nyt data with age as the predictor
nytdata = pd.read_csv('nyagg.csv')
nytregr = linear_model.LinearRegression()
age = [[x] for x in nytdata['Age'].values]
ctr = nytdata['Ctr'].values
nytregr.fit(age, ctr)
nytregr.score(age,ctr)
nytregr.coef_
plt.scatter(age, ctr)
plt.plot(age, nytregr.predict(age), color='blue', linewidth=3)
plt.show()

# linear regression on nyt data with age as the predictor, only males (assuming gender=1 as male)
nytdata = pd.read_csv('nyagg.csv')
nytdata = nytdata[nytdata["Gender"]==1]
nytregr = linear_model.LinearRegression()
age = [[x] for x in nytdata['Age'].values]
ctr = nytdata['Ctr'].values
nytregr.fit(age, ctr)
nytregr.score(age,ctr)
plt.scatter(age, ctr)
plt.plot(age, nytregr.predict(age), color='blue', linewidth=3)
plt.show()

# linear regression on nyt data with age as the predictor, only females (assuming gender=0 as female)
nytdata = pd.read_csv('nyagg.csv')
nytdata = nytdata[nytdata["Gender"]==0]
nytregr = linear_model.LinearRegression()
age = [[x] for x in nytdata['Age'].values]
ctr = nytdata['Ctr'].values
nytregr.fit(age, ctr)
nytregr.score(age,ctr)
plt.scatter(age, ctr)
plt.plot(age, nytregr.predict(age), color='blue', linewidth=3)
plt.show()

# linear regression with 2 features (gender, age)?
# eh, I have no idea what I'm doing here... 
# no, really. what does this code below do?
# grab statsmodel package
import statsmodels.api as sm
nytdata = pd.read_csv('nyagg.csv')
y = nytdata['Ctr'].values
# populate predictor data and constant
X = nytdata[['Age','Gender']]
X = sm.tools.add_constant(X)
est = sm.OLS(y,X).fit()
est.summary()
plt.scatter(X['Age'], y)
plt.plot(X['Age'], est.predict(X), color='blue', linewidth=3)
plt.show()

