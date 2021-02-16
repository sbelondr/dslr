def SGD(f, theta0, alpha, num_iters):
    """ 
       Arguments:
       f -- the function to optimize, it takes a single argument
            and yield two outputs, a cost and the gradient
            with respect to the arguments
       theta0 -- the initial point to start SGD from
       num_iters -- total iterations to run SGD for       Return:
       theta -- the parameter value after SGD finishes
    """
    start_iter = 0
    theta= theta0
    for iter in range(start_iter + 1, num_iters + 1):
        _, grad = f(theta)
        theta = theta - (alpha * grad) # there is NO dot product!
    return theta