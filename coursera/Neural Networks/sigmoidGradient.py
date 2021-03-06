@mfunction("g")
def sigmoidGradient(z=None):
    # SIGMOIDGRADIENT returns the gradient of the sigmoid function
    # evaluated at z
    #   g = SIGMOIDGRADIENT(z) computes the gradient of the sigmoid function
    #   evaluated at z. This should work regardless if z is a matrix or a
    #   vector. In particular, if z is a vector or matrix, you should return
    #   the gradient for each element.

    g = zeros(size(z))

    # Compute the gradient of the sigmoid function evaluated at
    #               each value of z (z can be a matrix, vector or scalar).
    one = ones(size(z))
    g = sigmoid(z) *elmul* (one - sigmoid(z))

end
