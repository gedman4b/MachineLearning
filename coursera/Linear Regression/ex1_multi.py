#% Machine Learning Online Class
#  Exercise 1: Linear regression with multiple variables
#

#% Initialization

#% ================ Part 1: Feature Normalization ================

#% Clear and Close Figures
clear(mstring('close'), mstring('all'), mstring('clc'))

fprintf(mstring('Loading data ...\\n'))

#% Load Data
data = load(mstring('ex1data2.txt'))
X = data(mslice[:], mslice[1:2])
y = data(mslice[:], 3)
m = length(y)

# Print out some data points
fprintf(mstring('First 10 examples from the dataset: \\n'))
fprintf(mstring(' x = [%.0f %.0f], y = %.0f \\n'), mcat([X(mslice[1:10], mslice[:]), y(mslice[1:10], mslice[:])]).cT)

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

# Scale features and set them to zero mean
fprintf(mstring('Normalizing Features ...\\n'))

[X, mu, sigma] = featureNormalize(X)

# Add intercept term to X
X = mcat([ones(m, 1), X])


#% ================ Part 2: Gradient Descent ================

fprintf(mstring('Running gradient descent ...\\n'))

# Choose some alpha value
alpha = 0.01
num_iters = 400

# Init Theta and Run Gradient Descent 
theta = zeros(3, 1)
[theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)

# Plot the convergence graph
figure()
plot(mslice[1:numel(J_history)], J_history, mstring('-b'), mstring('LineWidth'), 2)
xlabel(mstring('Number of iterations'))
ylabel(mstring('Cost J'))

# Display gradient descent's result
fprintf(mstring('Theta computed from gradient descent: \\n'))
fprintf(mstring(' %f \\n'), theta)
fprintf(mstring('\\n'))

# Estimate the price of a 1650 sq-ft, 3 br house

price = 0# You should change this


# ============================================================

fprintf(mcat([mstring('Predicted price of a 1650 sq-ft, 3 br house '), mstring('(using gradient descent):\\n $%f\\n')]), price)

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

#% ================ Part 3: Normal Equations ================

fprintf(mstring('Solving with normal equations...\\n'))

#% Load Data
data = csvread(mstring('ex1data2.txt'))
X = data(mslice[:], mslice[1:2])
y = data(mslice[:], 3)
m = length(y)

# Add intercept term to X
X = mcat([ones(m, 1), X])

# Calculate the parameters from the normal equation
theta = normalEqn(X, y)

# Display normal equation's result
fprintf(mstring('Theta computed from the normal equations: \\n'))
fprintf(mstring(' %f \\n'), theta)
fprintf(mstring('\\n'))


# Estimate the price of a 1650 sq-ft, 3 br house

price = 0# You should change this


# ============================================================

fprintf(mcat([mstring('Predicted price of a 1650 sq-ft, 3 br house '), mstring('(using normal equations):\\n $%f\\n')]), price)
