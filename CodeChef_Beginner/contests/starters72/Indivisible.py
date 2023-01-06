def com(l):
    i=1
    for i in range (1,100):
        if(l[0]%i!=0 and l[1]%i!=0 and l[2]%i!=0):
            return(i)
t=int(input())
for j in range (t):
    linp=list(map(int,input().split()))
    print(com(linp))