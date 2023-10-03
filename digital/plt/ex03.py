import matplotlib.pyplot as plt
import numpy as np

class LineSet():
    def __init__(self):
        self.t = np.arange(0,5,0.2)
        print("t = ",self.t)
        plt.plot(self.t,self.t, 'r--', self.t,self.t**2,'gs',self.t,self.t**3,'b^')

if __name__ == "__main__":
    l1 = LineSet()
        plt.show()
