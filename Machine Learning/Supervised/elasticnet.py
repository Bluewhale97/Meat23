#import packages
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, discriminant_analysis
from sklearn.model_selection import train_test_split 

#sklearn.model_selection.train_test_split
def load_data():
  diabetes = datasets.load_diabetes()
  return train_test_split(diabetes.data, diabetes.target,test_size=.25, random_state=0)

# elastic net
# combination of L1 and L2
sklearn.linear_modol.ElasticNet()
## Params

# l1_ratio: rho value, for l1 ratio
# others same as L1, L2

## Attributes:
# same as L1, L2

## Methods
# same as L1, L2


# test elastic net
def test_ElasticNet(data):
  X_train, X_test, y_train, y_test=data
  regr = linear_model.ElasticNet()
  regr.fit(X_train, y_train)
  print("Coefficients:%s, intercept %.2f"%(regr.coef_,regr.intercept_))
  print("Residual sum of squares: %.2f"%np.mean((regr.predict(X_test) - y_test)**2))
  print('Score:%.2f'% regr.score(X_test, y_test)) 
  
test_ElasticNet(data=data)

# test different alpha, rho on elastic net
def test_ElasticNet_alpha_rho(data):
  X_train, X_test, y_train, y_test=data
  alphas = np.logspace(-2,2)
  rhos=np.linspace(.01, 1)
  scores=[]
  for alpha in alphas:
    for rho in rhos:
      regr = linear_model.ElasticNet(alpha=alpha, l1_ratio=rho)
      regr.fit(X_train, y_train)
      scores.append(regr.score(X_test, y_test))
  return scores, alphas, rhos

scores, alphas, rhos = test_ElasticNet_alpha_rho(data=data)

alphas, rhos = np.meshgrid(alphas, rhos)

scores = np.array(scores).reshape(alphas.shape)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = Axes3D(fig, auto_add_to_figure=False)
surf = ax.plot_surface(alphas, rhos, scores, rstride=1, cstride=1, cmap=cm.jet,
                      linewidth =0, antialiased=False)
fig.add_axes(ax)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel(r"$\alpha$")
ax.set_ylabel(r"$\rho$")
ax.set_zlabel("score")
ax.set_title('ElasticNet')
plt.show()

# the score is getting smaller while the alpha is increasing
# rho just control the proportions of l1 and l2, then it directly impacts on the speed of getting smaller score
