@mfunction("")
def plotProgresskMeans(X=None, centroids=None, previous=None, idx=None, K=None, i=None):
    # PLOTPROGRESSKMEANS is a helper function that displays the progress of 
    # k-Means as it is running. It is intended for use only with 2D data.
    #   PLOTPROGRESSKMEANS(X, centroids, previous, idx, K, i) plots the data
    #   points with colors assigned to each centroid. With the previous
    #   centroids, it also plots a line between the previous locations and
    #   current locations of the centroids.
    #

    # Plot the examples
    plotDataPoints(X, idx, K)

    # Plot the centroids as black x's
    plot(centroids(mslice[:], 1), centroids(mslice[:], 2), mstring('x'), mstring('MarkerEdgeColor'), mstring('k'), mstring('MarkerSize'), 10, mstring('LineWidth'), 3)

    # Plot the history of the centroids with lines
    for j in mslice[1:size(centroids, 1)]:
        drawLine(centroids(j, mslice[:]), previous(j, mslice[:]))
    end

    # Title
    title(sprintf(mstring('Iteration number %d'), i))

end
