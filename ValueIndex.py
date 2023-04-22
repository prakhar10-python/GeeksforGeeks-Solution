A=list(map(int,input().split()))
ans=[]
for i in range(len(A)):
    if(i+1==A[i]):
        ans.append(A[i])
print(ans)