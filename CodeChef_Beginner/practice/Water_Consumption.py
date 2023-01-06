t=int(input())
x=[]
for i in range (t):
    x.append(int(input()))
for quant in x:
    if(quant<2000):
        print("NO")
    else:
        print("YES")