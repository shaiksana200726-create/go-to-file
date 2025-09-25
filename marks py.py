marks=int(input("Enter a marks"))

if marks<35:
    print("Fail")

elif marks>80:
    print("Pass")

if marks in range(35,59):
    print("First Class")


if marks in range(60,80):
    print("Distinction")
