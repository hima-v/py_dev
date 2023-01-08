for t in range(int(input())):
    n = int(input())
    print("NO" if (n%7)%2 != 0 and n < 7 else "YES")