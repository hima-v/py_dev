
for _ in range(int(input())):
    input()
    s = input()
    while len(s) != 0 and s[0] != s[-1]:
        s = s[1:-1]
    print(len(s))