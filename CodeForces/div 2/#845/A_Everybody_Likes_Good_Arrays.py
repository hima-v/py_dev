for i in range(int(input())):
    n=int(input())
    ev,od=0,0
    l=list(map(int,input().split()))
    barr=[0]*n
    for x in range(0,n):
        if(l[x]%2==1):
            barr[x]=1
    barrl=n
    k=0
    for j in range(0,n-1):
        if(barr[j]==barr[j+1]):
            k+=1
    print(k)
