@mfunction("theta, J_history")
def gradientDescent(X=None, y=None, theta=None, alpha=None, num_iters=None):
    #GRADIENTDESCENT Performs gradient descent to learn theta
    #   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
    #   taking num_iters gradient steps with learning rate alpha

    # Initialize some useful values
    m = length(y)# number of training examples
    J_history = zeros(num_iters, 1)

    for iter in mslice[1:num_iters]:

        # Perform a single gradient step on the parameter vector

        delta1 = 0
        delta2 = 0
        for i in mslice[1:m]:
            delta1 = delta1 + (theta(1) + theta(2) * X(i, 2) - y(i)) * X(i, 2)
            delta2 = delta2 + theta(1) + theta(2) * X(i, 2) - y(i)
            end
            theta(1).lvalue = theta(1) - alpha / m * delta2
            theta(2).lvalue = theta(2) - alpha / m * delta1

            # Save the cost J in every iteration    
            J_history(iter).lvalue = computeCost(X, y, theta)

        end

    end
end

