import numpy as np

z = 3 + 4j
magnitude = abs(z)
theta = np.angle(z)*180/np.pi

print("z=",z)
print("Magnitude =",magnitude)
print("Phase Angle=",theta)
