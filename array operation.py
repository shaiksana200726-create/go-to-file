# Basic Array Information
import numpy  as  np
arr = np.array([1,2,3,4,5])
print(arr.ndim)       #Return the number of dimensions (axes) of the array

print(arr.shape)   #Return a tuple shouing the size of the array in  each dimension(row,column, etc.).

print(arr.size)   #Return the total number of elements in the array

print(arr.dtype)   #Return the data type of the elements in the array

#Creating Arrays with Numpy
import numpy as np
print(np.zeros(5))    #Creating an array of 5
print(np.ones(5))       #Creates an array of 5
print(np.arange (1,10,2))     #Creates an array


#Indexing and Slicing
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr[0])  #First element
print(arr[-1])  #Last element
