def factors(x):
    fact=[]
    for i in range(1, x + 1):
        if x % i == 0:
            fact.append(i)
    ll=len(fact)
    if ll<3:
        return([-1])
    else:
        ans=[fact[0],fact[1],fact[ll-2]]
        return(ans)
t=int(input())
for j in range (t):
    n=int(input())
    a=factors(n)
    print(*a)