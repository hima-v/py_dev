for i in range(int(input())):
    l=int(input())
    st=input()
    rev=st[::-1]
    c=l%2
    j=0
    k=0
    if(c==0):
        for j in range (int(l/2)):
            if(int(st[j])^(int(rev[j]==1))):
                k+=1
            else:
                break
    elif(c==1):
        for j in range(l//2):
            if(int(st[j])^(int(rev[j]==1))):
                k+=1
            else:
                break
    print(k)
    print(l-k*2)
