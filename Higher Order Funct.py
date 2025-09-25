def square(X):
    return X*X
numbers = [1,2,3,4,5]
squared = list(map(square,numbers))
print(squared)

def is_even(X):
    return X%2==0
numbers = [1,2,3,4,5,6]
even_numbers = list (filter(is_even,numbers))
print(even_numbers)

from functools import reduce
def add (X,Y):
    return X+Y
numbers = [1,2,3,4,5]
sum_numbers = reduce(add,numbers)
print(sum_numbers)
 