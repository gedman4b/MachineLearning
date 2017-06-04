@mfunction("theta")
def trainLinearReg(X=None, y=None, _lambda=None):
    # TRAINLINEARREG Trains linear regression given a dataset (X, y) and a
    # regularization parameter lambda
    #   [theta] = TRAINLINEARREG (X, y, lambda) trains linear regression using
    #   the dataset (X, y) and regularization parameter lambda. Returns the
    #   trained parameters theta.
    #

    # Initialize Theta
    initial_theta = zeros(size(X, 2), 1)

    # Create "short hand" for the cost function to be minimized
    costFunction = lambda t: linearRegCostFunction(X, y, t, _lambda)

    # Now, costFunction is a function that takes in only one argument
    options = optimset(mstring('MaxIter'), 200, mstring('GradObj'), mstring('on'))

    # Minimize using fmincg
    theta = fmincg(costFunction, initial_theta, options)

end
