def ar(arr):
    are(0,len(arr)-1,arr)
    
def are(i,j,arr):
    if(j<i):
        return
    mid = (i+j)//2
    print(arr[mid],end=" ")
    are(i,mid-1,arr)
    are(mid+1,j,arr)
    
    
    

arr = list(map(int,input().split()))
ar(arr)

