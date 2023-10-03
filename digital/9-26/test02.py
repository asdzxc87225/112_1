import matplotlib.pyplot as plt
import numpy as np

def p8 ():
    x = np.linspace(0,4*np.pi,50)
    y = np.sin(x)

    plt.plot(x,y,color = 'silver',ls='-',marker='|',label= 'sin(x)' )
    plt.plot(x,y*2,color = 'navy',ls=':',marker='o',label= '2sin(x)' )
    plt.legend(loc='lower left')

    plt.title("sin(x) & 2sin(x)")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xticks((0,2,4,6))
    plt.yticks((-2,-1,0,1,2),('a','b','c','','e'))
    #plt.show()

    plt.xlim([0,10.5])
    plt.ylim([-2.5,2.5])

def line ():
    x = np.linspace(0,4*np.pi,50)
    y = np.sin(2*x)

    plt.plot(x,y,color = 'red',ls='-',marker='d',label = 'sin(2x)' )
    plt.plot(x,y*2,color = 'green',ls=':',marker='+' ,label='2sin(2x)')
    plt.legend(loc = 'lower right')

    plt.title("sin(x) & 2sin(x)")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xticks((0,2,4,6))
    plt.yticks((-2,-1,0,1,2),('a','b','c','','e'))

    plt.xlim([0,10.5])
    plt.ylim([-2.5,2.5])




if __name__ == "__main__":
    line()
    p8()
    plt.show()
