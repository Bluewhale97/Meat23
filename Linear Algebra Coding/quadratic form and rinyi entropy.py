# 1. spread of information
# the max of sigma / the min of sigma, called ccfdondition number as well
# small condition number "well-conditioned"
# large condition number 'ill-conditioned"
# it also tells as sensitivity or reliability of the matrix
# large condition number is more sensitive to small perturbations

# 2. quadratic form: to square matrix
# W.T @ S @ W

#3. normalize quadratic form
# w.T @ S @ W / (W.T @ W)

#4. GED with quadratic form
# generalized eigen decomposition
# Wm=argmax{W.T @ S @ W}, s.t. W.T @ W=1
# THEN Wm = argmax {W.T @ S @ W / (W.T @ R @ W)}
# This is rinyi entropy, S and R are two symmetric matrices for covariance
