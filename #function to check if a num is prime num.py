#function to check if a num is prime number
def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
        return True
    #collect all prime num between 100 and 500
    primes=[]
    for n in range (100,500):
        if is_prime(n):
            primes.append(n)
  #print the sum of two prime numbers
    print("prime numbers between 100 and 500")
    print(primes)
    print("\nsumtwo prime numbers")
    for i in range(len (primes)):
        for j in range (i+1,len (primes)):
            print(primes[i],"+",primes[j],"=",primes[i] + primes[j])
        
                   
 

                
