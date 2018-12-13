import sys


def transform(x):
    return {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }[x]


def toDec(str):
    result = 0
    for i in range(0, len(str)):
        result += transform(str[i])
    return result


def toRoman(number):
    temp = number
    str = ""

    while temp >= 1000:
        str += "M"
        temp -= 1000

    if temp >= 900:
        str += "CM"
        temp -= 900

    while temp >= 500:
        str += "D"
        temp -= 500

    if temp >= 400:
        str += "CD"
        temp -= 400

    while temp >= 100:
        str += "C"
        temp -= 100

    if temp >= 90:
        str += "XC"
        temp -= 90

    while temp >= 50:
        str += "L"
        temp -= 50

    if temp >= 40:
        str += "XL"
        temp -= 40

    while temp >= 10:
        str += "X"
        temp -= 10

    if temp == 9:
        str += "IX"
        temp -= 9

    while temp >= 5:
        str += "V"
        temp -= 5

    if temp == 4:
        str += "IV"
        temp -= 4

    while temp > 0:
        str += "I"
        temp -= 1

    return str


if __name__ == "__main__":

    firstLine = True
    for line in sys.stdin:
        s = str(line.strip())
        if not firstLine:
            print(toRoman(toDec(s)))
        firstLine = False
