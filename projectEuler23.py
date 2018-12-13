import sys
import math

abundantNumbers = []


def checkIfAbundant(num):
    dividers = dict()
    saveNum = num
    for j in range(2, int(math.sqrt(saveNum)) + 2):
        while num % j == 0:
            num = num / j
            if j in dividers:
                dividers[j] += 1
            else:
                dividers[j] = 1
    divSum = 1

    for key, value in dividers.items():
        divSum *= ((key ** (value + 1)) - 1) / (key - 1)
    if (divSum - saveNum) > saveNum:
        abundantNumbers.append(saveNum)


if __name__ == "__main__":

    for i in range(12, 28123):
        checkIfAbundant(i)

    # print(abundantNumbers)

    firstLine = True
    for line in sys.stdin:
        s = int(line.strip())
        if not firstLine:
            if (s < 957 and s % 2 != 0):
                print("NO")
            elif s > 28123:
                print("YES")
            else:
                resultStr = "NO"
                for m in range(0, len(abundantNumbers)):
                    if ((int(s) - abundantNumbers[m]) in abundantNumbers):
                        resultStr = "YES"
                print(resultStr)

        firstLine = False
