for i in range(int(input())):
    a=list(map(int,input().split()))
    t1=a[::2]    #slice operator[start,stop,step]
    t2=a[1::2]
    k =1
    if sum(t1)>sum(t2):
        print(1)
    elif sum(t1)<sum(t2):
        print(2)
    else :
        print(0)


