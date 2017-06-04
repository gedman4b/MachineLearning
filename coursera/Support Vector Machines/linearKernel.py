@mfunction("sim")
def linearKernel(x1=None, x2=None):
    # LINEARKERNEL returns a linear kernel between x1 and x2
    #   sim = linearKernel(x1, x2) returns a linear kernel between x1 and x2
    #   and returns the value in sim

    # Ensure that x1 and x2 are column vectors
    x1 = x1(mslice[:])
    x2 = x2(mslice[:])
    print(x2)


    # Compute the kernel
    sim = x1.cT * x2# dot product

end
