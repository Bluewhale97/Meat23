#import packages
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, discriminant_analysis
from sklearn.model_selection import train_test_split 

# logreg
sklearn.linear_model.LogisticRegression()

##Params
# penalty: l1,l2,...
# dual: bool. True using dual type for maximum livelihood, only penalty='l2' and solver='liblinear' has dual type. False using original type
# C: 1/alpha
# fit_intercept: bool, True for computing b
# intercept_scaling: float, only meaniful while solver='liblinear'. When fit_intercept=True, that means munually creating a feature that is always 1 and the weight is b, for mitigating the impact from this man-made feature, we need intercept_scaling
# class_weight: a dictionary or string 'balanced': dictionary to grant weight for every class: {class_label:weight}; 'balanced': every class has balanced weight; if nothing assined, every class has weight "1"
# max_iter
# random_state
# solver: 1. 'newton-cg': newton solver 2. 'lbfgs': use L-BFGS 3. liblinear: use liblinear, it is good for small dataset 4. 'sag': stochastic average gradient descent, it is good for big dataset...'newton-cg','lbfgs', 'sag' are only solve with penalty='l2'
# tol: float for threshold of convergence
# multi_class: a string, for multi-class scenario, 'ovr': using one-vs-rest strategy whereas 'multinomial': use multi-class logistic strategy
# verbose: positive integer, open or close log for iteration
# warm_start: bool, True for using results from previous iteration to continue training
# n_jobs: positive integer, assign the amount of CPU, -1 using all available CPUs

##Attributes:
# coef_
# intercept_
# n_iter_

##Methods:
# fit(X,y)
# predict(X)
# predict_log_proba(X): the log probability for every class of the label variable
# predict_proba(X): the probability of every class of the label variable
# score(X,y): the accuracy

# logreg case
# 150 data points, 3 classes, 4 features

def load_data():
  iris = datasets.load_iris()
  X_train=iris.data
  y_train=iris.target
  return train_test_split(X_train, y_train, test_size=.25, random_state=0, stratify=y_train)

# here using stratification sampling, because the first 50 are class 0, the middle 50 are class 1 and rest points are class 2


def test_LogisticRegression(data):
  X_train, X_test, y_train, y_test=data
  regr = linear_model.LogisticRegression()
  regr.fit(X_train, y_train)
  print('Coefficients:%s, intercept %s '%(regr.coef_, regr.intercept_))
  print('Score:%.2f'% regr.score(X_test, y_test))
  
# the impact from multi_class parameter
def test_LogisticRegression_multinomial(data):
  X_train, X_test, y_train, y_test=data
  regr = linear_model.LogisticRegression(multi_class='multinomial',solver='lbfgs')
  regr.fit(X_train, y_train)
  print('Coefficients:%s, intercept %s '%(regr.coef_, regr.intercept_))
  print('Score:%.2f'% regr.score(X_test, y_test))
  
test_LogisticRegression_multinomial(data=load_data()) # the multi-class strategy actually can benefit the accuracy

# test of C
def test_LogisticRegression_C(data):
  X_train, X_test, y_train, y_test=data
  Cs = np.logspace(-2,4,num=100)
  scores=[]
  for C in Cs:
    regr = linear_model.LogisticRegression(C=C)
    regr.fit(X_train, y_train)
    scores.append(regr.score(X_test, y_test))

# plotting

scores = test_LogisticRegression_C(data=load_data())
fig =plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(Cs, scores)
ax.set_xlabel(r"C")
ax.set_ylabel(r"score")
ax.set_xscale('log')
ax.set_title('logreg')
plt.show()
