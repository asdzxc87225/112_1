import numpy as np
import matplotlib.pyplot as plt 

if __name__ == '__main__':
    t = np.linspace(0,1,1000,endpoint=False)
    x = np.cos(2*np.pi*5*t)

    plt.plot(t,x)
    plt.xlabel('t(second)')
    plt.ylabel('Amplitude')
    plt.show()
