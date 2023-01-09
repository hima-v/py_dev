for i in range(int(input())):
    l=list(map(int,input().split()))
    if(min(l[0]//l[2],l[1]//l[3])>=l[4]):
        print("YES")
    else:
        print("NO")