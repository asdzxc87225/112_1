import matplotlib.pyplot as plt
import numpy as np

class p1:
    def __init__(self):
        self.x = [x for x in range(10)]
        self.y = [y for y in range(10)]
        plt.plot(self.x, self.y)

def p2():
    x = [x for x in range(10)]
    y = [y for y in range(10)]
    y1 = [y + 10 for y in range(10)]
    y2 = [y ** 2 + 2 for y in range(10)]
    y3 = [1 * y ** 3 + 3 for y in range(10)]
    plt.plot(x, y)
    plt.plot(x, y1, lw=3)
    plt.plot(x, y2, 'ro')
    plt.plot(x, y3, lw=10)  # 添加x参数
    plt.xlabel('x-label')
    plt.ylabel('y-label')

if __name__ == "__main__":
    p = p1()
    p2()

