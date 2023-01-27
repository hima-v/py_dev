for i in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    pos=0
    for j in range(1,n):
        if(x[j]>x[pos]):
            pos=j
        elif(x[pos]==x[j] and y[j]>y[pos]):
            pos=j
    print(pos+1)
