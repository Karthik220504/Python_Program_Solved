a = input("Enter 1:")
b = input("Enter 2:")
c= []

q = 0
w = 0
for i in range(len(a)):
    if(len(b) <= w):
        c.append(a[q])
    elif(a[q] != b[w]):
        c.append(a[q])
        q+=1
    else:
        q+=1
        w+=1
print(*c)
