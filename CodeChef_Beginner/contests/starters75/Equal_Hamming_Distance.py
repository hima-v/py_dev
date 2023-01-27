def hamming():
    N=int(input())
    A=int(input())
    B=int(input())
    xo=A^B
    d=str(xo).count('1')
    while d!=1:
        if(d==0):
            return(2**N)
        else:
            po=N-d+1
            return(2**po)
    return(-1)
for i in range(int(input())):
    print(hamming())
