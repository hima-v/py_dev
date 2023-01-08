t=int(input())
for i in range(t):
    z,y,a,b,c=map(int,input().split())
    if(z-y>=a+b+c):
        print("YES")
    else:
        print("NO")