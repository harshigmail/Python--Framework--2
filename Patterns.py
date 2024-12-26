# simple pyramid pattern
def pattern1(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for h in range(0, i + 1):
            print("*", end=" ")
        print("\r")


pattern1(4)


def pattern2(n):
    for i in range(0, n):
        for h in range(0, i + 1):
            print("*", end=" ")
        print("\r")


pattern2(4)


# inverse pyramid
def pattern4(n):
    for i in range(n, n - 1):
        for h in range(0, i - 1):
            print("*")
        print("\r")


pattern4(4)
