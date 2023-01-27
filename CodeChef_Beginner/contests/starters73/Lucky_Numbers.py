def luckynu(n):
    while(n!=0):
        if(n%10==7):
            return("YES")
        n=n//10
    return("NO")
for i in range(int(input())):
    print(luckynu(int(input())))