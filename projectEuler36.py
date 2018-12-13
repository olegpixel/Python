import sys

def checkIfPalindromic(num):
    strNum = str(num)
    rev = strNum[::-1]
    if rev == strNum:
        return True
    else:
        return False

def checkInAnotherBase(num, base):
    t = num
    numbs = ""
    while t > 0:
        numbs += str(int(t % base))
        t -= t % base
        t /= base

    if numbs == numbs[::-1]:
        return True
    else:
        return False




if __name__ == "__main__":
    input = str.split(sys.stdin.readline())
    N = int(input[0])
    K = int(input[1])
    sum = 0

    for i in range(1, N):
        if (checkIfPalindromic(i)):
            # print("in 10 = ", i)
            if (checkInAnotherBase(i, K)):
                sum += i

    print(sum)