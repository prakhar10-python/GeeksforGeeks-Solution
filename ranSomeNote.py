ransomNote=input()
magazine=input()
ransomNote_set=set(ransomNote)
magazine_set=set(magazine)
if(ransomNote_set.issubset(magazine_set)):
    dict1={}
    for i in ransomNote_set:
        val=ransomNote.count(i)
        dict1[i]=val
    dict2={}
    for i in magazine_set:
        val=magazine.count(i)
        dict2[i]=val
    flag=True
    for i in dict1:
        if(dict2[i]>=dict1[i]):
            flag=True
            continue
        else:
            flag=False
            break
    print(flag)
else:
    print(False)