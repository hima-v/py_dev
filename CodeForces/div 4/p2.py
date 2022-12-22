t=int(input())
for i in range(t):
    n=int(input())
    a = list(int(num) for num in input().strip().split())[:n]
    b=sorted(a)
    v=0
    k=1
    j=0
    for j in range(n):
        while(k!=n):
            if(b[j]==b[k]):
                v=1
            k+=1    
    if(v==1):
        print("NO")
    else:
        print("YES") 