n=int(input())
seq=list(map(int,input().split()))
mi=min(seq)
ma=max(seq)
for j in range(0,n):
    if(seq[j]==mi):
        miind=j
maind=seq.index(ma)
t=n+maind-miind-1
if(miind<maind):
    t-=1
if(mi==ma):
    t=0
print(t)

