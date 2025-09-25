#Global Variable
X=100
def function():
#local variable
 Y=50
 print("Inside function,X=",X) #Access
 print("Inside function,Y=",Y)  #Access local
function()
print("outside function,X=",X) #Accessible#
print(Y)
