import matplotlib.pyplot as plt
import numpy as np 

class LineSet():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        plt.plot(self.x, self.y)


if __name__ == "__main__":
    arr = []
    arr.append(np.linspace(0,2*np.pi,100))
    arr.append(np.sin(arr[0]))
    arr.append(arr[0])
    l1 = LineSet(arr[0],arr[1])
    l2 = LineSet(arr[0],arr[2])
    plt.show()


