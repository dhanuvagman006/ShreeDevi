# Python NumPy Tutorial

## What are NumPy Arrays?
NumPy is a Python package that stands for ‘Numerical Python’. It is the core library for scientific computing, which contains a powerful n-dimensional array object. It provides various functionalities for handling numerical data efficiently.

## Where is NumPy used?
NumPy arrays provide tools for integrating C, C++, etc. It is also useful in linear algebra, random number capability, and complex mathematical operations. NumPy arrays serve as an efficient multi-dimensional container for generic data, making them widely used in data science, artificial intelligence, and machine learning.

## Installing NumPy
To install Python NumPy, use the following command in your terminal or command prompt:
```bash
pip install numpy
```
Once the installation is completed, you can import it into your script:
```python
import numpy as np
```

## Creating NumPy Arrays
### Single-dimensional NumPy Array
```python
import numpy as np

a = np.array([1, 2, 3])
print(a)
```
**Explanation:**
1. `np.array([1, 2, 3])` creates a one-dimensional NumPy array with the elements `[1, 2, 3]`.
2. The `print(a)` statement outputs `[1 2 3]` to the console.

### Multi-dimensional Array
```python
a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)
```
**Explanation:**
1. `np.array([(1, 2, 3), (4, 5, 6)])` creates a two-dimensional NumPy array (a matrix) with two rows and three columns.
2. The `print(a)` statement outputs:
```
[[1 2 3]
 [4 5 6]]
```

## NumPy vs Python List

### Why Use NumPy Over Lists?
NumPy arrays are preferred over lists because they are:
1. **Memory Efficient** – NumPy arrays consume less memory than Python lists.
2. **Faster** – Operations on NumPy arrays execute faster.
3. **More Convenient** – NumPy provides built-in functions for various operations.

#### Memory Efficiency
```python
import numpy as np
import sys

S = range(1000)
print(sys.getsizeof(5) * len(S))  # Memory occupied by list

D = np.arange(1000)
print(D.size * D.itemsize)  # Memory occupied by NumPy array
```
**Explanation:**
1. `sys.getsizeof(5) * len(S)` calculates the memory occupied by a list of 1000 elements.
2. `D.size * D.itemsize` calculates the memory occupied by a NumPy array of the same size.
3. The output shows that NumPy uses significantly less memory than lists.

#### Speed Comparison
```python
import time
import numpy as np

SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)
A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x, y) for x, y in zip(L1, L2)]
print((time.time() - start) * 1000)  # Time taken by list operation

start = time.time()
result = A1 + A2
print((time.time() - start) * 1000)  # Time taken by NumPy operation
```
**Explanation:**
1. Two lists (`L1` and `L2`) and two NumPy arrays (`A1` and `A2`) are created with one million elements.
2. The time taken to sum the elements of lists is measured and compared with the time taken for NumPy arrays.
3. The NumPy operation is much faster due to its optimized implementation.

## NumPy Array Properties
### ndim - Number of Dimensions
```python
import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])
print(a.ndim)
```
**Explanation:**
1. `a.ndim` returns `2` because the array has two dimensions.

### itemsize - Byte Size of Each Element
```python
import numpy as np

a = np.array([1, 2, 3])
print(a.itemsize)
```
**Explanation:**
1. `a.itemsize` returns the size of each element in bytes.

### dtype - Data Type of Elements
```python
import numpy as np

a = np.array([1, 2, 3])
print(a.dtype)
```
**Explanation:**
1. `a.dtype` returns the data type of the elements, such as `int32` or `int64`.

## NumPy Operations
### Reshaping Arrays
```python
import numpy as np

a = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])
print(a.reshape(4, 2))
```
**Explanation:**
1. `a.reshape(4, 2)` converts the 2x4 array into a 4x2 array.

### Slicing Arrays
```python
import numpy as np

a = np.array([10, 20, 30, 40, 50])
print(a[1:4])
```
**Explanation:**
1. Extracts elements from index `1` to `3`, returning `[20, 30, 40]`.

### Creating Arrays with Zeros and Ones
```python
import numpy as np

print(np.zeros((2, 3)))  # 2x3 matrix of zeros
print(np.ones((3, 3)))  # 3x3 matrix of ones
```
**Explanation:**
1. `np.zeros((2, 3))` creates a 2x3 matrix filled with zeros.
2. `np.ones((3, 3))` creates a 3x3 matrix filled with ones.

### Creating Arrays with a Range of Values
```python
import numpy as np

print(np.arange(10, 50, 5))  # Numbers from 10 to 50 with step 5
print(np.linspace(0, 10, 5))  # 5 evenly spaced numbers from 0 to 10
```
**Explanation:**
1. `arange` generates numbers in a range with a specified step.
2. `linspace` generates evenly spaced numbers in a range.

### Statistical Operations
```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a.min())  # Minimum value
print(a.max())  # Maximum value
print(a.sum())  # Sum of all elements
print(a.mean())  # Mean value
```
**Explanation:**
1. Computes and prints the min, max, sum, and mean of the array.

### Matrix Operations
```python
import numpy as np

a = np.array([(1, 2), (3, 4)])
b = np.array([(5, 6), (7, 8)])

print(np.dot(a, b))  # Matrix multiplication
print(np.transpose(a))  # Transpose of matrix
```
**Explanation:**
1. `np.dot(a, b)` computes matrix multiplication.
2. `np.transpose(a)` returns the transposed matrix.

## Conclusion
NumPy is a powerful library for numerical computing in Python. It provides efficient array operations, mathematical functions, and statistical tools, making it a preferred choice for scientific computing, data analysis, and machine learning.

