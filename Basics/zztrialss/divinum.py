def factors(x):
    l=[]
    for i in range(x,1,-1):
       if x % i == 0:
          l.append(i)
    return(l)
print(factors(756))