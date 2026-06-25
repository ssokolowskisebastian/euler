# decrypt the message and find the sum of the ASCII values in the original text.
import string

from timer_utils import timer

with open("../../euler_files/euler0059") as f:
    ciphertext = list(map(int, f.read().split(",")))

acceptable = set(
    ord(ch) for ch in string.ascii_letters + string.digits + " .,:;+?!/[]()'\""
)


def possible_keys(ctext):
    result = []
    for key_char in string.ascii_lowercase:
        key = ord(key_char)
        plaintext = {ct ^ key for ct in set(ctext)}

        if plaintext <= acceptable:
            result.append(key)
    return result


@timer
def solution() -> int:
    groups = [ciphertext[i::3] for i in range(3)]
    candidates = [possible_keys(group)[0] for group in groups]

    return sum(c ^ candidates[i % 3] for i, c in enumerate(ciphertext))


solution()  # result: 129448 took: 0.002073s
