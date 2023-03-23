#import packages
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, discriminant_analysis
from sklearn.model_selection import train_test_split 

#sklearn.model_selection.train_test_split
def load_data():
  diabetes = datasets.load_diabetes()
  return train_test_split(diabetes.data, diabetes.target,test_size=.25, random_state=0)
  
# Lasso regressor
sklearn.linear_model.Lasso(alpha=1.0, fit_intercept=True, normalize=False, 
                          precompute=False, copy_X=True, max_iter=1000,
                          tol=0.0001, warm_start=False)

## Params:
# alpha: alpha value
# fit_intercept: bool, True to compute b
# max_iter
# copy_X
# precompute: bool or a procession, whether to compute Gram for speeding up training
# tol: float for threshold of convergence
# warm_start: bool, True to use result of the previous time to continue training, otherwise get back to restart
# positive: bool, True for every feature's param should be positive
# selection: a string, could be either 'cyclic' or 'random', to choose which feature's param to update in every iteration
# random_state: an integer or an instance, or None, None using default randomizer 

## Attribute:
# coef_: param vectors of features
# intercept_: b value
# n_iter_: actual iterations

## Methods:
# fit(X, y)
# predict(X)
# score(X,y) # higher is better


# test lasso
data = load_data()

def test_Lasso(data):
  X_train, X_test, y_train, y_test = data
  regr = linear_model.Lasso()
  regr.fit(X_train, y_train)
  print("Coefficients:%s, intercept %.2f"%(regr.coef_,regr.intercept_))
  print("Residual sum of squares: %.2f"%np.mean((regr.predict(X_test) - y_test)**2))
  print('Score:%.2f'% regr.score(X_test, y_test)) 
  
test_Lasso(data=data)

# test alpha to Lasso
def test_Lasso_alpha(data):
  X_train, X_test, y_train, y_test=data
  alphas = [.01,.02,.05,.1,.2,.5,1,2,5,10,20,50,100,200,500,1000]
  scores=[]
  for i, alpha in enumerate(alphas):
    regr = linear_model.Lasso(alpha=alpha)
    regr.fit(X_train, y_train)
    scores.append(regr.score(X_test, y_test))
  return alphas, scores
  
alphas, scores = test_Lasso_alpha(data=data)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(alphas, scores)
ax.set_xlabel(r"$\alpha$")
ax.set_ylabel(r"score")
ax.set_xscale('log')
ax.set_title("Lasso")

