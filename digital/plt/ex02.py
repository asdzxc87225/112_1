import matplotlib.pyplot as plt 
import numpy as np 

class LineSet():
    def __init__(self):
        self.x = [x for x in range(10)]
        self.y = [self.x[y]  for y in range(10)]
        plt.plot(self.x,self.y,'ro')
        self.setLabel()

    def setLabel(self):
        plt.xlabel('x-label')
        plt.ylabel('y-label')

if __name__ == "__main__":
    line = LineSet()
    plt.show()

