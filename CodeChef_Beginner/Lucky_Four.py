n=int(input())
l=[]
for i in range (n):
    l.append(int(input()))
for num in l:
    k=0
    p=""
    p=str(num)
    length=len(p)
    for j in range(0,length):
        if(p[j]=='4'):
            k+=1
    print(k)
