#% Machine Learning Online Class - Exercise 2: Logistic Regression
#
#% Initialization
clear(mstring('close'), mstring('all'), mstring('clc'))

#% Load Data
#  The first two columns contains the exam scores and the third column
#  contains the label.

data = load(mstring('ex2data1.txt'))
X = data(mslice[:], mcat([1, 2]))
y = data(mslice[:], 3)
print(y)


#% ==================== Part 1: Plotting ====================
#  We start the exercise by first plotting the data to understand the 
#  the problem we are working with.

fprintf(mcat([mstring('Plotting data with + indicating (y = 1) examples and o '), mstring('indicating (y = 0) examples.\\n')]))

plotData(X, y)

# Put some labels 
hold(mstring('on'))
# Labels and Legend
xlabel(mstring('Exam 1 score'))
ylabel(mstring('Exam 2 score'))

# Specified in plot order
legend(mstring('Admitted'), mstring('Not admitted'))
hold(mstring('off'))

fprintf(mstring('\\nProgram paused. Press enter to continue.\\n'))
pause()


#% ============ Part 2: Compute Cost and Gradient ============
#  In this part of the exercise, you will implement the cost and gradient
#  for logistic regression. You neeed to complete the code in 
#  costFunction.m

#  Setup the data matrix appropriately, and add ones for the intercept term
[m, n] = size(X)

# Add intercept term to x and X_test
X = mcat([ones(m, 1), X])

# Initialize fitting parameters
initial_theta = zeros(n + 1, 1)

# Compute and display initial cost and gradient
[cost, grad] = costFunction(initial_theta, X, y)

fprintf(mstring('Cost at initial theta (zeros): %f\\n'), cost)
fprintf(mstring('Expected cost (approx): 0.693\\n'))
fprintf(mstring('Gradient at initial theta (zeros): \\n'))
fprintf(mstring(' %f \\n'), grad)
fprintf(mstring('Expected gradients (approx):\\n -0.1000\\n -12.0092\\n -11.2628\\n'))

# Compute and display cost and gradient with non-zero theta
test_theta = mcat([-24, OMPCSEMI, 0.2, OMPCSEMI, 0.2])
[cost, grad] = costFunction(test_theta, X, y)

fprintf(mstring('\\nCost at test theta: %f\\n'), cost)
fprintf(mstring('Expected cost (approx): 0.218\\n'))
fprintf(mstring('Gradient at test theta: \\n'))
fprintf(mstring(' %f \\n'), grad)
fprintf(mstring('Expected gradients (approx):\\n 0.043\\n 2.566\\n 2.647\\n'))

fprintf(mstring('\\nProgram paused. Press enter to continue.\\n'))
pause()


#% ============= Part 3: Optimizing using fminunc  =============
#  In this exercise, you will use a built-in function (fminunc) to find the
#  optimal parameters theta.

#  Set options for fminunc
options = optimset(mstring('GradObj'), mstring('on'), mstring('MaxIter'), 400)

#  Run fminunc to obtain the optimal theta
#  This function will return theta and the cost 
[theta, cost] = fminunc(lambda t: (costFunction(t, X, y)), initial_theta, options)

# Print theta to screen
fprintf(mstring('Cost at theta found by fminunc: %f\\n'), cost)
fprintf(mstring('Expected cost (approx): 0.203\\n'))
fprintf(mstring('theta: \\n'))
fprintf(mstring(' %f \\n'), theta)
fprintf(mstring('Expected theta (approx):\\n'))
fprintf(mstring(' -25.161\\n 0.206\\n 0.201\\n'))

# Plot Boundary
plotDecisionBoundary(theta, X, y)

# Put some labels 
hold(mstring('on'))
# Labels and Legend
xlabel(mstring('Exam 1 score'))
ylabel(mstring('Exam 2 score'))

# Specified in plot order
legend(mstring('Admitted'), mstring('Not admitted'))
hold(mstring('off'))

fprintf(mstring('\\nProgram paused. Press enter to continue.\\n'))
pause()

#% ============== Part 4: Predict and Accuracies ==============
#  After learning the parameters, you'll like to use it to predict the outcomes
#  on unseen data. In this part, you will use the logistic regression model
#  to predict the probability that a student with score 45 on exam 1 and 
#  score 85 on exam 2 will be admitted.
#
#  Furthermore, you will compute the training and test set accuracies of 
#  our model.
#
#  Your task is to complete the code in predict.m

#  Predict probability for a student with score 45 on exam 1 
#  and score 85 on exam 2 

prob = sigmoid(mcat([1, 45, 85]) * theta)
fprintf(mcat([mstring('For a student with scores 45 and 85, we predict an admission '), mstring('probability of %f\\n')]), prob)
fprintf(mstring('Expected value: 0.775 +/- 0.002\\n\\n'))

# Compute accuracy on our training set
p = predict(theta, X)

fprintf(mstring('Train Accuracy: %f\\n'), mean(double(p == y)) * 100)
fprintf(mstring('Expected accuracy (approx): 89.0\\n'))
fprintf(mstring('\\n'))
