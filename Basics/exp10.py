def inp():
    npr=int(input("Enter no of production rules"))
    # S=input("Enter rule Start Rule")[3:]
    # pr["ruleno_"+str(i)] = list(map(str,input().split(">"))
    pr={}
    for i in range(npr):
        var,ru=input().split("->")
        pr[var]=ru
