from timer_utils import timer

with open("../../euler_files/euler0079") as f:
    keys = f.read().splitlines()


@timer
def solve(keys):
    pwd = ""

    while keys:
        candidates = {k[0] for k in keys}
        forbidden = {c for k in keys for c in k[1:]}

        next_digit = (candidates - forbidden).pop()
        pwd += next_digit

        keys = [k[1:] if k[0] == next_digit else k for k in keys]
        keys = [k for k in keys if k]

    return pwd


solve(keys)  # result: 73162890 took: 0.000298s
