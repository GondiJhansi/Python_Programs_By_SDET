l=[23,65,19,90]
print(l)
p1,p2=1,3
f=l.pop(p1)
s=l.pop(p2-1)
l.insert(p1,s)
l.insert(p2,f)
print(l)
