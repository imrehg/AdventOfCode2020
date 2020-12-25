import sys
from collections import Counter


def adapter_diffs(adapters):
    adapt = [0] + adapters + [adapters[-1] + 3]
    diffs = [z[1] - z[0] for z in zip(adapt[:-1], adapt[1:])]
    return diffs


def find_paths(diffs):
    paths = 1
    run = 0
    for current in diffs:
        if current == 1:
            run += 1
        else:
            if run > 1:
                multiplier = 2 ** (run - 1)
                if run > 3:
                    multiplier -= 2 ** (run - 4)
                paths *= multiplier
            # print(current, run, multiplier)
            run = 0
    if run > 1:
        paths *= 2 ** (run - 1)
    return paths


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        adapters = sorted([int(line.strip()) for line in f.readlines()])
    diffs = adapter_diffs(adapters)
    res = Counter(diffs)
    # print(res)
    val = res[1] * res[3]
    print(val)
    print(find_paths(diffs))
