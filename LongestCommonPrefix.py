s=["flower","flight","flow"]
s.sort()
# print(s)
end_of_searching=min(len(s[0]),len(s[len(s)-1]))
i=0
while(i<end_of_searching):
    if(s[0][i]==s[len(s)-1][i]):
        i+=1
    else:
        break
ans=s[len(s)-1]
print(s[len(s)-1][:i])