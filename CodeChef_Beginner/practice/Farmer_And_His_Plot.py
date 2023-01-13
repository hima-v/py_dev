for i in range(int(input())):
    l,b=map(int,input().split())
    k=1
    for j in range (min(l,b),0,-1):
        if(l%j==0 and b%j==0):
            k=j
            break
    print((l*b)//(k*k))
