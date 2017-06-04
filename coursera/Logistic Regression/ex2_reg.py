#% Machine Learning Online Class - Exercise 2: Logistic Regression
#

#% Initialization
clear(mstring('close'), mstring('all'), mstring('clc'))

#% Load Data
#  The first two columns contains the X values and the third column
#  contains the label (y).

data = load(mstring('ex2data2.txt'))
X = data(mslice[:], mcat([1, 2]))
y = data(mslice[:], 3)
print(y)


plotData(X, y)

# Put some labels
hold(mstring('on'))

# Labels and Legend
xlabel(mstring('Microchip Test 1'))
ylabel(mstring('Microchip Test 2'))

# Specified in plot order
legend(mstring('y = 1'), mstring('y = 0'))
hold(mstring('off'))


#% =========== Part 1: Regularized Logistic Regression ============
#  In this part, you are given a dataset with data points that are not
#  linearly separable. However, you would still like to use logistic
#  regression to classify the data points.
#
#  To do so, you introduce more features to use -- in particular, you add
#  polynomial features to our data matrix (similar to polynomial
#  regression).
#

# Add Polynomial Features

# Note that mapFeature also adds a column of ones for us, so the intercept
# term is handled
X = mapFeature(X(mslice[:], 1), X(mslice[:], 2))

# Initialize fitting parameters
initial_theta = zeros(size(X, 2), 1)

# Set regularization parameter lambda to 1
_lambda = 1

# Compute and display initial cost and gradient for regularized logistic
# regression
[cost, grad] = costFunctionReg(initial_theta, X, y, _lambda)

fprintf(mstring('Cost at initial theta (zeros): %f\\n'), cost)
fprintf(mstring('Expected cost (approx): 0.693\\n'))
fprintf(mstring('Gradient at initial theta (zeros) - first five values only:\\n'))
fprintf(mstring(' %f \\n'), grad(mslice[1:5]))
fprintf(mstring('Expected gradients (approx) - first five values only:\\n'))
fprintf(mstring(' 0.0085\\n 0.0188\\n 0.0001\\n 0.0503\\n 0.0115\\n'))

fprintf(mstring('\\nProgram paused. Press enter to continue.\\n'))
pause()

# Compute and display cost and gradient
# with all-ones theta and lambda = 10
test_theta = ones(size(X, 2), 1)
[cost, grad] = costFunctionReg(test_theta, X, y, 10)

fprintf(mstring('\\nCost at test theta (with lambda = 10): %f\\n'), cost)
fprintf(mstring('Expected cost (approx): 3.16\\n'))
fprintf(mstring('Gradient at test theta - first five values only:\\n'))
fprintf(mstring(' %f \\n'), grad(mslice[1:5]))
fprintf(mstring('Expected gradients (approx) - first five values only:\\n'))
fprintf(mstring(' 0.3460\\n 0.1614\\n 0.1948\\n 0.2269\\n 0.0922\\n'))

fprintf(mstring('\\nProgram paused. Press enter to continue.\\n'))
pause()

#% ============= Part 2: Regularization and Accuracies =============
#  Optional Exercise:
#  In this part, you will get to try different values of lambda and
#  see how regularization affects the decision coundart
#
#  Try the following values of lambda (0, 1, 10, 100).
#
#  How does the decision boundary change when you vary lambda? How does
#  the training set accuracy vary?
#

# Initialize fitting parameters
initial_theta = zeros(size(X, 2), 1)

# Set regularization parameter lambda to 1 (you should vary this)
_lambda = 1

# Set Options
options = optimset(mstring('GradObj'), mstring('on'), mstring('MaxIter'), 400)

# Optimize
[theta, J, exit_flag] = fminunc(lambda t: (costFunctionReg(t, X, y, _lambda)), initial_theta, options)

# Plot Boundary
plotDecisionBoundary(theta, X, y)
hold(mstring('on'))
title(sprintf(mstring('lambda = %g'), _lambda))

# Labels and Legend
xlabel(mstring('Microchip Test 1'))
ylabel(mstring('Microchip Test 2'))

legend(mstring('y = 1'), mstring('y = 0'), mstring('Decision boundary'))
hold(mstring('off'))

# Compute accuracy on our training set
p = predict(theta, X)

fprintf(mstring('Train Accuracy: %f\\n'), mean(double(p == y)) * 100)
fprintf(mstring('Expected accuracy (with lambda = 1): 83.1 (approx)\\n'))
