t=int(input())
for i in range (t):
    l=list(map(int,input().split()))
    if(l[1]>=l[0] and l[3]>=l[2] and l[5]<=l[4]):
        print("YES")
    else:
        print("NO")