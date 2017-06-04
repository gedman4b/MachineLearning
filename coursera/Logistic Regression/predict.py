@mfunction("p")
def predict(theta=None, X=None):
    # PREDICT Predict whether the label is 0 or 1 using learned logistic 
    # regression parameters theta
    # p = PREDICT(theta, X) computes the predictions for X using a 
    # threshold at 0.5 (i.e., if sigmoid(theta'*x) >= 0.5, predict 1)

    m = size(X, 1)# Number of training examples

    # You need to return the following variables correctly
    p = zeros(m, 1)
    # Complete the following code to make predictions using
    # your learned logistic regression parameters. 
    # You should set p to a vector of 0's and 1's
    #

    for j in mslice[1:m]:
        temp(j).lvalue = 0
        for i in mslice[1:size(theta)]:
            temp(j).lvalue = temp(j) + theta(i) * X(j, i)
        end
    end

    for j in mslice[1:m]:
        h(j).lvalue = sigmoid(temp(j))
        if (h(j) >= 0.5):
           p(j).lvalue = 1
        else:
           p(j).lvalue = 0
        end

    end
