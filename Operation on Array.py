#Adding Elements 
import array
numbers = array.array('i',[1,2,3])
numbers.append(4)
print(numbers)

#Insert at specific index
numbers.insert(1,10)
print(numbers)


#Removing Elements
numbers.remove(10)
print(numbers)