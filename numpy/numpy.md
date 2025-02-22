# Python Numpy Tutorial

## What are NumPy Arrays?
###  NumPy is a Python package that stands for ‘Numerical Python’. It is the core library for scientific computing, which contains a powerful n-dimensional array object.

## Where is NumPy used?
### Python NumPy arrays provide tools for integrating C, C++, etc. It is also useful in linear algebra, random number capability etc. NumPy array can also be used as an efficient multi-dimensional container for generic data.

### *Python NumPy Array*: Numpy array is a powerful N-dimensional array object which is in the form of rows and columns. We can initialize NumPy arrays from nested Python lists and access it elements. In order to perform these NumPy operations.

## How do I install NumPy?
### To install Python NumPy, go to your command prompt and type “pip install numpy”. Once the installation is completed, go to your IDE (For example: PyCharm) and simply import it by typing: “import numpy as np”

## Single-dimensional Numpy Array:
`
import numpy as np
a=np.array([1,2,3])
print(a)
`

## Multi-dimensional Array:

`
a=np.array([(1,2,3),(4,5,6)])
print(a)
`
# Python NumPy Array v/s List

## Why NumPy is used in Python?

### We use python NumPy array instead of a list because of the below three reasons:

### Less Memory
### Fast
### Convenient

`
import numpy as np

import time
import sys
S= range(1000)
print(sys.getsizeof(5)*len(S))

D= np.arange(1000)
print(D.size*D.itemsize)
`
### The above output shows that the memory allocated by list (denoted by S) is 14000 whereas the memory allocated by the NumPy array is just 4000. From this, you can conclude that there is a major difference between the two and this makes Python NumPy array as the preferred choice over list.

`
import time
import sys

SIZE = 1000000

L1= range(SIZE)
L2= range(SIZE)
A1= np.arange(SIZE)
A2=np.arange(SIZE)

start= time.time()
result=[(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)

start=time.time()
result= A1+A2
print((time.time()-start)*1000)
`
### In the above code, we have defined two lists and two numpy arrays. Then, we have compared the time taken in order to find the sum of lists and sum of numpy arrays both. If you see the output of the above program, there is a significant change in the two values. List took 380ms whereas the numpy array took almost 49ms.

# ndim
### You can find the dimension of the array, whether it is a two-dimensional array or a single dimensional array.

`
import numpy as np
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)
`

# itemsize
### You can calculate the byte size of each element.
`
import numpy as np
a = np.array([(1,2,3)])
print(a.itemsize)
`
# dtype

### You can find the data type of the elements that are stored in an array. So, if you want to know the data type of a particular element, you can use ‘dtype’ function which will print the datatype along with the size. 

`
import numpy as np
a = np.array([(1,2,3)])
print(a.dtype)
`