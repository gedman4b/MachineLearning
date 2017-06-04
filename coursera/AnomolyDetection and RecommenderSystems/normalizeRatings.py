@mfunction("Ynorm, Ymean")
def normalizeRatings(Y=None, R=None):
    # NORMALIZERATINGS Preprocess data by subtracting mean rating for every 
    # movie (every row)
    #   [Ynorm, Ymean] = NORMALIZERATINGS(Y, R) normalized Y so that each movie
    #   has a rating of 0 on average, and returns the mean rating in Ymean.
    #

    [m, n] = size(Y)
    Ymean = zeros(m, 1)
    Ynorm = zeros(size(Y))
    for i in mslice[1:m]:
        idx = find(R(i, mslice[:]) == 1)
        Ymean(i).lvalue = mean(Y(i, idx))
        Ynorm(i, idx).lvalue = Y(i, idx) - Ymean(i)
    end

end
