@mfunction("")
def plotDecisionBoundary(theta=None, X=None, y=None):
    # PLOTDECISIONBOUNDARY Plots the data points X and y into a new figure with
    # the decision boundary defined by theta
    # PLOTDECISIONBOUNDARY(theta, X,y) plots the data points with + for the 
    # positive examples and o for the negative examples. X is assumed to be 
    #   a either 
    # 1) Mx3 matrix, where the first column is an all-ones column for the 
    #    intercept.
    # 2) MxN, N>3 matrix, where the first column is all-ones

    # Plot Data
    plotData(X(mslice[:], mslice[2:3]), y)
    hold(mstring('on'))

    if size(X, 2) <= 3:
        # Only need 2 points to define a line, so choose two endpoints
        plot_x = mcat([min(X(mslice[:], 2)) - 2, max(X(mslice[:], 2)) + 2])

        # Calculate the decision boundary line
        plot_y = (-1. / theta(3)) *elmul* (theta(2) *elmul* plot_x + theta(1))

        # Plot, and adjust axes for better viewing
        plot(plot_x, plot_y)

        # Legend, specific for the exercise
        legend(mstring('Admitted'), mstring('Not admitted'), mstring('Decision Boundary'))
        axis(mcat([30, 100, 30, 100]))
    else:
        # Here is the grid range
        u = linspace(-1, 1.5, 50)
        v = linspace(-1, 1.5, 50)

        z = zeros(length(u), length(v))
        # Evaluate z = theta*x over the grid
        for i in mslice[1:length(u)]:
            for j in mslice[1:length(v)]:
                z(i, j).lvalue = mapFeature(u(i), v(j)) * theta
            end
        end
        z = z.cT            # important to transpose z before calling contour

        # Plot z = 0
        # Notice you need to specify the range [0, 0]
        contour(u, v, z, mcat([0, 0]), mstring('LineWidth'), 2)
    end
    hold(mstring('off'))

end
