units=int(input("Enter the number of electricity units consumed:"))
if units<=100:
    bill= units*5
elif units<=200:
    bill =(100*5) + (100*7) +(units- 200)*10
    print("Total Electricity Bill:rupees",bill)

          
