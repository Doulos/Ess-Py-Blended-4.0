#!/usr/bin/env python
# coding: utf-8

"""
Create four subplots where each subplot shows two superimposed sine waves,
each of a different wavelength, 8 sine waves in total.
Use `np.linspace` to generate the x values. Give each subplot a distinct title. Add appropriate x and y labels to each plot.
Experiment with various line colors, line weights, and plotting symbols.
Increase the size of the plots so that they are easily readable.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

plt.figure(figsize=(12, 10))

plt.subplot(221)
plt.title("Plot 1")
plt.xlabel("x")
plt.ylabel("sin(x), sin(1.5x)")
plt.plot(x, np.sin(1.0 * x), linewidth=10.0)
plt.plot(x, np.sin(1.5 * x), "r")

plt.subplot(222)
plt.title("Plot 2")
plt.xlabel("x")
plt.ylabel("sin(2x), sin(2.5x)")
plt.plot(x, np.sin(2.0 * x), "y")
plt.plot(x, np.sin(2.5 * x), "g")

plt.subplot(223)
plt.title("Plot 3")
plt.xlabel("x")
plt.ylabel("sin(3x), sin(3.5x)")
plt.plot(x, np.sin(3.0 * x), "k")
plt.plot(x, np.sin(3.5 * x), "o")

plt.subplot(224)
plt.title("Plot 4")
plt.xlabel("x")
plt.ylabel("sin(4x), sin(4.5x)")
plt.plot(x, np.sin(4.0 * x), "v")
plt.plot(x, np.sin(4.5 * x), "s")
plt.show()

"""
Create a 3-D surface plot in the shape of a dome, for example by plotting the
function -(x**2+y**2)
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-1, 1, 20)
y = np.linspace(-1, 1, 20)
X, Y = np.meshgrid(x, y)
Z = -(X**2) - Y**2

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap=matplotlib.cm.plasma)
plt.show()
