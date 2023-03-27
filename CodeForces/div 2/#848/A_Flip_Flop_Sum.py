for i in range (int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    i=0
    h=0
    s=sum(ar)
    for i in range(0,n-1):
        if(ar[i]==ar[i+1]==-1):
            h=1
            break
    c=ar.count(1)
    if c==n:
        print(s-4)
    elif h==1:
        print(s+4)
    else:
        print(s)