from itertools import permutations

from timer_utils import timer


@timer
def solution(ring_size=5):
    best = ""

    nums = set(range(1, 11))
    sum_10 = sum(nums)

    for inner in permutations(range(1, 10), ring_size):
        inner_set = set(inner)

        total = sum_10 + sum(inner)
        if total % ring_size:
            continue
        magic_sum = total // ring_size

        outer = tuple(
            magic_sum - inner[i] - inner[(i + 1) % ring_size] for i in range(ring_size)
        )

        m = min(outer)

        if m < 1 or outer[0] != m:  # avoid rotation
            continue

        outer_set = set(outer)

        if len(outer_set) != ring_size or outer_set != nums - inner_set:
            continue

        s = "".join(
            f"{outer[i]}{inner[i]}{inner[(i + 1) % ring_size]}"
            for i in range(ring_size)
        )

        if s > best:
            best = s

    return best


solution()  # result: 6531031914842725 took: 0.011073s
