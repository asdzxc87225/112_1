import matplotlib.pyplot as plt
import numpy as np 

class LineData():
    def __init__(self):
        self.x = [x for x in range(10)]
        self.y = self.x
        plt.plot(self.x, self.y)
        plt.show()
         
if  __name__ == "__main__":
    line1 = LineData()
