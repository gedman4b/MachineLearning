@mfunction("idx")
def findClosestCentroids(X=None, centroids=None):
    # FINDCLOSESTCENTROIDS computes the centroid memberships for every example
    #   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
    #   in idx for a dataset X where each row is a single example. idx = m x 1 
    #   vector of centroid assignments (i.e. each entry in range [1..K])
    #

    # Set K
    K = size(centroids, 1)

    # You need to return the following variables correctly.
    idx = zeros(size(X, 1), 1)

    # Go over every example, find its closest centroid, and store
    # the index inside idx at the appropriate location.
    # Concretely, idx(i) should contain the index of the centroid
    # closest to example i. Hence, it should be a value in the 
    # range 1..K
    #
    # Note: You can use a for-loop over the examples to compute this.
    #
    for i in mslice[1:size(X, 1)]:
        mins = 1000
        id = 0
        for j in mslice[1:K]:
            X1 = X(i, mslice[:])
            u1 = centroids(j, mslice[:])
            mintemp = (X1 - u1) * (X1 - u1).cT
            if (mintemp < mins):
                mins = mintemp
                id = j
            end
        end
        idx(i).lvalue = id
    end

end
