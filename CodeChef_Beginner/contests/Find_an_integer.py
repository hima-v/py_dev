def awsm(x,y):
    f=x*y
    mult=[]
    minr=abs(x-y)
    for i in range(f,minr,-1):
        if(f%i==0):
            mult.append(i)
    for nums in mult:
        val=nums-x-y
        print(val)
        if((val+x)%y==0 and (val+y)%x==0):
            return(val)
for i in range(int(input())):
    x,y=map(int,input().split())
    print(awsm(x,y))