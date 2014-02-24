#Review: An Inference Model for Online Media Users by Narameth Nananukul published in Journal of Data Science 11 (2013)


##Abstract
This paper is about using logistic regression to infer demographics about a viewing population on an online video streaming website. The purpose is to extrapolate the demographic of a particular user from his / her viewing habits so as to be better able to target ads to that user.
#####Hypothesis
The hypothesis is that there is applicable difference between the genre preferences and and viewing time between different age / gender groups and collaborative filtering would be able to provide a way to infer a users profle based on his / her viewing history.

##Style
It could be just me but this paper doesn't seem to be targeted at any particular reader. Perhaps it was submitted summarily as part of the authors student work? The way it is written doesn't make clear who the intended audience is.

##Methods
Viewing data was gathered over a 1-month period from an unnamed media provider in the US. It is implied that the demographic data from user registration were matched to the viewing data.

Of the dataset collected, 80% was used as a training set and 10% as a test set.

It appears that the features / factors in the data were flatten to discrete variables (1/0). The features were then selected based on their P-value relationship to the output. P-values with 0.1 and better were selected for fitting.

The interaction terms were decided using the Akaike Information Criterion values. If I read this right, the author ran regression using R which automatically deleted or included features until they got a good AIC value. (*Note: not a staistics major. Need more research and explanation on interaction terms / interaction variables* )

As the author is using Logistic Regression, the author is testing each user against a single Inferred Probablity (IP) demographic grouping, meaning the author has to run a test for each user against each IP, which will reveal a P-statistic on the chances that the user belongs to that IP.


##Conclusions
This is not a very clearly written paper. The hypotheses and conlcusions are not very clearly spelt out. Or is this how most acadamic papers couch their terms? 

If I read it right, the author states that they can improve inference accuracy by using genre-ratio and usage-levels. They also state that they managed to reduce noise by using thrsholds to trim the data. That sounds like the author was reducing the data into quartiles or simply into binary by cutting them off at abitarily defined "thresholds". The paper doesn't go on to define what those "thresholds" are.

The paper presents the data of the male, age 45-54, as the results of the expriment. The presented IP deviations and scores are derived from the above dataset. It is not clear if other demographic data has the same result i.e. would running the regression on a dataset of females aged 25-34 have the same results, thus proving that we have a model we can use to infer demographics from viewer histories?

I'm not sure if I'm really bad at reading journal articles or if I picked a badly presented article to read.

