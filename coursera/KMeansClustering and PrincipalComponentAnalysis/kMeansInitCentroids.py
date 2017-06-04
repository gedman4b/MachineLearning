@mfunction("centroids")
def kMeansInitCentroids(X=None, K=None):
    # KMEANSINITCENTROIDS This function initializes K centroids that are to be 
    # used in K-Means on the dataset X
    #   centroids = KMEANSINITCENTROIDS(X, K) returns K initial centroids to be
    #   used with the K-Means on the dataset X
    #

    # You should return this values correctly
    centroids = zeros(K, size(X, 2))

    # You should set centroids to randomly chosen examples from
    #               the dataset X
    #
    randomidx = randperm(size(X, 1))

    centroids = X(randomidx(mslice[1:K]), mslice[:])

end
