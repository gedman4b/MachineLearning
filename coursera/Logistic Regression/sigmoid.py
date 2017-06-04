@mfunction("g")
def sigmoid(z=None):
    # SIGMOID Compute sigmoid function
    # g = SIGMOID(z) computes the sigmoid of z.

    # You need to return the following variables correctly 
    g = zeros(size(z))
    [row, col] = size(z)

    # Compute the sigmoid of each value of z (z can be a matrix, vector or scalar).
    for i in mslice[1:row]:
        for j in mslice[1:col]:
            g(i, j).lvalue = 1 / (1 + exp(-z(i, j)))
        end
    end

end
