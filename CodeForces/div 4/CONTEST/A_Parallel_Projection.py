for i in range (int(input())):
    w,d,h=map(int,input().split())
    a,b,f,g=map(int,input().split())
    x=(min(abs(d-g),g)+h+abs(a-f)+b)
    print(x)