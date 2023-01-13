# cook your dish here
# cook your dish here
t = int(input())
while(t>0):
    l,b = map(int, input().split())
    for i in range(min(l,b) , 0, -1):
        print(i)
        if(l%i == 0 and b%i == 0):
            s = i
            break
    print(int((l*b)/(s*s)))
    t -= 1
    print(s)