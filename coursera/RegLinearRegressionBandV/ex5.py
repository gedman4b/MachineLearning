#% Machine Learning Online Class
#  Exercise 5 | Regularized Linear Regression and Bias-Variance
#

#% Initialization
clear(mstring('close'), mstring('all'), mstring('clc'))

#% =========== Part 1: Loading and Visualizing Data =============
#  We start the exercise by first loading and visualizing the dataset. 
#  The following code will load the dataset into your environment and plot
#  the data.
#

# Load Training Data
fprintf(mstring('Loading and Visualizing Data ...\\n'))

# Load from ex5data1: 
# You will have X, y, Xval, yval, Xtest, ytest in your environment
load(mstring('ex5data1.mat'))

# m = Number of examples
m = size(X, 1)

# Plot training data
plot(X, y, mstring('rx'), mstring('MarkerSize'), 10, mstring('LineWidth'), 1.5)
xlabel(mstring('Change in water level (x)'))
ylabel(mstring('Water flowing out of the dam (y)'))

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

#% =========== Part 2: Regularized Linear Regression Cost =============
#  You should now implement the cost function for regularized linear 
#  regression. 
#

theta = mcat([1, OMPCSEMI, 1])
J = linearRegCostFunction(mcat([ones(m, 1), X]), y, theta, 1)

fprintf(mcat([mstring('Cost at theta = [1 ; 1]: %f '), mstring('\\n(this value should be about 303.993192)\\n')]), J)

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

#% =========== Part 3: Regularized Linear Regression Gradient =============
#  You should now implement the gradient for regularized linear 
#  regression.
#

theta = mcat([1, OMPCSEMI, 1])
[J, grad] = linearRegCostFunction(mcat([ones(m, 1), X]), y, theta, 1)

fprintf(mcat([mstring('Gradient at theta = [1 ; 1]:  [%f; %f] \'\\n(this value should be about [-15.303016; 598.250744])\\n')]), grad(1), grad(2))

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()


#% =========== Part 4: Train Linear Regression =============
#  Once you have implemented the cost and gradient correctly, the
#  trainLinearReg function will use your cost function to train 
#  regularized linear regression.
# 
#  Write Up Note: The data is non-linear, so this will not give a great 
#                 fit.
#

#  Train linear regression with lambda = 0
_lambda = 1
[theta] = trainLinearReg(mcat([ones(m, 1), X]), y, _lambda)

#  Plot fit over the data
plot(X, y, mstring('rx'), mstring('MarkerSize'), 10, mstring('LineWidth'), 1.5)
xlabel(mstring('Change in water level (x)'))
ylabel(mstring('Water flowing out of the dam (y)'))
hold(mstring('on'))
plot(X, mcat([ones(m, 1), X]) * theta, mstring('--'), mstring('LineWidth'), 2)
hold(mstring('off'))

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()


#% =========== Part 5: Learning Curve for Linear Regression =============
#  Next, you should implement the learningCurve function. 
#
#  Write Up Note: Since the model is underfitting the data, we expect to
#                 see a graph with "high bias" -- Figure 3 in ex5.pdf 
#

_lambda = 1
[error_train, error_val] = learningCurve(mcat([ones(m, 1), X]), y, mcat([ones(size(Xval, 1), 1), Xval]), yval, _lambda)

plot(mslice[1:m], error_train, mslice[1:m], error_val)
title(mstring('Learning curve for linear regression'))
legend(mstring('Train'), mstring('Cross Validation'))
xlabel(mstring('Number of training examples'))
ylabel(mstring('Error'))
axis(mcat([0, 13, 0, 150]))

fprintf(mstring('# Training Examples\\tTrain Error\\tCross Validation Error\\n'))
for i in mslice[1:m]:
    fprintf(mstring('  \\t%d\\t\\t%f\\t%f\\n'), i, error_train(i), error_val(i))
