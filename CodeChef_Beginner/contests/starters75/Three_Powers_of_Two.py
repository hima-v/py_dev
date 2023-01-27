for i in range(int(input())):
    N=int(input())
    S=str(input())
    c=S.count('1')
    if(c>3):
        print("NO")
    elif(c<=3 and int(S)>10):
        print("YES")
    else:
        print("NO")