import  matplotlib.pyplot as plt 
import  matplotlib
import numpy as np

matplotlib.rc('font', family='TW-Sung')

if __name__ == '__main__':
    x = np.linspace(0,2*np.pi,10)
    y = np.sinc(x)
    plt.plot()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.yticks(np.linspace(0,1,11))
    plt.xticks(np.linspace(0,6,7))

    plt.title(r'home work')
    plt.text(1,0.9,r'\text',fontsize=18)
    plt.text(5,0.6,r'$\alpha^\gamma$',fontsize=20)
    plt.text(1,0.2,'C110185120\n姓名:劉仁承',fontsize=18)
    plt.show()
