import numpy as np
 # 1D array
arr1 = np.array([1,2,3,4,5])
print(arr1)

#2D array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

#Adding 2 Arrays using python arrays(with looping):
import array
a = array.array('i',[1,2,3])
b = array.array('i',[4,5,6])
result = array.array('i',[a[i] + b[i] for i in range(len(a))])
print(result)


#Using Numpy Array(Vectorized)
import array 
a = np.array([1,2,3])
b = np.array([4,5,6])
result = a+b
print(result) 