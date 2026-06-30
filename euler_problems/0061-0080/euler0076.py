from timer_utils import timer


@timer
def solution(limit):
    ways = [0] * (limit + 1)
    ways[0] = 1

    for number in range(1, limit):
        for i in range(number, limit + 1):
            ways[i] += ways[i - number]

    return ways[limit]


solution(100)  # result: 190569291 took: 0.000828s
