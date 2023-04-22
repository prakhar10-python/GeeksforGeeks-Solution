arr=list(map(int,input().split()))
x=int(input())
x_first_index=arr.index(x)
arr=arr[::-1]
x_last_index=arr.index(x)
print(x_first_index,x_last_index)