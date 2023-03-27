for i in range(int(input())):
    k=0
    x=0
    y=0
    s=int(input())
    moves=str(input())
    for j in range(s):
        if(moves[j]=='U'):
            y+=1
        elif(moves[j]=='D'):
            y-=1
        elif(moves[j]=='R'):
            x+=1
        else:
            x-=1
        if(x==1 and y==1):
            k=1
            break
    if(k==1):
        print("YES")
    else:
        print("NO")
