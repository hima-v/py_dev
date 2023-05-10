for i in range (int(input())):
    s= str(input())
    k=0
    st='codeforces'
    for ch in s:
        if ch!=st[:1]:
            k+=1
        st=st[1:]
    print(k)