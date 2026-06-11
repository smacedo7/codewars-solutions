from math import sqrt


def find_number(sums):
    if not sums:
        return 0

    n = int((1 + sqrt(1 + 8 * len(sums))) / 2)

    if n == 2:
        return sums[0]

    a = (sums[0] + sums[1] - sums[n - 1]) // 2
    return int(''.join(map(str, [a] + [sums[i] - a for i in range(n - 1)])))