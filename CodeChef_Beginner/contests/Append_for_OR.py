from functools import reduce
def appor(lenar,bval,arr):
    b_or=reduce(lambda x,y:x|y, arr)
    ans=bval-b_or
    if(bval==(ans|b_or)):
        return(ans)
    else:
        for j in range (ans,bval):
            ans2=ans+1
            if(b_or|ans2==bval):
                return(ans2)
        return(-1)
for i in range(int(input())):
    n,y=map(int,input().split())
    ar=list(map(int,input().split()))
    print(appor(n,y,ar))

#     from functools import reduce
# def appor(lenar,bval,arr):
#     b_or=reduce(lambda x,y:x|y, arr)
#     ans=bval-b_or
#     if(bval==(ans|b_or)):
#         return(ans)
#     else:
#         return(-1)
# for i in range(int(input())):
#     n,y=map(int,input().split())
#     ar=list(map(int,input().split()))
#     print(appor(n,y,ar))