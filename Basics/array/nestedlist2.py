# take the second element for sort
def take_second(elem):
    return elem[1]
n=int(input())
nl,nm,sc=[],[],[]
for i in range (n):
    nm.append(input())
    sc.append(float(input()))
    val=[nm[i],sc[i]]
    nl.append(val)
b=sorted(nl,key=take_second)
scores=sorted(sc)
maxi=scores[0]
k=0
for i in range (1,n):
    if(scores[i]==maxi):
        break
    if (scores[i]<maxi):
        k=i
        break
valu=b[k][1]

newn=[]
for i in range (0,n):
    if(b[i][1]==valu):
        newn.append(b[i][0])
print(newn.sort())
