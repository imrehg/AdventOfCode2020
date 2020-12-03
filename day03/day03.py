from math import prod


def encounters(geography, slope=(3, 1)):
    width = len(geography[0])
    height = len(geography)
    pos = (0, 0)
    count = 0
    while pos[1] < height:
        here = geography[pos[1]][pos[0]]
        count += int(here == "#")
        pos = ((pos[0] + slope[0]) % width, pos[1] + slope[1])
    return count


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = [line.strip() for line in f.readlines()]
    print(f"Result 1: {encounters(input)}")

    checks = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    totals = []
    for check in checks:
        totals += [encounters(input, check)]
    print(f"Result 2: {prod(totals)}")
