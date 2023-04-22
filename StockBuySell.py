def stockBuySell(A, n):
    if n==1:
        return []
    i=0
    lis=[]
    while i<n-1:
        if A[i]<A[i+1]:
            lis.append((i,i+1))
        i+=1
    return lis

A=list(map(int,input().split()))
n=len(A)
ans=stockBuySell(A,n)
print(ans)