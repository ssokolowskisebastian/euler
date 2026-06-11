from timer_utils import timer

ones = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4}

teens = {10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}

tens = {20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}


def letter_count(n=1000):
    if n == 1000:
        return len("onethousand")

    total = 0

    if n >= 100:
        total = ones[n // 100] + len("hundred")
        if n % 100 != 0:
            total += len("and")
        n %= 100

    if n >= 20:
        total += tens[(n // 10) * 10]
        n %= 10

    if n >= 10:
        total += teens[n]
    else:
        total += ones[n]

    return total


@timer
def solution(n=1000):
    return sum(letter_count(i) for i in range(n + 1))


solution()  # result: 21124 took: 0.000549s
