def function_name():
# code black
  print("Hello,world!")

def greet():
  print("Welcome to python functions!")
greet()

def greet_user(name):
    print("Hello",name)
    #calling function with argument
greet_user("hero")
    
def add(a,b):
      print("sum is:",a+b)
add(5,10)

def introduce (name,age):
    print(f"my name is {name} and i am {age} years old.")
introduce(age =29,name = "hero")

def greet (name = "Guest"):
    print("Hello",name)
greet()
greet("ram")