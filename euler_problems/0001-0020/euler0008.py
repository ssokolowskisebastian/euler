# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?
from timer_utils import timer

with open("../../euler_files/euler0008") as f:
    digits = "".join(line.strip() for line in f)

digits_list = [int(d) for d in digits]


@timer  # O(n)
def solution(dgs_arr=digits_list, dgs_nums=13):
    product = 1
    zero_count = 0
    window = dgs_arr[:dgs_nums]
    for d in window:
        if d == 0:
            zero_count += 1
        else:
            product *= d
    max_product = product if zero_count == 0 else 0

    for i in range(dgs_nums, len(dgs_arr)):
        outgoing = dgs_arr[i - dgs_nums]
        incoming = dgs_arr[i]

        if outgoing == 0:
            zero_count -= 1
        else:
            product //= outgoing

        if incoming == 0:
            zero_count += 1
        else:
            product *= incoming

        if zero_count == 0:
            max_product = max(max_product, product)

    return max_product


solution()  # result: 23514624000 took: 0.000404s
