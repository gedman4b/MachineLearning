@mfunction("")
def visualizeBoundaryLinear(X=None, y=None, model=None):
    # VISUALIZEBOUNDARYLINEAR plots a linear decision boundary learned by the
    # SVM
    #   VISUALIZEBOUNDARYLINEAR(X, y, model) plots a linear decision boundary 
    #   learned by the SVM and overlays the data on it

    w = model.w
    b = model.b
    xp = linspace(min(X(mslice[:], 1)), max(X(mslice[:], 1)), 100)
    yp = -(w(1) * xp + b) / w(2)
    plotData(X, y)
    hold(mstring('on'))
    plot(xp, yp, mstring('-b'))
    hold(mstring('off'))

end
