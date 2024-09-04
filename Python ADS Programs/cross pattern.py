a = input()

for i in range(len(a)-1):
    for j in range(len(a)):
        if(i != j and i != (len(a)-j-1)):
            print(" ",end=" ")
        else:
            print(a[j],end="")
            
    print()
