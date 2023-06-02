#import packages
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, discriminant_analysis
from sklearn.model_selection import train_test_split 

# logreg case
# 150 data points, 3 classes, 4 features

def load_data():
  iris = datasets.load_iris()
  X_train=iris.data
  y_train=iris.target
  return train_test_split(X_train, y_train, test_size=.25, random_state=0, stratify=y_train)

# here using stratification sampling, because the first 50 are class 0, the middle 50 are class 1 and rest points are class 2

# Linear Discriminant Analysis
sklearn.discriminant_analysis.LinearDiscriminantAnalysis()

## Params
# solver: 'svd' if have many features, lsqr: least square, recommend using with shrinkage, eigen: feature extraction, recommend using with shrinkage
# shrinkage: a float value or 'auto' or None, only meaniful while solver=lsqr or eigen. 'auto' means using Ledoit-Wolf to automatically decide the size of shrinkage. None: do not use shrinkage. A float value like 0.3(should be 0-1): assign shrinkage
# priors: an array for prior probability for every class, if None, means same prob
# n_components: integer, the dimensionality, should smaller than n_classes-1
# store_covariance: bool, True to compute covariance matrixs 
# tol: threshold of convergence

## Attributes
# coef_
# intercept_
# covariance_: covariance matrix for every class
# means_: mean vector for every class
# xbar_: overall mean vector
# n_iter_: actual iterations

## methods
# fit(X,y)
# predict(X)
# predict_log_proba(X)
# predict_proba(X)
# score(X,y)

# test LDA
def test_LDA(data):
  X_train, X_test, y_train, y_test=data
  lda = discriminant_analysis.LinearDiscriminantAnalysis()
  lda.fit(X_train, y_train)
  print('Coefficients:%s, intercept %s '%(lda.coef_, lda.intercept_))
  print('Score:%.2f'% lda.score(X_test, y_test))
  
test_LDA(data=load_data())


# plotting for dataset after dimensionality reduction by using LDA
def plot_LDA(converte_X,y):
  from mpl_toolkits.mplot3d import Axes3D
  fig=plt.figure()
  ax=Axes3D(fig,auto_add_to_figure=False)
  fig.add_axes(ax)
  colors='rgb'
  markers='o*s'
  for target,color,marker in zip([0,1,2], colors, markers):
    pos=(y==target).ravel()
    X=converted_X[pos,:]
    ax.scatter(X[:,0], X[:,1], X[:,2], color=color, marker=marker,
              label="label %d"%target)
  ax.legend(loc='best')
  fig.suptitle('Iries After LDA')
  plt.show()
  

X_train, X_test, y_train, y_test=load_data()
X=np.vstack((X_train, X_test))
Y=np.vstack((y_train.reshape(y_train.size,1),y_test.reshape(y_test.size,1)))
lda=discriminant_analysis.LinearDiscriminantAnalysis()
lda.fit(X,Y)
converted_X=np.dot(X,np.transpose(lda.coef_))+lda.intercept_
plot_LDA(converted_X,Y)


# impact from different solvers
def test_LDA_solver(data):
  X_train, X_test, y_train, y_test=data
  solvers = ['svd','lsqr','eigen']
  for solver in solvers:
    if(solver=='svd'):
      lda = discriminant_analysis.LinearDiscriminantAnalysis(solver=solver)
    else:
      lda = discriminant_analysis.LinearDiscriminantAnalysis(solver=solver, shrinkage=None)
    lda.fit(X_train, y_train)
    print('Score at solver=%s: %.2f' %(solver, lda.score(X_test, y_test)))
    
test_LDA_solver(data=load_data()) # no diff

# test the impact from shrinkage
def test_LDA_shrinkage(data):
  X_train, X_test, y_train, y_test=data
  shrinkages = np.linspace(0.0,1.0,num=20)
  scores=[]
  for shrinkage in shrinkages:
    lda = discriminant_analysis.LinearDiscriminantAnalysis(solver='lsqr',
                                                          shrinkage=shrinkage)
    lda.fit(X_train, y_train)
    scores.append(lda.score(X_test,y_test))
  return scores, shrinkages

scores, shrinkages = test_LDA_shrinkage(data=load_data())
## plotting
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(shrinkages,scores)
ax.set_xlabel(r"shrinkage")
ax.set_ylabel(r"score")
ax.set_ylim(0,1.05)
ax.set_title("LDA")
plt.show()

# this plot means that the accuracy will be going down while the shrinkage increases



