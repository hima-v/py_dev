num=1234
base=5
ans=[]
while(num!=0):
    r=num%base
    ans.append(r)
    num=int(num/base)
print(ans)