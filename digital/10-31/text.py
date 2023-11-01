import numpy as np
import matplotlib.pyplot as plt 

if __name__ == "__main__":
    f,ax = plt.subplots(3,3,sharex='col',sharey='row')
    t = np.linspace(0,1,1000)
    x = 1*np.cos(2*np.pi*1*t)
    ax[0,0].plot(t,x)
    ax[0,0].set_title('A=1')
    x = 2*np.cos(2*np.pi*1*t)
    ax[0,1].plot(t,x)
    ax[0,1].set_title('A=2')
    x = 4*np.cos(2*np.pi*1*t)
    ax[0,2].plot(t,x)
    ax[0,2].set_title('A=4')

    x = 10*np.cos(2*np.pi*5*t)
    ax[1,0].plot(t,x)
    ax[1,0].set_title('f=1')
    x =10 * np.cos(2*np.pi*10*t)
    ax[1,1].plot(t,x)
    ax[1,1].set_title('f=10')
    x =10 * np.cos(2*np.pi*15*t)
    ax[1,2].plot(t,x)
    ax[1,2].set_title('f=15')
    
    x = 5*np.cos(2*np.pi*1*t)
    ax[2,0].plot(t,x)
    ax[2,0].set_title('$\phi =0$')
    x =5*np.cos(2*np.pi*1*t+np.pi/4)
    ax[2,1].plot(t,x)
    ax[2,1].set_title('$\phi =\pi / 4$')
    x = 5*np.cos(2*np.pi*1*t+np.pi/2)
    ax[2,2].plot(t,x)
    ax[2,2].set_title('$\phi =\pi / 2$')

    plt.show()
