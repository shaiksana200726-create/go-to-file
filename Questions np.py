#1Q
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
#arthemetic operations
Add = n1+n2
sub = n1-n2
mul =  n1*n2
Divd = n1/n2
mod = n1%n2
exponent = n1**n2
# print the results
result= (f"Add:{Add}")
print(result)
result= (f"sub:{sub}")
print(result)
result = (f"mul:{mul}")
print(result)
result =  (f"mod:{mod}")
print(result)
result = (f"exponent:{exponent}")
print(result)

#3Q
num1 = float(input("Enter a first number"))
num2 = float(input("Enetr a second number"))
if num1==num2:
    print(f"the numbers{num1}={num2}")
else:
    print("num1 and num2 are not equal")

array = [1,2,3,4,5,6,7]
reverse_array = (7,6,5,4,3,2,1,)
reversed_array= reverse_array(array)
print(f"original array:[1,2,3,4,5,6,7]")
print(f"Reversed array:{reversed_array}")