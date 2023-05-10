n=5
k=0
h=0
for i in range (0,n-1):
    h+=1
    print("i value for this iteration is",i)
    #print("times of i operation",h)
    for j in range(0,i-1):
        k+=1
        print("j value for this operation",j)
        print("i value for this operation",i)
        #print("times of j operation",k)