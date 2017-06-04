@mfunction("C, sigma")
def dataset3Params(X=None, y=None, Xval=None, yval=None):
    # DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
    # where you select the optimal (C, sigma) learning parameters to use for SVM
    # with RBF kernel
    #   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
    #   sigma. You should complete this function to return the optimal C and 
    #   sigma based on a cross-validation set.
    #

    # You need to return the following variables correctly.
    C = 1
    sigma = 0.3

    Fill(mstring('in'), mstring('this'), mstring('function'), mstring('to'), mstring('return'), mstring('the'), mstring('optimal'), mstring('C'), mstring('and'), mstring('sigma'))
    #               learning parameters found using the cross validation set.
    #               You can use svmPredict to predict the labels on the cross
    #               validation set. For example, 
    #                   predictions = svmPredict(model, Xval);
    #               will return the predictions on the cross validation set.
    #
    #  Note: You can compute the prediction error using 
    #        mean(double(predictions ~= yval))
    #
    Ctemp = mcat([0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30])
    sigmatemp = mcat([0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30])

    for ci in mslice[1:8]:
        for si in mslice[1:8]:
            model = svmTrain(X, y, Ctemp(ci), lambda x1, x2: gaussianKernel(x1, x2, sigmatemp(si)))
            predictions = svmPredict(model, Xval)
            error(si).lvalue = mean(double(predictions != yval))
            if (si == 1):
                error_si = error(si)
            else:
                error_si = mcat([error_si, OMPCSEMI, error(si)])
                end
                end
                if (ci == 1):
                    error_ci = error_si
                else:
                    error_ci = mcat([error_ci, error_si])
                    end
                    end
                    [r, c] = find(error_ci == min(min(error_ci)))
                    C = Ctemp(c)
                    sigma = sigmatemp(r)

                    end
