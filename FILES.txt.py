f = open("data.txt","w")
f.write("Hello,python!\n")
f.close()


f = open ("data.txt","r")
print(f.read()) #reads entire file
print(f.read(5)) #reads first 5 characters
f.close

f = open("data.txt","r")
print(f.readline()) #first line
print(f.readline()) #second line
f.close()

f = open("data.txt","r")
print(f.read(5)) #reads first 5 characters
print("pointer at:",f.tell()) #shows postion
f.seek(0) #moves pointer to beginning
print(f.read(5))   #reads again from start
f.close()


