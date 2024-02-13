# Library Overview
## What library
NumPy for Python
## What purpose does it serve
Python is a language that offers ease of use, at the expense of memory management. It can run slowly when working with vast amounts of data.

NumPy is a library that is programmed in Python and C [ref](https://numpy.org/devdocs/user/whatisnumpy.html). This way, there are the memory management benefits of C, along with the ease of use from Python. To use it, you need to import it to your program, and create a np array. From there, you can do so much more than what Python would normally allow.

This includes getting the indexes of every element in an array that fulfills a condition (can also be returned as a flattened array index), indexing a >1D array using a flattened index, Using an array of indexes on an array to get an array of corresponding elements, multiplying two arrays together. multiply, add, subtract, or divide every element in an array by a scalar value, creating arrays of any size containing random numbers of a specified range, and more [ref](https://numpy.org/doc/).

## Examples of functionalities
np.zeros(x) - Creates an array of zeroes of size x (Can be multidimensional).

np.random.randint(a, b, x) - Creates an array of size x (Can be multidimensional), filled with random ints between a and b.

np.multiply(a, b) - multiplies the contents of two arrays (not matrix multiplication)

np.matmul(a, b) - multiplies two matrices

np.where(condition) - checks every element of an array involved in a conditional statement, and returns a list of indexes whose elements satisfy the condition.

np.flatnonzero(condition) - Like np.where(), but used for multidimensional arrays. Will return a list of indexes for the flattened equivalent of the array.

ab = np.append(a, b)

abUnique, abInstances = np.unique(ab, return_counts = True)

abRepeatedindexes = np.where(abInstances > 1)

abRepeated = abUnique[abRepeatedindexes] - These four lines will return a list of repeated numbers between two arrays.
## When was it created
NumPy was created in 2005, building off of the pre-existing numeric and numarray libraries. [ref](https://numpy.org/about/)
## Why NumPy
I chose this library because with languages like javascript and numpy, I can sometimes feel a little disconnected from what is actually happening in the computer, like there are fewer ways to get creative when trying to find the solution to a problem. Numpy provides a wide variety of functionality to arrays that lets you get creative and consise when solving issues.
## How has it influenced learning?
Explorring this library made me realize two things. 1, How restrictive arrays are in most languages, and 2, how far removed python is from base memory. The things you can do in Numpy would be incredibly inefficient if done in Python.
## Overall Experience
I had a greaat experience with this library. If anyone needs to work with arrays in Python, Numpy is nearly a neccessity. I will absolutely continue using this library. The level of abstraction it allows is much cleaner than the loops that would otherwise be required.