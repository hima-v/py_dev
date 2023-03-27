for i in range(int(input())):
    n=int(input())
    s=str(input())
    alset=set(s)
    alph=list(alset)
    ans=[]
    for j in range (n):
        le=s[0:j]
        ri=s[j:n]
        o=len(list(set(le)))
        ne=len(list(set(ri)))
        ans.append(o+ne)
    print(max(ans))
