@mfunction("out")
def mapFeature(X1=None, X2=None):
    # MAPFEATURE Feature mapping function to polynomial features
    #
    #   MAPFEATURE(X1, X2) maps the two input features
    #   to quadratic features used in the regularization exercise.
    #
    #   Returns a new feature array with more features, comprising of 
    #   X1, X2, X1.^2, X2.^2, X1*X2, X1*X2.^2, etc..
    #
    #   Inputs X1, X2 must be the same size
    #

    degree = 6
    out = ones(size(X1(mslice[:], 1)))
    for i in mslice[1:degree]:
        for j in mslice[0:i]:
            out(mslice[:], end + 1).lvalue = (X1 **elpow** (i - j)) *elmul* (X2 **elpow** j)
        end
    end

end
