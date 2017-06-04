#% Machine Learning Online Class
#  Exercise 7 | Principle Component Analysis and K-Means Clustering
#

#% Initialization
clear(mstring('close'), mstring('all'), mstring('clc'))

#% ================== Part 1: Load Example Dataset  ===================
#  We start this exercise by using a small dataset that is easily to
#  visualize
#
fprintf(mstring('Visualizing example dataset for PCA.\\n\\n'))

#  The following command loads the dataset. You should now have the 
#  variable X in your environment
load(mstring('ex7data1.mat'))

#  Visualize the example dataset
plot(X(mslice[:], 1), X(mslice[:], 2), mstring('bo'))
axis(mcat([0.5, 6.5, 2, 8]))
axis("square")


fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()


#% =============== Part 2: Principal Component Analysis ===============
#  You should now implement PCA, a dimension reduction technique. You
#  should complete the code in pca.m
#
fprintf(mstring('\\nRunning PCA on example dataset.\\n\\n'))

#  Before running PCA, it is important to first normalize X
[X_norm, mu, sigma] = featureNormalize(X)

#  Run PCA
[U, S] = pca(X_norm)

#  Compute mu, the mean of the each feature

#  Draw the eigenvectors centered at mean of data. These lines show the
#  directions of maximum variations in the dataset.
hold(mstring('on'))
drawLine(mu, mu + 1.5 * S(1, 1) * U(mslice[:], 1).cT, mstring('-k'), mstring('LineWidth'), 2)
drawLine(mu, mu + 1.5 * S(2, 2) * U(mslice[:], 2).cT, mstring('-k'), mstring('LineWidth'), 2)
hold(mstring('off'))

fprintf(mstring('Top eigenvector: \\n'))
fprintf(mstring(' U(:,1) = %f %f \\n'), U(1, 1), U(2, 1))
fprintf(mstring('\\n(you should expect to see -0.707107 -0.707107)\\n'))

fprintf(mstring('Program paused. Press enter to continue.\\n'))
pause()


#% =================== Part 3: Dimension Reduction ===================
#  You should now implement the projection step to map the data onto the 
#  first k eigenvectors. The code will then plot the data in this reduced 
#  dimensional space.  This will show you what the data looks like when 
#  using only the corresponding eigenvectors to reconstruct it.
#
#  You should complete the code in projectData.m
#
fprintf(mstring('\\nDimension reduction on example dataset.\\n\\n'))

#  Plot the normalized dataset (returned from pca)
plot(X_norm(mslice[:], 1), X_norm(mslice[:], 2), mstring('bo'))
axis(mcat([-4, 3 - 4, 3]))
axis("square")

#  Project the data onto K = 1 dimension
K = 1
Z = projectData(X_norm, U, K)
fprintf(mstring('Projection of the first example: %f\\n'), Z(1))
fprintf(mstring('\\n(this value should be about 1.481274)\\n\\n'))

X_rec = recoverData(Z, U, K)
fprintf(mstring('Approximation of the first example: %f %f\\n'), X_rec(1, 1), X_rec(1, 2))
fprintf(mstring('\\n(this value should be about  -1.047419 -1.047419)\\n\\n'))

