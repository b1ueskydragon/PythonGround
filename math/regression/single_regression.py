import numpy as np

# Real Data
x = np.array([1, 2, 3])
y = np.array([2, 3.9, 6.1])

# Centering
xc = x - x.mean()
yc = y - y.mean()

# calc parameter slop `a`
# element product
xy = xc * yc
xx = xc * xc

a = xy.sum() / xx.sum()

if __name__ == '__main__':
    print(a)
