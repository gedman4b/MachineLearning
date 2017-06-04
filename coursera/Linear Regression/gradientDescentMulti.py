@mfunction("theta, J_history")
def gradientDescentMulti(X=None, y=None, theta=None, alpha=None, num_iters=None):
    #GRADIENTDESCENTMULTI Performs gradient descent to learn theta
    #   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
    #   taking num_iters gradient steps with learning rate alpha

    # Initialize some useful values
    m = length(y)# number of training examples
    J_history = zeros(num_iters, 1)

    for iter in mslice[1:num_iters]:
        # Perform a single gradient step on the parameter vector
        delta = 1 / m * (X.cT * X * theta - X.cT * y)
        theta = theta - alpha *elmul* delta

        # Save the cost J in every iteration    
        J_history(iter).lvalue = computeCostMulti(X, y, theta)

    end

end

