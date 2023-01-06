x = list(map(int, input("Enter numbers ").split()))
l=x[0]
d=x[1]
k=0
tlen=len(x)
if(tlen==l+2):
    for i in range(2,l+1):
        if(x[i]%d==0):
            k+=1
print(k)

#error: cannot handle index out of range questions.
#target is to take input only once but make sure that the length of tuple is apt? tf