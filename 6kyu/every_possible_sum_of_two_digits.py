from math import sqrt


def find_number(sums):
    if not sums:
        return 0

    n = int((1 + sqrt(1 + 8 * len(sums))) / 2)

    if n == 2:
        a = min(9, sums[0])
        b = sums[0] - a
        return int(str(a) + str(b))

    a = (sums[0] + sums[1] - sums[n - 1]) // 2

    digits = [a]

    for i in range(n - 1):
        digits.append(sums[i] - a)

    return int(''.join(map(str, digits)))