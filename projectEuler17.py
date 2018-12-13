import sys
import math

# 1 000 000 000 000 = one trillion
# 1 000 000 000     = one billion
# 1 000 000         = one million
# 1000              = one thousand
# 100               = one hundred

numbers = dict()
zeros = dict()

numbers[1] = "One"
numbers[2] = "Two"
numbers[3] = "Three"
numbers[4] = "Four"
numbers[5] = "Five"
numbers[6] = "Six"
numbers[7] = "Seven"
numbers[8] = "Eight"
numbers[9] = "Nine"
numbers[10] = "Ten"
numbers[11] = "Eleven"
numbers[12] = "Twelve"
numbers[13] = "Thirteen"
numbers[14] = "Fourteen"
numbers[15] = "Fifteen"
numbers[16] = "Sixteen"
numbers[17] = "Seventeen"
numbers[18] = "Eighteen"
numbers[19] = "Nineteen"
numbers[20] = "Twenty"
numbers[30] = "Thirty"
numbers[40] = "Forty"
numbers[50] = "Fifty"
numbers[60] = "Sixty"
numbers[70] = "Seventy"
numbers[80] = "Eighty"
numbers[90] = "Ninety"

zeros[1] = ""
zeros[2] = "Thousand"
zeros[3] = "Million"
zeros[4] = "Billion"
zeros[5] = "Trillion"


def numToWords(n):
    resultStr = ""
    z = 0

    while n != 0:
        z += 1
        hundred = n % 1000
        resultTmp = []

        if hundred > 99:
            resultTmp.append(numbers[int(hundred / 100)])
            resultTmp.append("Hundred")

        remainder = n % 100
        n = int(n / 1000)

        if remainder > 0:
            if remainder <= 20:
                resultTmp.append(numbers[remainder])
            else:
                resultTmp.append(numbers[int(remainder / 10) * 10])
                if remainder % 10 != 0:
                    resultTmp.append(numbers[remainder % 10])

        if hundred > 99 or remainder > 0:
            resultTmp.append(zeros[z])
        if len(resultTmp) > 0:
            resultStr = " ".join(resultTmp) + " " + resultStr

    print(resultStr)


if __name__ == "__main__":
    # numToWords(160000)

    firstLine = True
    for line in sys.stdin:
        s = int(line.strip())
        if not firstLine:
            if s != 0:
                numToWords(s)
            else:
                print("Zero")

        firstLine = False
