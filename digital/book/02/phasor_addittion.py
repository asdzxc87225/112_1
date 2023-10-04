import numpy as np 
import matplotlib.pyplot as plt

class FuntionBuild():
    def __init__(self):
        self.t = np.linspace(0,1,1000,endpoint = False)
        self.x1 = 3 * np.cos(2 * np.pi * 10 * self.t + np.pi/4)
        self.x2 = 4 * np.cos(2 * np.pi * 10 * self.t + 3 * np.pi/4)
        self.x3 = self.x1 + self.x2
        plt.plot(self.t,self.x1,'-',label='x1(t)')
        plt.plot(self.t,self.x2,'-',label='x2(t)')
        plt.plot(self.t,self.x3,'-',label='x3(t)')

        plt.legend(loc = 'upper right')
        plt.xlabel('t(second)')
        plt.ylabel('Amplitude')
        plt.axis([0,1,-6,6])



if __name__ == "__main__":
    f1 = FuntionBuild()
    plt.show()
