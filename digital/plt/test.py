import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib as mpl 

def ex1():
    fig, ax = plt.subplots()
    ax.plot([1,2,3,4],[1,4,2,3])
    plt.show()
def ex2():
    fig = plt.figure()  # an empty figure with no Axes
    fig, ax = plt.subplots()  # a figure with a single Axes
    fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
    # a figure with one axes on the left, and two on the right:
    fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])
    plt.show()
def ex3():
    b = np.matrix([[1, 2], [3, 4]])
    b_asarray = np.asarray(b)
    np.random.seed(19680801)  # seed the random number generator.
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.scatter('a', 'b', c='c', s='d', data=data)
    ax.set_xlabel('entry a')
    ax.set_ylabel('entry b')
    plt.show()

def ex4():
    x = np.linspace(0, 2, 100)  # Sample data.

    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x, x, label='linear')  # Plot some data on the axes.
    ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
    ax.plot(x, x**3, label='cubic')  # ... and some more.
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title("Simple Plot")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.show()

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out

def ex5():
    data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
    fig, ax = plt.subplots(2, 2, figsize=(5, 2.7))
    a = {'marker': 'x','color':'blue'}
    my_plotter(ax[0,0], data1, data2, {'marker': 'x'})
    my_plotter(ax[0,1], data3, data4, {'marker': 'o'})
    my_plotter(ax[1,0], data3, data4, a)
    plt.show()

if __name__ == "__main__":
    ex5()
