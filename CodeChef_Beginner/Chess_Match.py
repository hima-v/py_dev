# t=int(input())
# x=[]
# for i in range (t):
#     l=list(map(int,input().split()))
#     time=((2*(180+l[0]))-(l[1]+l[2]))
#     x.append(time)
# for num in x:
#     print(num)

for _ in range(int(input())):
    N, A, B = list(map(int, input().split(' ')))
    out1 = (180 + N)*2
    print(out1 - A - B)