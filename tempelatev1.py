#t: number of test cases
#a,b pair values
#l1 list of size len_l1

# taking input for number of test cases
def inp():
    t=int(input())
    return t

#taking input for two pair spaced input
def mapp():
    a,b=map(int,input().split())
    return a,b

#taking input for user defined size of list size n length
def fixed_list():
    n=int(input())
    l1=list(int(num) for num in input().split())[:n]
    return n,l1

#taking input via each line. appending in the list
def app_list(t):
    l2=[]
    for i in range (t):
        val=int(input())
        l2.append(val)
    return l2

t=inp()
a,b=mapp()
len_l1,l1=fixed_list()
l2=app_list(t)