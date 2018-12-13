import sys
from math import sqrt

def is_prime(a):
    return a > 1 and all(a % i for i in range(2, int(sqrt(a)+1)))


if __name__ == "__main__":

    primes = []
    primes.append(2)

    for b in range(3, 30009, 2):
        if (is_prime(b)):
            primes.append(b)

    for index, line in enumerate(sys.stdin):
        # if index != 0:
        n = int(line.strip())
        aMax = 0
        bMax = 0
        nMax = 0

        for a in range(-n + 1, n + 1, 2):
            for b in primes:
                k = 0
                if b <= n:

                    while (is_prime(k * k + a * k + b)):
                        k += 1

                    if (k > nMax):
                        aMax = a
                        bMax = b
                        nMax = k
                        # print("new record = ",a,b,k)

        print(aMax, bMax)


