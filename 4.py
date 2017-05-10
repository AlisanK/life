def count_neighbours(A,i,j):
    count=0
    if A[i-1][j-1]==1:
        count+=1
    if A[i][j-1]==1:
        count+=1
    if A[i-1][j]==1:
        count+=1
    if A[i+1][j+1]==1:
        count+=1
    if A[i+1][j]==1:
        count+=1
    if A[i][j+1]==1:
        count+=1
    if A[i-1][j+1]==1:
        count+=1
    if A[i+1][j-1]==1:
        count+=1
    return count

def check_exit(states,n,m):
    flag=0
    zero=[[0]*n for i in range(m)]
    if states[-1]==zero:
        print('zero')
        flag=1
    for i in range(len(states)-1):
        if states[i]==states[-1]:
            flag=1
            print('the same')
            break
    return flag

f=open('field.txt','r')
r=f.readlines()
m=len(r[0].rstrip())
n=len(r)
current=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        current[i][j]=int(r[i][j].rstrip())
next=[[0]*m for i in range(n)]
for k in range(n):
    print(*current[k])
print()
states=[]
states.append(current)

while 1:
    for i in range(-1,n-1):
        for j in range(-1,m-1):
            c=count_neighbours(current,i,j)
            if current[i][j]==1:
                if not(c==2 or c==3):
                    next[i][j]=0
                else:
                    next[i][j]=1
            elif current[i][j]==0:
                if c==3:
                    next[i][j]=1
                else:
                    next[i][j]=0
    states.append(next)
    current=next
    next=[[0]*m for i in range(n)]
    for k in range(n):
        print(*current[k])
    if check_exit(states,n,m)==1:
        break

    print()