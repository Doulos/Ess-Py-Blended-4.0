#!/usr/bin/env python
# coding: utf-8

# # Exercise 20 - NumPy

"""
Create a NumPy array consisting of 5 rows and 3 columns,
where each element is initialized to a random floating-point number 
between 0.0 and 1.0
"""

import numpy as np

a = np.random.rand(5, 3)
print("a=\n", a)


"""
Sort the numbers within each of the 3 individual columns in ascending order
"""
a_sorted = np.sort(a, axis=0)
print("a_sorted=\n", a_sorted)

"""
Plot the values of this 5 x 3 matrix using matplotlib. There should be 3 lines on the plot, one line per column, that each climb across the plot from left to right because the numbers in each column are in ascending order.
"""
import matplotlib.pyplot as plt

plt.plot(a_sorted)

"""
Transpose the sorted 5 x 3 array into a 3 x 5 array, then plot the values of the new 3 x 5 array using matplotlib. There should be 5 non-intersecting lines on the plot, one line per column.
"""
a_transposed = a_sorted.transpose(1, 0)
plt.plot(a_transposed)


"""
Create a one-dimensional NumPy array of 5 elements that contains the minimum values of each of the 5 columns of the transposed 3 x 5 array, and another one-dimensional NumPy array of 5 elements that contains the maximum values of each of the 5 columns.
"""
min_values = a_transposed.min(axis=0)
print("min_values=\n", min_values)

max_values = a_transposed.max(axis=0)
print("max_values=\n", max_values)


"""
Create a two-dimensional NumPy array of 2 rows and 5 columns, where the first row contains the 5 minimum values and the second row contains the 5 maximum values calculated above.
"""
min_and_max = np.empty((2, 5))
min_and_max[0] = min_values
min_and_max[1] = max_values
print("min_and_max=\n", min_and_max)


"""
Plot the transposed array. There should be 2 lines on the plot, each climbing across the plot from left to right because the minimum values and maximum values should both be in ascending order.
"""
plt.plot(min_and_max.T)
plt.show()
