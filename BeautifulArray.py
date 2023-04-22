arr=list(map(int,input().split()))
ans=[]
for i in range(len(arr)):
    if(len(ans)==0):
        ans.append(arr[i])
    else:
        if(ans[-1]>=0 and arr[i]<0) or (ans[-1]<0 and arr[i]>0):
            print("diff",ans[-1])
            ans.pop()
        else:
            ans.append(arr[i])
            print("Step",ans[-1])
print(ans)