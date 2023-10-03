import matplotlib.pyplot as plt
import numpy as np

class LineSet():
    def __init__(self):
        self.x = np.arange(0,5,0.1)
        self.y1 = np.sin(2*np.pi*self.x)
        self.y2 = np.cos(2*np.pi*self.x)
        plt.subplot(211);plt.plot(self.x,self.y1,'b-')
        plt.subplot(212);plt.plot(self.x,self.y2,'r--')
if __name__ == "__main__":
    l1 = LineSet()
    plt.show()
        
