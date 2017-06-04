@mfunction("")
def plotData(X=None, y=None):
    # PLOTDATA Plots the data points X and y into a new figure 
    # PLOTDATA(x,y) plots the data points with + for the positive examples
    # and o for the negative examples. X is assumed to be a Mx2 matrix.

    # Create New Figure
    figure(mstring('hold'), mstring('on'))

    # Plot the positive and negative examples on a
    # 2D plot, using the option 'k+' for the positive
    # examples and 'ko' for the negative examples.
    #

    # Find Indices of Positive and Negative Examples
    pos = find(y == 1)
    neg = find(y == 0)
    print(neg)

    # Plot Examples
    plot(X(pos, 1), X(pos, 2), mstring('k+'), mstring('LineWidth'), 2, mstring('MarkerSize'), 7)
    plot(X(neg, 1), X(neg, 2), mstring('ko'), mstring('MarkerFaceColor'), mstring('y'), mstring('MarkerSize'), 7)

    hold(mstring('off'))
end