#  Draw lines connecting the projected points to the original points
hold(mstring('on'))
plot(X_rec(mslice[:], 1), X_rec(mslice[:], 2), mstring('ro'))
for i in mslice[1:size(X_norm, 1)]:
    drawLine(X_norm(i, mslice[:]), X_rec(i, mslice[:]), mstring('--k'), mstring('LineWidth'), 1)
    end
    hold(mstring('off'))

    fprintf(mstring('Program paused. Press enter to continue.\\n'))
    pause()

    #% =============== Part 4: Loading and Visualizing Face Data =============
    #  We start the exercise by first loading and visualizing the dataset.
    #  The following code will load the dataset into your environment
    #
    fprintf(mstring('\\nLoading face dataset.\\n\\n'))

    #  Load Face dataset
    load(mstring('ex7faces.mat'))

    #  Display the first 100 faces in the dataset
    displayData(X(mslice[1:100], mslice[:]))

    fprintf(mstring('Program paused. Press enter to continue.\\n'))
    pause()

    #% =========== Part 5: PCA on Face Data: Eigenfaces  ===================
    #  Run PCA and visualize the eigenvectors which are in this case eigenfaces
    #  We display the first 36 eigenfaces.
    #
    fprintf(mcat([mstring('\\nRunning PCA on face dataset.\\n'), mstring('(this might take a minute or two ...)\\n\\n')]))

    #  Before running PCA, it is important to first normalize X by subtracting 
    #  the mean value from each feature
    [X_norm, mu, sigma] = featureNormalize(X)

    #  Run PCA
    [U, S] = pca(X_norm)

    #  Visualize the top 36 eigenvectors found
    displayData(U(mslice[:], mslice[1:36]).cT)

    fprintf(mstring('Program paused. Press enter to continue.\\n'))
    pause()


    #% ============= Part 6: Dimension Reduction for Faces =================
    #  Project images to the eigen space using the top k eigenvectors 
    #  If you are applying a machine learning algorithm 
    fprintf(mstring('\\nDimension reduction for face dataset.\\n\\n'))

    K = 100
    Z = projectData(X_norm, U, K)

    fprintf(mstring('The projected data Z has a size of: '))
    fprintf(mstring('%d '), size(Z))

    fprintf(mstring('\\n\\nProgram paused. Press enter to continue.\\n'))
    pause()

    #% ==== Part 7: Visualization of Faces after PCA Dimension Reduction ====
    #  Project images to the eigen space using the top K eigen vectors and 
    #  visualize only using those K dimensions
    #  Compare to the original input, which is also displayed

    fprintf(mstring('\\nVisualizing the projected (reduced dimension) faces.\\n\\n'))

    K = 100
    X_rec = recoverData(Z, U, K)

    # Display normalized data
    subplot(1, 2, 1)
    displayData(X_norm(mslice[1:100], mslice[:]))
    title(mstring('Original faces'))
    axis(mstring('square'))

    # Display reconstructed data from only k eigenfaces
    subplot(1, 2, 2)
    displayData(X_rec(mslice[1:100], mslice[:]))
    title(mstring('Recovered faces'))
    axis(mstring('square'))

    fprintf(mstring('Program paused. Press enter to continue.\\n'))
    pause()


    #% === Part 8(a): Optional (ungraded) Exercise: PCA for Visualization ===
    #  One useful application of PCA is to use it to visualize high-dimensional
    #  data. In the last K-Means exercise you ran K-Means on 3-dimensional 
    #  pixel colors of an image. We first visualize this output in 3D, and then
    #  apply PCA to obtain a visualization in 2D.

    close(mstring('all'), mstring('close'), mstring('all'), mstring('clc'))

    # Reload the image from the previous exercise and run K-Means on it
    # For this to work, you need to complete the K-Means assignment first
    A = double(imread(mstring('bird_small.png')))

    # If imread does not work for you, you can try instead
    #   load ('bird_small.mat');

    A = A / 255
    img_size = size(A)
    X = reshape(A, img_size(1) * img_size(2), 3)
    K = 16
    max_iters = 10
    initial_centroids = kMeansInitCentroids(X, K)
    [centroids, idx] = runkMeans(X, initial_centroids, max_iters)

    #  Sample 1000 random indexes (since working with all the data is
    #  too expensive. If you have a fast computer, you may increase this.
    sel = floor(rand(1000, 1) * size(X, 1)) + 1

    #  Setup Color Palette
    palette = hsv(K)
    colors = palette(idx(sel), mslice[:])

    #  Visualize the data and centroid memberships in 3D
    figure()
    scatter3(X(sel, 1), X(sel, 2), X(sel, 3), 10, colors)
    title(mstring('Pixel dataset plotted in 3D. Color shows centroid memberships'))
    fprintf(mstring('Program paused. Press enter to continue.\\n'))
    pause()

    #% === Part 8(b): Optional (ungraded) Exercise: PCA for Visualization ===
    # Use PCA to project this cloud to 2D for visualization

    # Subtract the mean to use PCA
    [X_norm, mu, sigma] = featureNormalize(X)

    # PCA and project the data to 2D
    [U, S] = pca(X_norm)
    Z = projectData(X_norm, U, 2)

    # Plot in 2D
    figure()
    plotDataPoints(Z(sel, mslice[:]), idx(sel), K)
    title(mstring('Pixel dataset plotted in 2D, using PCA for dimensionality reduction'))
    fprintf(mstring('Program paused. Press enter to continue.\\n'))
    pause()
