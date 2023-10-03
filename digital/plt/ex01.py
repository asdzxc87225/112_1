import matplotlib.pyplot as plt 
import numpy as np

class LineSet():
    def __init__(self):
        self.x = [x for x in range(10)]
        self.y = [self.x[y]**2 for y in range(10)]
        plt.plot(self.x,self.y,lw=3)

if __name__ == "__main__":
    a = LineSet()
    plt.show()
