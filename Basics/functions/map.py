def evenodd(num):
    if(num%2==0):
        print("the number {} is even".format(num))
    else:
        print("The number {} is odd.".format(num))
l1=[1,2,4,7,8]
list(map(evenodd,l1))
print(l1)
x, y = [int(x) for x in input().split()]