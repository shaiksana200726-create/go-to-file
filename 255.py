print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")

        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")

        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")

        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero is not allowed.")
else:
        print("Invalid input")





marks= int(input("enter marks"))
if marks>90:
     print("Grade A")
elif marks>80:
     print("Grade B")
elif marks>70:
     print("Grade C")
elif marks>60:
     print("Grade D")
else:
     print("fail")               



num=int(input("Enter a number"))
if num%2==0:
     print("even")
else:
     print("Odd")     
        



