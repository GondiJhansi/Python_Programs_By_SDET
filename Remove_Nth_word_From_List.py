l=['geeks','for','geeks','for','geeks']
s=input()
n=int(input())
c=0
for i in range(0,len(l)-1):
    if l[i]==s:
        c+=1
        if c==n:
            del l[i]
print(l)
