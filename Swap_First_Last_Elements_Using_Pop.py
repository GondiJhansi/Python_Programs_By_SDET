l=[12,35,9,56,24]
first=l.pop(0)
last=l.pop(-1)
l.insert(0,last)
l.append(first)
print(l)
