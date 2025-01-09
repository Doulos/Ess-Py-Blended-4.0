#!/usr/bin/env python
# coding: utf-8

"""
Create a one-dimensional NumPy array initialized with the integer values 1 
through 12.
"""

import numpy as np

a = np.arange(1, 13)
print("a=\n", a)


"""
Add a second axis (dimension) to this array so that it becomes a 2-dimensional
array containing a single column of 12 elements, that is, 12 rows by 1 column.
"""
a2d = a[:, np.newaxis]
print("a2d=\n", a2d)


"""
Perform an element-wise multiplication of this 12 x 1 array with its transpose
(1 row by 12 columns) to create a multiplication table that contains the
product of every integer between 1 and 12 with every integer between 1 and 12.
Print the values of this multiplication table.
"""
multiplication_table = a2d * a2d.T
print("multiplication_table=\n", multiplication_table)


"""
Now create two separate 4 x 4 NumPy arrays named A and B, each array
initialized with random floating-point numbers between 0.0 and 1.0
"""

A = np.random.rand(4, 4)
B = np.random.rand(4, 4)
print("A=\n", A, "B=\n", B)

"""
Create a third 4 x 4 NumPy array, where each element is True if the 
corresponding element of A is greater than that of B, and False otherwise.
In other words, the third 4 x 4 array is an array-of-Booleans.
"""
C = A > B
print("C=\n", C)


"""
Create a NumPy array containing only the elements of A for which the 
corresponding element of the array-of-Booleans is True, that is, only the 
elements of A that are greater than the corresponding elements of B.
"""
greater_elements = A[C]
print("greater_elements=\n", greater_elements)


"""
Create another NumPy array containing only the corresponding elements of B, 
that is, only the elements of B that are less than or equal to the
corresponding elements of A.
"""
lesser_elements = B[C]
print("lesser_elements=\n", lesser_elements)


"""
Create yet another Numpy array that stacks these two arrays of greater and
lesser elements vertically. This array should have exactly two rows, but the
number of columns will be data-dependent, depending on the random
floating-point values.
"""
stacked_arrays = np.vstack((greater_elements, lesser_elements))
print("stacked_arrays=\n", stacked_arrays)
