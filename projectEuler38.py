import sys


def checkIfPandigital(numStr, K):
    if len(tempStr) != K:
        return False
    if "0" in numStr:
        return False
    for m in range(1, K+1):
        if str(m) not in numStr:
            return False
    if K != 9:
        if "9" in numStr:
            return False
    return True


if __name__ == "__main__":
    input = str.split(sys.stdin.readline())
    N = int(input[0])
    K = int(input[1])

    for mult in range(2, N):
        tempStr = ""
        for i in range(1, 9):
            tempStr += str(mult * i)
            if (checkIfPandigital(tempStr, K)):
                print(mult)
                break
