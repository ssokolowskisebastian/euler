# The nth term of the sequence of triangle numbers is given by, 𝑡𝑛=𝑛(𝑛+1)/2;
# so the first ten triangle numbers are: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19+11+25=55=𝑡10
# If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (linked file), a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?
from timer_utils import timer

with open("../../euler_files/euler0042") as f:
    words = sorted(f.read().replace('"', "").split(","))


def word_to_number(word: str) -> int:
    return sum(ord(c) - ord("A") + 1 for c in word)


def is_triangle(n):
    s = int((8 * n + 1) ** 0.5)
    return (s - 1) % 2 == 0 and s**2 == 1 + 8 * n


@timer
def solution():
    return sum(1 for word in words if is_triangle(word_to_number(word)))


solution()  # result: 162 took: 0.002977s
