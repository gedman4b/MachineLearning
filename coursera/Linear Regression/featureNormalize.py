@mfunction("X_norm, mu, sigma")
def featureNormalize(X=None):
    #FEATURENORMALIZE Normalizes the features in X 
    #   FEATURENORMALIZE(X) returns a normalized version of X where
    #   the mean value of each feature is 0 and the standard deviation
    #   is 1. This is often a good preprocessing step to do when
    #   working with learning algorithms.

    # You need to set these values correctly
    X_norm = X
    mu = zeros(1, size(X, 2))
    sigma = zeros(1, size(X, 2))

    mean_X1 = mean(X(mslice[:], 1))
    std_X1 = std(X(mslice[:], 1))
    mean_X2 = mean(X(mslice[:], 2))
    std_X2 = std(X(mslice[:], 2))
    k = size(X)
    m = k(1, 1)

    #mu=[mean_X1(1:m,1), mean_X2(1:m,2)];
    for i in mslice[1:m]:
        mu(i, 1).lvalue = mean_X1
        mu(i, 2).lvalue = mean_X2
        end
        #sigma=[std_X1(1:m,1),std_X2(1:m,2)];
        for i in mslice[1:m]:
            sigma(i, 1).lvalue = std_X1
            sigma(i, 2).lvalue = std_X2
            end

            # Compute X_norm
            X_norm = (X - mu) /eldiv/ sigma
            print(X_norm)
end
