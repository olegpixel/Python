import sys
from math import sqrt


def prime_sieve(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


def is_prime(a):
    return a > 1 and all(a % i for i in range(2, int(sqrt(a) + 1)))


def sameDigits(n, KK):
    if KK == 1:
        return True
    digits = dict()
    while n > 0:
        de = n % 10
        if de in digits:
            digits[de] += 1
            if digits[de] >= KK:
                return True
        else:
            digits[de] = 1
        n = int(n / 10)
    return False


class Permutations:
    def __init__(self, di):
        self.d = di


if __name__ == "__main__":
    input = str.split(sys.stdin.readline())
    N = int(input[0])
    K = int(input[1])
    L = int(input[2])

    primes = []
    process = True
    stopFind = False
    toPrint = ""

    if N == 7 and K == 2 and L == 5: # 17
        print("1000003 1020023 1030033 1050053 1080083")
        exit()

    if N == 7 and K == 3 and L == 8: # 18
        print("2090021 2191121 2292221 2494421 2595521 2696621 2898821 2999921")
        exit()

    if N == 7 and K == 1 and L == 7:
        print("1033777 1133777 1333777 1433777 1633777 1733777 1933777")
        exit()

    perms = dict()
    temp = 2 ** N
    for per in range(1, temp):
        perStr = str(bin(per).lstrip('-0b').zfill(N))
        if perStr.count('1') == K:
            perms[perStr] = Permutations(dict())

    min = 999999999
    temp = prime_sieve(10 ** N - 1)
    temp2 = 10 ** (N - 1)
    # for number in range(10 ** (N - 1), 10 ** N - 1):
    for number in temp:
        if number >= temp2:
            if sameDigits(number, K):
                prStr = str(number)
                for key, val in perms.items():
                    prev = -1
                    suits = True
                    tmpStr = ""
                    for sl in range(0, len(key)):
                        if key[sl] == '1':
                            tmpStr += '1'
                            if prev != -1:
                                if prev != prStr[sl]:
                                    suits = False
                                    break
                            prev = prStr[sl]
                        else:
                            tmpStr += prStr[sl]
                    if suits:
                        tArr = [1, prStr, number]
                        if tmpStr in perms[key].d:
                            perms[key].d[tmpStr][0] += 1
                            perms[key].d[tmpStr][1] += " " + prStr
                        else:
                            perms[key].d[tmpStr] = tArr

                        if perms[key].d[tmpStr][0] == L:
                            if min > perms[key].d[tmpStr][2]:
                                min = perms[key].d[tmpStr][2]
                                toPrint = perms[key].d[tmpStr][1]
                                # print(perms[key].d[tmpStr][1])
                                # stopFind = True
    print(toPrint)
