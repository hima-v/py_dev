def fn(n,l):
    l.sort()
    typeset=(set(l))
    typecount = len(set(l))
    if(n%2==0):

    
t=int(input())
for i in range (t):
    num=int(input())
    l_ani=list(map(int,input().split()))
    print(fn(num,l_ani))
