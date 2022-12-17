#find occurences of digit 4 in number
t = int(input())
for i in range(t):
    k=0
    n=int(input())
    l=len(str(n))
    p=str(n)
    for j in range(l):
        if(p[j]=='4'):
            k+=1
        n/10
        p=str(n)
    print(k)