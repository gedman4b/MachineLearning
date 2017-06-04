@mfunction("theta")
def normalEqn(X=None, y=None):
    #NORMALEQN Computes the closed-form solution to linear regression 
    #   NORMALEQN(X,y) computes the closed-form solution to linear 
    #   regression using the normal equations.

    theta = zeros(size(X, 2), 1)

    theta = pinv(X.cT * X) * X.cT * y

end


