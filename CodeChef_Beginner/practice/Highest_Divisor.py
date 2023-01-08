n=int(input())
div=1
for i in range(2,11):
    if(n%i==0):
        div=i
print(div)