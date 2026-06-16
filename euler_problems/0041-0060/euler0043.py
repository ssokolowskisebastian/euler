# The sber, 1406357289, is a 0 to 9 pandigital sber
# because it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.
#
# Let 𝑑1 be the 1st digit, 𝑑2 be the 2nd digit, and so on. In this way, we note the following:
# d_2 d_3 d_4=406 is divisible by 2 d_3 d_4 d_5=063 is divisible by 3
# d_4 d_5 d_6=635 is divisible by 5 d_5 d_6 d_7=357 is divisible by 7
# d_6 d_7 d_8=572 is divisible by 11 d_7 d_8 d_9=728 is divisible by 13
# d_8 d_9 d_10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property
from timer_utils import timer


@timer
def solution():
    digits = "0123456789"
    primes = [13, 11, 7, 5, 3, 2]
    nums = [f"{n:03}" for n in range(17, 1000, 17) if len(set(f"{n:03}")) == 3]

    for p in primes:
        res = []
        for s in nums:
            for d in digits:
                if d not in s and int(d + s[:2]) % p == 0:
                    res.append(d + s)
        nums = res

    total = 0
    for s in nums:
        for d in digits:
            if d not in s:
                total += int(d + s)

    return total


solution()  # result: 16695334890 took: 0.000420s
