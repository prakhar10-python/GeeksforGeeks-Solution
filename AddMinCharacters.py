# without KMP
# prakhargfg0923@gmail.com Asdfasdf8
s1=input()
s1_copy=s1
ans=0
for i in range(len(s1_copy)):
    if(s1_copy==s1_copy[::-1]):
        ans=(len(s1)-len(s1_copy))
    else:
        s1_copy=s1_copy[:-1]
print(ans)

