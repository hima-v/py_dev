def inp():
    t=int(input())
    return t
#taking input for two pair spaced input
def mapp():
    a,b=map(int,input().split())
    return a,b
t=inp()
for h in range(t):
    k,n=mapp()
    arr_range=list(range(1,n+1))
    print(arr_range[:k])