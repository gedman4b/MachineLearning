@mfunction("J, grad")
def linearRegCostFunction(X=None, y=None, theta=None, _lambda=None):
    # LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
    # regression with multiple variables
    #   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
    #   cost of using theta as the parameter for linear regression to fit the 
    #   data points in X and y. Returns the cost in J and the gradient in grad

    # Initialize some useful values
    m = length(y)# number of training examples

    # You need to return the following variables correctly 
    J = 0
    grad = zeros(size(theta))

    # Compute the cost and gradient of regularized linear 
    # regression for a particular choice of theta.
    #
    # You should set J to the cost and grad to the gradient.
    #
    h = X * theta
    J = sum((h - y) **elpow** 2) / 2 / m + _lambda / 2 / m * (sum(theta **elpow** 2) - theta(1) ** 2)

    grad(1).lvalue = sum((h - y) *elmul* X(mslice[:], 1)) / m
    for j in mslice[2:size(theta)]:
        grad(j).lvalue = sum((h - y) *elmul* X(mslice[:], j)) / m + _lambda * theta(j) / m
    end

    grad = grad(mslice[:])

end
