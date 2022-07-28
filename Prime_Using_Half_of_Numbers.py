def IsPrime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True
n=int(input())
if IsPrime(n):
    print(n," is a Prime Number")
else:
    print(n," is not a Prime Number")
