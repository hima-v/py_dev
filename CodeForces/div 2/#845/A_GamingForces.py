import math
for i in range(int(input())):
    n=int(input())
    h=list(map(int,input().split()))
    amin=math.ceil(sum(h)/2)
    if(amin>n):
        print(n)
    else:
        print(amin)