for i in range(int(input())):
    n=int(input())
    v=0
    ar=list(map(int,input().split()))
    odd=(ar.count(0)%2)
    even=(ar.count(1)%2)
    if(odd+even!=0):
        v=1
    else:
        v=0
    if(n%2==v):
        print("YES")
    else:
        print("NO")