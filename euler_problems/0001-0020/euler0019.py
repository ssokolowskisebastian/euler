# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import datetime

from timer_utils import timer


@timer # Brute force
def solution(start=1901, end=2000):
    count = 0

    for year in range(start, end + 1):
        for month in range(1, 13):
            if datetime.date(year, month, 1).weekday() == 6:
                count += 1
    return count


solution()  # result: 171 took: 0.000475s
