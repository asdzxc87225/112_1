import matplotlib.pyplot as plt
import numpy as np

class line1 ():
    def __init__(self):
        self.x = np.linespace(0,2*np.pi,40)
        self.y = np.sin(x)
        plt.plot(self.x,self.y)
        plt.show()

if __name__ == "__main__":
    print('t')
    p1 = line1
    print(p1.x)
    plt.show()
