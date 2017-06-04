#% Machine Learning Online Class - Exercise 3 | Part 1: One-vs-all

#% Initialization
clear(mstring('close'), mstring('all'), mstring('clc'))

#% Setup the parameters you will use for this part of the exercise
input_layer_size = 400# 20x20 Input Images of Digits
num_labels = 10# 10 labels, from 1 to 10
# (note that we have mapped "0" to label 10)

#% =========== Part 1: Loading and Visualizing Data =============
#  We start the exercise by first loading and visualizing the dataset.
#  You will be working with a dataset that contains handwritten digits.
#

# Load Training Data
fprintf(mstring('Loading and Visualizing Data ...\\n'))

load(mstring('ex3data1.mat'))# training data stored in arrays X, y
m = size(X, 1)

# Randomly select 100 data points to display
rand_indices = randperm(m)
sel = X(rand_indices(mslice[1:100]), mslice[:])

displayData(sel)

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()

#% ============ Part 2a: Vectorize Logistic Regression ============
#  In this part of the exercise, you will reuse your logistic regression
#  code from the last exercise. You task here is to make sure that your
#  regularized logistic regression implementation is vectorized. After
#  that, you will implement one-vs-all classification for the handwritten
#  digit dataset.
#

# Test case for lrCostFunction
fprintf(mstring('\\nTesting lrCostFunction() with regularization'))

theta_t = mcat([-2, OMPCSEMI, -1, OMPCSEMI, 1, OMPCSEMI, 2])
X_t = mcat([ones(5, 1), reshape(mslice[1:15], 5, 3) / 10])
y_t = (mcat([1, OMPCSEMI, 0, OMPCSEMI, 1, OMPCSEMI, 0, OMPCSEMI, 1]) >= 0.5)
lambda_t = 3
[J, grad] = lrCostFunction(theta_t, X_t, y_t, lambda_t)

fprintf(mstring('\\nCost: %f\\n'), J)
fprintf(mstring('Expected cost: 2.534819\\n'))
fprintf(mstring('Gradients:\\n'))
fprintf(mstring(' %f \\n'), grad)
fprintf(mstring('Expected gradients:\\n'))
fprintf(mstring(' 0.146561\\n -0.548558\\n 0.724722\\n 1.398003\\n'))

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()
#% ============ Part 2b: One-vs-All Training ============
fprintf(mstring('\\nTraining One-vs-All Logistic Regression...\\n'))

_lambda = 0.1
[all_theta] = oneVsAll(X, y, num_labels, _lambda)

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()


#% ================ Part 3: Predict for One-Vs-All ================

pred = predictOneVsAll(all_theta, X)

fprintf(mstring('\\nTraining Set Accuracy: %f\\n'), mean(double(pred == y)) * 100)