end

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

    #% =========== Part 6: Feature Mapping for Polynomial Regression =============
    #  One solution to this is to use polynomial regression. You should now
    #  complete polyFeatures to map each example into its powers
    #

p = 8

# Map X onto Polynomial Features and Normalize
X_poly = polyFeatures(X, p)
[X_poly, mu, sigma] = featureNormalize(X_poly)# Normalize
X_poly = mcat([ones(m, 1), X_poly])# Add Ones

# Map X_poly_test and normalize (using mu and sigma)
X_poly_test = polyFeatures(Xtest, p)
X_poly_test = bsxfun(minus, X_poly_test, mu)
X_poly_test = bsxfun(rdivide, X_poly_test, sigma)
X_poly_test = mcat([ones(size(X_poly_test, 1), 1), X_poly_test])# Add Ones

# Map X_poly_val and normalize (using mu and sigma)
X_poly_val = polyFeatures(Xval, p)
X_poly_val = bsxfun(minus, X_poly_val, mu)
X_poly_val = bsxfun(rdivide, X_poly_val, sigma)
X_poly_val = mcat([ones(size(X_poly_val, 1), 1), X_poly_val])# Add Ones

fprintf(mstring('Normalized Training Example 1:\\n'))
fprintf(mstring('  %f  \\n'), X_poly(1, mslice[:]))

fprintf(mstring('\\nProgram paused. Press enter to continue.\\n'))
pause()



#% =========== Part 7: Learning Curve for Polynomial Regression =============
#  Now, you will get to experiment with polynomial regression with multiple
#  values of lambda. The code below runs polynomial regression with 
#  lambda = 0. You should try running the code with different values of
#  lambda to see how the fit and learning curve change.
#

_lambda = 1
[theta] = trainLinearReg(X_poly, y, _lambda)

# Plot training data and fit
figure(1)
plot(X, y, mstring('rx'), mstring('MarkerSize'), 10, mstring('LineWidth'), 1.5)
plotFit(min(X), max(X), mu, sigma, theta, p)
xlabel(mstring('Change in water level (x)'))
ylabel(mstring('Water flowing out of the dam (y)'))
title(sprintf(mstring('Polynomial Regression Fit (lambda = %f)'), _lambda))
figure(2)
[error_train, error_val] = learningCurve(X_poly, y, X_poly_val, yval, _lambda)
plot(mslice[1:m], error_train, mslice[1:m], error_val)

title(sprintf(mstring('Polynomial Regression Learning Curve (lambda = %f)'), _lambda))
xlabel(mstring('Number of training examples'))
ylabel(mstring('Error'))
axis(mcat([0, 13, 0, 100]))
legend(mstring('Train'), mstring('Cross Validation'))

fprintf(mstring('Polynomial Regression (lambda = %f)\\n\\n'), _lambda)
fprintf(mstring('# Training Examples\\tTrain Error\\tCross Validation Error\\n'))
for i in mslice[1:m]:
    fprintf(mstring('  \\t%d\\t\\t%f\\t%f\\n'), i, error_train(i), error_val(i))
end

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

    #% =========== Part 8: Validation for Selecting Lambda =============
    #  You will now implement validationCurve to test various values of 
    #  lambda on a validation set. You will then use this to select the
    #  "best" lambda value.
    #
[lambda_vec, error_train, error_val] = validationCurve(X_poly, y, X_poly_val, yval)

close(mstring('all'))
plot(lambda_vec, error_train, lambda_vec, error_val)
legend(mstring('Train'), mstring('Cross Validation'))
xlabel(mstring('lambda'))
ylabel(mstring('Error'))

fprintf(mstring('lambda\\t\\tTrain Error\\tValidation Error\\n'))
for i in mslice[1:length(lambda_vec)]:
    fprintf(mstring(' %f\\t%f\\t%f\\n'), lambda_vec(i), error_train(i), error_val(i))
end

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()
