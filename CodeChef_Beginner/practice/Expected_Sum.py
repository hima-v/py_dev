import random 
def chit(ones,zeroes):
    f=0
    while (ones!=0):
        k=random.randint(0,1)
        if(k==0):
            zeroes-=1
        else:
            f+=1
            ones-=1
    print(f)
    return(f)
t=int(input())
for i in range(t):
    a,b=map(int,input().split()) #a=1s b=0s
    f=chit(a,b)
    ev= (1/(a+b))
    #ev=(f*(1/a+b))
    print(ev)
    
