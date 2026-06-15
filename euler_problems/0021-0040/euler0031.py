# How many different ways can £2 be made using any number of coins?
from timer_utils import timer


@timer  # Dynamic Approach O(CT)
def solution(target=200, coins=[1, 2, 5, 10, 20, 50, 100, 200]):
    ways = [1] + [0] * target

    for coin in coins:
        for amt in range(coin, target + 1):
            ways[amt] += ways[amt - coin]
    return ways[target]


solution()  # result: 73682 took: 0.000130s
