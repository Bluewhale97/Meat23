#1. GLM, general linear model
# formula: y=x*beta + epsilon
# x is design matrix, columns are independent variables
# beta is regression coefficients or beta parameters
# y is dependent variable

#when use left inverse to compute the beta, you have to meet the full column rank n for matrix mxn

#2. multi collinearity
#sometimes happens that the matrix is not full col rank
# this is called multi collinearity

# and sometimes we need to know whether y is in the column space of x, if not, we should use a noice to change y => y+epsilon
# why adding noice help dealing with multi-collinearity?
# it is impacting on some columns and that make the columns are independent

#3. least squares fitting via orthogonal projection
# first step is using QR to replace x
# then beta = (inverse of (R.T @ R)) @ (Q@R).T @ y
beta = np.linalg.lstsq(x,y, rcond=None)[0]

