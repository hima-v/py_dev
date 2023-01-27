def mood(a):
    t1=a[0]
    am=t1
    bm=t1
    return(am,bm)
def jokscalci(joks):
    a=joks
    almood,bmood=mood(joks)
    t1=a[0]
    t2=min(t1,a[1])  #to know maximum jokes of type 2 without going below 0
    t3=min(t1,a[2])  #to know maximum jokes of type 3 
    almood-=t3       #get almood-type3 
    a[2]=a[2]-t3     #type3 jokes reduced
    joks+=t3         
    bmood-=t2
    a[1]=a[1]-t2
    joks+=t2
    if (almood>0 and bmood>0):
        joks=joks+min(bmood-a[1],almood-a[2],almood-a[3],bmood-a[3])
    else:
        return(joks+)
for i in range(int(input())):
    joks=list(map(int,input().split()))
    print(jokscalci(joks))