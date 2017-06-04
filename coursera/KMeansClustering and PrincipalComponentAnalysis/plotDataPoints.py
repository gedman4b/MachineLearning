@mfunction("")
def plotDataPoints(X=None, idx=None, K=None):
    # PLOTDATAPOINTS plots data points in X, coloring them so that those with the same
    # index assignments in idx have the same color
    #   PLOTDATAPOINTS(X, idx, K) plots data points in X, coloring them so that those 
    #   with the same index assignments in idx have the same color

    # Create palette
    palette = hsv(K + 1)
    colors = palette(idx, mslice[:])

    # Plot the data
    scatter(X(mslice[:], 1), X(mslice[:], 2), 15, colors)

end
