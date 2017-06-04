@mfunction("")
def visualizeBoundary(X=None, y=None, model=None, *varargin):
    # VISUALIZEBOUNDARY plots a non-linear decision boundary learned by the SVM
    #   VISUALIZEBOUNDARYLINEAR(X, y, model) plots a non-linear decision 
    #   boundary learned by the SVM and overlays the data on it

    # Plot the training data on top of the boundary
    plotData(X, y)

    # Make classification predictions over a grid of values
    x1plot = linspace(min(X(mslice[:], 1)), max(X(mslice[:], 1)), 100).cT
    x2plot = linspace(min(X(mslice[:], 2)), max(X(mslice[:], 2)), 100).cT
    [X1, X2] = meshgrid(x1plot, x2plot)
    vals = zeros(size(X1))
    for i in mslice[1:size(X1, 2)]:
        this_X = mcat([X1(mslice[:], i), X2(mslice[:], i)])
        vals(mslice[:], i).lvalue = svmPredict(model, this_X)
        end

        # Plot the SVM boundary
        hold(mstring('on'))
        contour(X1, X2, vals, mcat([0.5, 0.5]), mstring('b'))
        hold(mstring('off'))

    end
