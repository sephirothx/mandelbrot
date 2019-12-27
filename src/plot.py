import numpy as np
import matplotlib.pyplot as plt
from mandelbrot import mandelbrot

X = 1000
Y = 1000

x_start, x_end, y_start, y_end = -2, 1, -1.5, 1.5

result = np.zeros([Y, X])

for x, re in enumerate(np.linspace(x_start, x_end, X)):
    for y, im in enumerate(np.linspace(y_start, y_end, Y)):
        result[y, x] = mandelbrot(re, im)

plt.imshow(result, cmap='CMRmap', interpolation='nearest')
plt.axis('off')
plt.show()