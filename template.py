import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    # 1 2 3 -> [1, 2, 3]
    return(list(map(int,input().split())))
def insr():
    # abc -> ["a", "b", "c"]
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

# Definitions

def output_list(l):
    print(" ".join(list(map(str, l))))

class Node:
    def __init__(self, i, next):
        self.i = i
        self.next = next
    def __str__(self):
        return str(self.i)


def test_case():
    s = "".join(insr())

    yes_n = "".join(["Yes" for i in range(int(len(s)))])
    #print(s, yes_n)
    if s in yes_n:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    n_cases = inp()

    for i in range(n_cases):
        test_case()
