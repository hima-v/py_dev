for i in range(int(input())):
    n=int(input())
    ar=list(map(int,input().split()))
    m=min([i for i in ar if i>0],default=0)
    ans=m-1
    print(ans)
    # if(nans>min(ar)):
    #     print(ans)
    # else:
    #     print(-1)
