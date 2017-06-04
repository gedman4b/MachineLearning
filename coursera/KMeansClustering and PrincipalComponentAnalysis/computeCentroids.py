@mfunction("centroids")
def computeCentroids(X=None, idx=None, K=None):
    # COMPUTECENTROIDS returns the new centroids by computing the means of the 
    # data points assigned to each centroid.
    #   centroids = COMPUTECENTROIDS(X, idx, K) returns the new centroids by 
    #   computing the means of the data points assigned to each centroid. It is
    #   given a dataset X where each row is a single data point, a vector
    #   idx of centroid assignments (i.e. each entry in range [1..K]) for each
    #   example, and K, the number of centroids. You should return a matrix
    #   centroids, where each row of centroids is the mean of the data points
    #   assigned to it.
    #

    # Useful variables
    [m, n] = size(X)

    # You need to return the following variables correctly.
    centroids = zeros(K, n)

    # Go over every centroid and compute mean of all points that
    # belong to it. Concretely, the row vector centroids(i, :)
    # should contain the mean of the data points assigned to
    # centroid i.
    #
    # Note: You can use a for-loop over the centroids to compute this.
    #
    numcen = zeros(K, 1)
    for xi in mslice[1:m]:
        numcen(idx(xi)).lvalue = numcen(idx(xi)) + 1
        centroids(idx(xi), mslice[:]).lvalue = centroids(idx(xi), mslice[:]) + X(xi, mslice[:])
    end
    for Ck in mslice[1:K]:
        centroids(Ck, mslice[:]).lvalue = centroids(Ck, mslice[:]) / numcen(Ck)
    end

end
