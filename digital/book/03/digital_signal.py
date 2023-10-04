import numpy as np 
import matplotlib.pyplot as plt 

n = np.array([0,1,2,3,4,5])
x = np.array([1,2,3,4,5,6])
plt.stem(n,x)
plt.xlabel('n')
plt.ylabel(r'$x[n]$')
plt.show()
