a = input()
b =input()

a = [i for i in a]
b = [j for j in b]

pre = 0
c = 0

a = a[::-1]
b = b[::-1]

ma = 0
j = 0
for i in range(len(a)):
    ind = 0
    if a[j] in b:
        ind = b.index(a[j])
        if (ind>=pre):
            pre = ind
            c+=1
            ma = c
            
        else:
            j -=2
            ma = c
            pre = 0
            c=0
    j+=1
    

print(ma)
