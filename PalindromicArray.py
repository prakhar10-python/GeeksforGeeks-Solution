arr=list(map(int,input().split()))
flag=True
for i in range(len(arr)):
    if(str(arr[i])==str(arr[i])[::-1]):
        flag=True
        continue
    else:
        flag=False
        break
print(flag)