for number in range(1,4):
    if number==2:
        pass #Do nothing when number is 2
    print("Number:",number)
    
    

#Create a integer array import array
import array
numbers = array.array('i',[1,2,3,4,5])
print(numbers)


#Create Float Array
import array
float = array.array('f',[1.1,2.2,3.3])
print(float)
 

 # Accessing Elements (indexing)
import array
number = array.array('i',[10,20,30,40])
print(number[0])
print(number[2])

#Slicing Arrays
import array
number = array.array('i',[10,20,30,40,50])
print(number[1:4])
print(number[::-1])

