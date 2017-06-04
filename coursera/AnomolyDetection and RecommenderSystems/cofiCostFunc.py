@mfunction("J, grad")
def cofiCostFunc(params=None, Y=None, R=None, num_users=None, num_movies=None, num_features=None, _lambda=None):
    # COFICOSTFUNC Collaborative filtering cost function
    #   [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, ...
    #   num_features, lambda) returns the cost and gradient for the
    #   collaborative filtering problem.
    #

    # Unfold the U and W matrices from params
    X = reshape(params(mslice[1:num_movies * num_features]), num_movies, num_features)
    Theta = reshape(params(mslice[num_movies * num_features + 1:end]), num_users, num_features)


    # You need to return the following values correctly
    J = 0
    X_grad = zeros(size(X))
    Theta_grad = zeros(size(Theta))

    # Compute the cost function and gradient for collaborative
    # filtering. Concretely, you should first implement the cost
    # function (without regularization) and make sure it is
    # matches our costs. After that, you should implement the 
    # gradient and use the checkCostFunction routine to check
    # that the gradient is correct. Finally, you should implement
    # regularization.
    #
    # Notes: X - num_movies  x num_features matrix of movie features
    #        Theta - num_users  x num_features matrix of user features
    #        Y - num_movies x num_users matrix of user ratings of movies
    #        R - num_movies x num_users matrix, where R(i, j) = 1 if the 
    #            i-th movie was rated by the j-th user
    #
    # You should set the following variables correctly:
    #
    #        X_grad - num_movies x num_features matrix, containing the 
    #                 partial derivatives w.r.t. to each element of X
    #        Theta_grad - num_users x num_features matrix, containing the 
    #                     partial derivatives w.r.t. to each element of Theta
    #
    temp1 = (X * Theta.cT - Y)
    temp = temp1 **elpow** 2
    J = sum(sum(temp(R == 1))) / 2
    J = J + _lambda / 2 * sum(sum(Theta **elpow** 2)) + _lambda / 2 * sum(sum(X **elpow** 2))
    for i in mslice[1:num_movies]:
        idx = find(R(i, mslice[:]) == 1)
        Theta_temp = Theta(idx, mslice[:])
        Y_tem = Y(i, idx)
        X_grad(i, mslice[:]).lvalue = (X(i, mslice[:]) * Theta_temp.cT - Y_tem) * Theta_temp + _lambda * X(i, mslice[:])

    end

    for j in mslice[1:num_users]:
        idy = find(R(mslice[:], j) == 1)
        Theta_temp = Theta(j, mslice[:])
        Y_tem = Y(idy, j)
        X_tem = X(idy, mslice[:])
        Theta_grad(j, mslice[:]).lvalue = (X_tem * Theta_temp.cT - Y_tem).cT * X_tem + _lambda * Theta(j, mslice[:])
    end

    grad = mcat([X_grad(mslice[:]), OMPCSEMI, Theta_grad(mslice[:])])

end
