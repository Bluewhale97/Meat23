#import packages
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, discriminant_analysis
from sklearn.model_selection import train_test_split 

#sklearn.model_selection.train_test_split
def load_data():
  diabetes = datasets.load_diabetes()
  return train_test_split(diabetes.data, diabetes.target,test_size=.25, random_state=0)

# Ridge Regression
from sklearn.linear_model import Ridge

Ridge()

# Parameters
# alpha: parameter of regularization
# fit_intercept: compute b or not
# max_iter: biggest times of iteration, if set None, use default value(different solver has different default set value)
# normalize: bool, True than normalizing before training
# copy_X
# solver: 
## 1. auto: auto-select solver
## 2. svd: 
## 3. cholesky: use scipy.linalg.solve
## 4. sparse_cg: use scipy.sparse.linalg.cg
## 5. lsqr: scipy.sparse.linalg.lsqr
## 6. sag: use stochastic average gradient descent
## 7. tol: float, for threshod of convergence
## 8. random_state: None or an instance, using it when solver=sag. None means using default random state. instance means using designated random state

# Attributes:
# coef_:features' params
# intercept_: value of b
# n_iter: actual times of iterations


# Methods:
# fit(X, y[,sample_weight])
# predict(X)
# score(X, y[,sample_weight])

def test_Ridge(data):
  X_train, X_test, y_train, y_test = data
  regr = linear_model.Ridge()
  regr.fit(X_train, y_train)
  print("Coefficients:%s, intercept %.2f"%(regr.coef_,regr.intercept_))
  print("Residual sum of squares: %.2f"%np.mean((regr.predict(X_test) - y_test)**2))
  print('Score:%.2f'% regr.score(X_test, y_test))

# tuning alpha value
def test_Ridge_alpha(data):
  X_train, X_test, y_train, y_test=data
  alphas = [.01,.02,.05,.1,.2,.5,1,2,5,10,20,50,100,200,500,1000]
  scores=[]
  for i, alpha in enumerate(alphas):
    regr = linear_model.Ridge(alpha=alpha)
    regr.fit(X_train, y_train)
    scores.append(regr.score(X_test, y_test))
  return alphas, scores

alphas,scores = test_Ridge_alpha(data)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(alphas,scores)
ax.set_xlabel(r"$\alpha$")
ax.set_ylabel(r"score")
ax.set_xscale('log')
ax.set_title("Ridge") # log x is useful for viz!
  
