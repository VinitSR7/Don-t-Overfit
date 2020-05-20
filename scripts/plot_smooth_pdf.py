def plot_smoothed_pdf(data):
    # refer - https://stackoverflow.com/questions/37373457/how-to-plot-probability-density-function-pdf-of-inter-arrival-time-of-events
    import numpy as np
    import scipy.stats
    import matplotlib.pyplot as plt
    # generate data samples
    data = scipy.stats.expon.rvs(loc=0, scale=1, size=1000, random_state=123)
    scipy.stats.gaussian_kde(data)
    
    # test values for the bw_method option ('None' is the default value)
    bw_values =  [None, 0.1, 0.01]

    # generate a list of kde estimators for each bw
    kde = [scipy.stats.gaussian_kde(data,bw_method=bw) for bw in bw_values]


    # plot (normalized) histogram of the data
     
    plt.hist(data, 50, normed=1, facecolor='green', alpha=0.5);

    # plot density estimates
    t_range = np.linspace(-2,8,200)
    for i, bw in enumerate(bw_values):
        plt.plot(t_range,kde[i](t_range),lw=2, label='bw = '+str(bw))
    plt.xlim(-1,6)
    plt.legend(loc='best')
