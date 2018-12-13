import sys

def toFactorialRepresentation(num):
    result = []
    quotient = 0
    while num > 0:
        quotient += 1
        result.append(int(num % quotient))
        num = int(num / quotient)
    return result


if __name__ == "__main__":
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m']

    firstLine = True
    for line in sys.stdin:
        s = int(line.strip()) - 1
        if not firstLine:
            tempArr = toFactorialRepresentation(s)
            for i in range(0, 13 - len(tempArr)):
                tempArr.append(0)
            tempArr = list(reversed(tempArr))

            nth = ""
            tempLetters = letters.copy()
            for i in tempArr:
                nth += tempLetters[i]
                tempLetters.pop(i)
            print(nth)

        firstLine = False

