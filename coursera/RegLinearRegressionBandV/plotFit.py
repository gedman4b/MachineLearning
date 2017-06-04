@mfunction("")
def plotFit(min_x=None, max_x=None, mu=None, sigma=None, theta=None, p=None):
    # PLOTFIT Plots a learned polynomial regression fit over an existing figure.
    # Also works with linear regression.
    #   PLOTFIT(min_x, max_x, mu, sigma, theta, p) plots the learned polynomial
    #   fit with power p and feature normalization (mu, sigma).

    # Hold on to the current figure
    hold(mstring('on'))

    # We plot a range slightly bigger than the min and max values to get
    # an idea of how the fit will vary outside the range of the data points
    x = (mslice[min_x - 15:0.05:max_x + 25]).cT

    # Map the X values 
    X_poly = polyFeatures(x, p)
    X_poly = bsxfun(minus, X_poly, mu)
    X_poly = bsxfun(rdivide, X_poly, sigma)

    # Add ones
    X_poly = mcat([ones(size(x, 1), 1), X_poly])

    # Plot
    plot(x, X_poly * theta, mstring('--'), mstring('LineWidth'), 2)

    # Hold off to the current figure
    hold(mstring('off'))

end
