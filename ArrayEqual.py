A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()
for i in range(len(A)):
    if A[i]!=B[i]:
        print( False)
        break
print(True)