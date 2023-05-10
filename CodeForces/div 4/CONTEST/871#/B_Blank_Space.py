for i in range (int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=0
    ans=[]
    for num in a:
        if num==0:
            k+=1
            ans.append(k)
        else:
            k=0
    ans.append(0)
    print(max(ans))
