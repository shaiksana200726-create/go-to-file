def mul(a,b):
    print("mul is:",a*b)
mul(6,5)

n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
def mul_number(a,b):
 return a*b
result = mul_number(n1,n2)
print(result)

n = int(input("Enter number"))
def is_even(num):
 if num%2==0:
      print("Even")
 else:
      print("odd")
is_even(n)

n1 = int(input("Enter a number"))
def   factorial(n):
    result =1
    for i in range(1,n+1):
     result*=i            
    return result                                                                                                                 
print(factorial(n1))

n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
n3 = int(input("Enter third number"))
def largest_of_three(a,b,c):
 
 if a>=b and a>=c:
  return a 
 elif b>=a and b>=c:
  return b 
 else:
   return c 
   print(largest_of_these(n1,n2,n3))
   
str = input("enter string")
def reverse_string (s):
 return s[::1]
print(reverse_string(str))

def count_vowels(word):
     vowels ="aeiouAEIOU" 
     count = 0
     for char in word :
          if char in vowels:
             count+=1
             return count 
     print(count_vowels("Programming"))


     