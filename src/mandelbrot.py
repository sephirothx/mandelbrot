from numba import jit

@jit
def mandelbrot(re, im, iterations=100):
    c = complex(re, im)
    z = 0
    for i in range(iterations):
        z = z*z + c
        if abs(z) > 2:
            return i
    return 0