def factorial(a):
    return 1 if (a==0 or a==1) else a*factorial(a-1)
f=int(input())
print("Factorial of ",f,"is ",factorial(f))

