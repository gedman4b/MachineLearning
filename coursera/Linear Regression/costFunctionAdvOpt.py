@mfunction("jVal, gradient")
def costFunctionAdvOpt(theta=None):
    jVal = (theta(1) - 5) ** 2 + (theta(2) - 5) ** 2
    gradient = zeros(2, 1)
    gradient(1).lvalue = 2 * (theta(1) - 5)
    gradient(2).lvalue = 2 * (theta(2) - 5)
end
