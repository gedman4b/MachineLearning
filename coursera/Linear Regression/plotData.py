@mfunction("")
def plotData(x=None, y=None):
    #PLOTDATA Plots the data points x and y into a new figure 
    #   PLOTDATA(x,y) plots the data points and gives the figure axes labels of
    #   population and profit.

    figure()# open a new figure window

    data = load(mstring('ex1data1.txt'))# read comma separated data
    X = data(mslice[:], 1)
    y = data(mslice[:], 2); print y

    m = length(y)# number of training examples

    plot(X, y, mstring('rx'), mstring('MarkerSize'), 10)# Plot the data
    ylabel(mstring('Profit in $10,000s'))# Set the y axis label
    xlabel(mstring('Population of City in 10,000s'))# Set the x axis label

end
