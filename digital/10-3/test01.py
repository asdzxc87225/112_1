import matplotlib.pyplot as plt 
import matplotlib
import numpy as np 

class LinSet():
    def __init__(self,x,y,typ):
        self.x = x
        self.y = y
        self.typ = typ

def ex01():
    plt.figure(1) 
    plt.subplot(211)
    plt.plot([1,2,3],'r+-')

    plt.subplot(212)
    plt.plot([4,5,5],'g-d')

    plt.figure(2)
    plt.subplot(251)
    plt.plot([1,2,3],'k-+')

    plt.subplot(2,5,10)
    plt.plot([4,5,5],'b-s')

    plt.show()

def ex02():
    f,ax = plt.subplots(2,2, sharex = 'col', sharey='row')
    x = np.linspace(0, 2*np.pi,20)
    y = np.sin(x)

    ax[0,0].plot(x,y)
    ax[0,0].set_title('sin(x)')
    ax[0,0].set_ylabel('Y1')

    ax[0,1].plot(x,y*2)
    ax[0,1].set_title('2*sin(x)')

    ax[1,0].plot(x,y*0.5)
    ax[1,0].set_title('0.5*sin(x)')
    ax[1,0].set_xlabel('X3')
    ax[1,0].set_ylabel('Y3')
    ax[1,0].set_xticks((0,2,4,6))
    
    ax[1,1].plot(x,y*3)
    ax[1,1].set_title('3*sin(x)')
    ax[1,1].set_xlabel('X4')
    
def ex02_no():
    f,ax = plt.subplots(2,2, sharex = 'none')
    x = np.linspace(0, 2*np.pi,20)
    y = np.sin(x)

    ax[0,0].plot(x,y)
    ax[0,0].set_title('sin(x)')
    ax[0,0].set_ylabel('Y1')

    ax[0,1].plot(x,y*2)
    ax[0,1].set_title('2*sin(x)')

    ax[1,0].plot(x,y*0.5)
    ax[1,0].set_title('0.5*sin(x)')
    ax[1,0].set_xlabel('X3')
    ax[1,0].set_ylabel('Y3')
    ax[1,0].set_xticks((0,2,4,6))
    
    ax[1,1].plot(x,y*3)
    ax[1,1].set_title('3*sin(x)')
    ax[1,1].set_xlabel('X4')
    


def ex03():
    f,ax = plt.subplots(2,2,sharex = 'col',sharey='row')
    f.subplots_adjust(hspace = 0.6,wspace = 0.1)
    x = np.linspace(0,2*np.pi,20)
    y = np.sin(x)

    ax[0,0].plot(x,y)
    ax[0,0].set_title('sin(x)')
    ax[0,0].set_ylabel('Y1')

    ax[0,1].plot(x,2*y)
    ax[0,1].set_title('2*sin(x)')
    
    ax[1,0].plot(x,y*0.5)
    ax[1,0].set_title('0.5*sin(x)')
    ax[1,0].set_ylabel('Y3')
    ax[1,0].set_xlabel('X3')
    ax[1,0].set_xticks((0,2,4,6))
    ax[1,0].set_xlim(0,6.5)

    ax[1,1].plot(x,3*y)
    ax[1,1].set_title('3*sin(x)')
    ax[1,1].set_xlabel('X4')

def ex04():
    x = np.linspace(0,2*np.pi,20)

    plt.subplot(2,1,1)
    plt.plot(x, np.sin(x),color='purple')
    plt.title(r'sin(2*$\pi$*x)')
    plt.text(3,0.5,r'sin($2 * \pi * x$)')

    plt.subplot(234)
    plt.plot(x,1.5*np.sin(1.5*x),color='y')
    plt.title(r'1.5sin(3*$\pi$*x)')
    plt.text(3,0.5,r'1.5sin($3 * \pi * x$)')

    plt.subplot(235)
    plt.plot(x,1*np.cos(x),color='olive')
    plt.title(r'cos(2*$\pi$*x)')
    plt.text(3,0.5,r'cos($2 * \pi * x$)')

    plt.subplot(236)
    plt.plot(x,2*np.cos(2*x),color='lime')
    plt.title(r'2cos(4*$\pi$*x)')
    plt.text(3,0.5,r'2cos($4 * \pi * x$)')

def ex04_2():

    x = np.linspace(0,2*np.pi,20)

    plt.subplot(2,1,1)
    plt.plot(x,np.sin(x),color='purple')

    ax2 = plt.subplot(2,3,4)
    plt.plot(x,2*np.sin(x),color='y')
    plt.yticks(np.linspace(1,-1,10))
    plt.ylim(-1,1)


    ax2 = plt.subplot(2,3,5,sharey =ax2)
    plt.plot(x,np.sin(x),color='olive')

    ax2 = plt.subplot(2,3,6,sharey =ax2)
    plt.plot(x,np.sin(x),color='lime')


    

if  __name__ == "__main__":
    #matplotlib.rc('font',family='AR PL UKai CN')
    ex04_2()
    plt.show()
