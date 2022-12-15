#input the number of test cases. then reverse them and print

t = int(input())
reverse=0
n=[]
num=0
for i in range(t):
    el=int(input())
    n.append(el)
for num in n:
    l=len(str(num))
    for k in range(0,l):
        x=num%10
        reverse=reverse*10 + x
        num=int(num/10)
    print(reverse)
    reverse=0
