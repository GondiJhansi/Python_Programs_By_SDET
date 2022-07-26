num=int(input("Enter a Number:"))
c=0
if num>1:
    for i in range(1,num+1):
        if num%i==0:
            c+=1
    if c==2:
        print(num," is a Prime Number")
    else:
        print(num," is not a Prime Number")
