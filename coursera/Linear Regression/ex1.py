#% Machine Learning Online Class - Exercise 1: Linear Regression
#
# x refers to the population size in 10,000s
# y refers to the profit in $10,000s
#

#% Initialization
clear(mstring('close'), mstring('all'), mstring('clc'))

#% ==================== Part 1: Basic Function ====================
# Complete warmUpExercise.m
fprintf(mstring('Running warmUpExercise ... \\n'))
fprintf(mstring('5x5 Identity Matrix: \\n'))
warmUpExercise()

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()


#% ======================= Part 2: Plotting =======================
fprintf(mstring('Plotting Data ...\\n'))
data = load(mstring('ex1data1.txt'))
X = data(mslice[:], 1)
y = data(mslice[:], 2); print y

m = length(y)# number of training examples

# Plot Data
# Note: You have to complete the code in plotData.m
plotData(X, y)

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

#% =================== Part 3: Cost and Gradient descent ===================

X = mcat([ones(m, 1), data(mslice[:], 1)])# Add a column of ones to x
theta = zeros(2, 1)# initialize fitting parameters

# Some gradient descent settings
iterations = 1500
alpha = 0.01

fprintf(mstring('\\nTesting the cost function ...\\n'))
# compute and display initial cost
J = computeCost(X, y, theta)
fprintf(mstring('With theta = [0 ; 0]\\nCost computed = %f\\n'), J)
fprintf(mstring('Expected cost value (approx) 32.07\\n'))

# further testing of the cost function
J = computeCost(X, y, mcat([-1, OMPCSEMI, 2]))
fprintf(mstring('\\nWith theta = [-1 ; 2]\\nCost computed = %f\\n'), J)
fprintf(mstring('Expected cost value (approx) 54.24\\n'))

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

fprintf(mstring('\\nRunning Gradient Descent ...\\n'))
# run gradient descent
theta = gradientDescent(X, y, theta, alpha, iterations)

# print theta to screen
fprintf(mstring('Theta found by gradient descent:\\n'))
fprintf(mstring('%f\\n'), theta)
fprintf(mstring('Expected theta values (approx)\\n'))
fprintf(mstring(' -3.6303\\n  1.1664\\n\\n'))

# Plot the linear fit
hold(mstring('on'))# keep previous plot visible
plot(X(mslice[:], 2), X * theta, mstring('-'))
legend(mstring('Training data'), mstring('Linear regression'))
hold(mstring('off'))# don't overlay any more plots on this figure

# Predict values for population sizes of 35,000 and 70,000
predict1 = mcat([1, 3.5]) * theta
fprintf(mstring('For population = 35,000, we predict a profit of %f\\n'), predict1 * 10000)
predict2 = mcat([1, 7]) * theta
fprintf(mstring('For population = 70,000, we predict a profit of %f\\n'), predict2 * 10000)

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

#% ============= Part 4: Visualizing J(theta_0, theta_1) =============
fprintf(mstring('Visualizing J(theta_0, theta_1) ...\\n'))

# Grid over which we will calculate J
theta0_vals = linspace(-10, 10, 100)
theta1_vals = linspace(-1, 4, 100)

# initialize J_vals to a matrix of 0's
J_vals = zeros(length(theta0_vals), length(theta1_vals))

# Fill out J_vals
for i in mslice[1:length(theta0_vals)]:
    for j in mslice[1:length(theta1_vals)]:
        t = mcat([theta0_vals(i), OMPCSEMI, theta1_vals(j)])
        J_vals(i, j).lvalue = computeCost(X, y, t)
        end
        end


        # Because of the way meshgrids work in the surf command, we need to
        # transpose J_vals before calling surf, or else the axes will be flipped
        J_vals = J_vals.cT
        # Surface plot
        figure()
        surf(theta0_vals, theta1_vals, J_vals)
        xlabel(mstring('\\theta_0'))
        ylabel(mstring('\\theta_1'))


        # Contour plot
        figure()
        # Plot J_vals as 15 contours spaced logarithmically between 0.01 and 100
        contour(theta0_vals, theta1_vals, J_vals, logspace(-2, 3, 20))
        xlabel(mstring('\\theta_0'))
        ylabel(mstring('\\theta_1'))

        hold(mstring('on'))
        plot(theta(1), theta(2), mstring('rx'), mstring('MarkerSize'), 10, mstring('LineWidth'), 2)
