@mfunction("J, grad")
def costFunction(theta=None, X=None, y=None):
    #COSTFUNCTION Compute cost and gradient for logistic regression
    #   J = COSTFUNCTION(theta, X, y) computes the cost of using theta as the
    #   parameter for logistic regression and the gradient of the cost
    #   w.r.t. to the parameters.

    # Initialize some useful values
    m = length(y)# number of training examples

    # You need to return the following variables correctly 
    J = 0
    grad = zeros(size(theta))

    # Compute the cost of a particular choice of theta.
    # You should set J to the cost.
    # Compute the partial derivatives and set grad to the partial
    # derivatives of the cost w.r.t. each parameter in theta
    #
    # grad should have the same dimensions as theta
    #
    for j in mslice[1:m]:
        temp(j).lvalue = 0
        for i in mslice[1:size(theta)]:
            temp(j).lvalue = temp(j) + theta(i) * X(j, i)
        end
    end

    for j in mslice[1:m]:
        h(j).lvalue = sigmoid(temp(j))
    end

    for j in mslice[1:m]:
        J = J + y(j) * log(h(j)) + (1 - y(j)) * log(1 - h(j))
    end

    J = -J / m

    for i in mslice[1:size(theta)]:
        grad(i).lvalue = 0
        for j in mslice[1:m]:
            grad(i).lvalue = grad(i) + (h(j) - y(j)) * X(j, i)
        end
        grad(i).lvalue = grad(i) / m
    end

    end
