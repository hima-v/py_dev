p=str(314159265358979323846264338327)
for i in range(int(input())):
    k=0
    n=str(input())
    l=len(n)
    for j in range(0,l):
        if(n[j]==p[j]):
            k+=1
        elif(n[j]!=p[j]):
            break
    print(k)