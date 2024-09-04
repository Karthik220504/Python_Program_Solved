di = ["N","S","E","W","Ne","Se","Sw","Nw"]
dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, 1, -1 ,1 ,1, -1, -1]


def valid(r,c,n,ma):
  return (r>=0 and r<n) and (c>=0 and c<n) and (ma[r][c] == 1)


def fp(r,c,ma,n,res,cr):
  
  if r == n-1 and c == n-1:
    res.append(cr)
    return
  ma[r][c] = 0
  
  for i in range(8):
    n_r = r+dr[i]
    n_c = c+dc[i]
    
    if valid(n_r,n_c,n,ma):
      cr += di[i]
      fp(n_r,n_c,ma,n,res,cr)
      cr = cr[::-1]
  
  ma[r][c] = 1 

q = []
np = int(input())

for i in range(np):
  ee = list(map(int,input().split()))
  q.append(ee)

res = []
cr = ""

if(q[0][0] != 0 and q[np-1][np-1] != 0):
  fp(0,0,q,np,res,cr)

if not res:
  print(-1)
else:
  print(res)
