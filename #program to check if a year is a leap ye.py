#program to check if a year is a leap year
year=int(input("Enter a year:"))
#leap year condition
#1.year should be divisible by 4
#2.but not divisible by 100
#3.unless it is divisible by 400
if(year %400==0)or (year %4==0 and year % 100!=1):
  print(year, "is a leap year.")
else:
  print(year, "is a  not leap year.")