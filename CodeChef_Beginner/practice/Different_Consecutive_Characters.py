def getopval(string,le):
    k=0
    i=0
    for i in range (0,le-1):
        if(string[i]==string[i+1]):
            k+=1
    return(k)
t=int(input())
x=[]
for j in range (0,t):
    l=int(input())
    s=str(input())
    x.append(getopval(s,l))
for val in x:
    print(val)