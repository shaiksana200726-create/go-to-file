#check if an Elements Exits
fruits = ['apple','banana','mango']

if 'grapes' in fruits:
    print("Grapes are in the list")
else:
    print("Grapes are not in the list")

 
    fruits = ('apple','banana','mango','grapes','orange')
print(fruits[0])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])

#Slicing
fruits = ('apple','banana','mango','grapes','orange')
#slice from index 1 to 3 (does not include)
print(fruits[1:3])
#slice from beginning up to index 3
print(fruits[:3])
#slice from index 2 to end
print(fruits[2:])
#step slicing : every second element
print(fruits[::2])

#Reverse tuple
print(fruits[::-1])