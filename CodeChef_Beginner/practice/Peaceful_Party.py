t=int(input())
for i in range (t):
    l=list(map(int,input().split()))
    print(max(l[0]+l[2],l[1]))