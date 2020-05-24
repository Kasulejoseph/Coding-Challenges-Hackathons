n = int(input())


def trailing_zeros(factorial):
    i = 5
    zeros = 0
    while factorial / i >= 1:
        zeros += factorial // i
        i *= 5
    print(zeros)


for _ in range(n):
    factorial = int(input())
    trailing_zeros(factorial)
