import itertools
import sys
from copy import deepcopy


def update(layout):
    new_layout = deepcopy(layout)
    max_i, max_j = len(layout) - 1, len(layout[0]) - 1
    for i in range(max_i + 1):
        i_vals = [val for val in [i - 1, i, i + 1] if 0 <= val <= max_i]
        for j in range(max_j + 1):
            current = layout[i][j]
            if current == ".":
                continue
            j_vals = [val for val in [j - 1, j, j + 1] if 0 <= val <= max_j]
            combos = set(itertools.product(i_vals, j_vals)) - {(i, j)}
            occupied = sum([layout[c[0]][c[1]] == "#" for c in combos])
            if current == "L" and occupied == 0:
                new_layout[i][j] = "#"
            if current == "#" and occupied >= 4:
                new_layout[i][j] = "L"
    return new_layout


def compare_layout(old, new):
    for i in range(len(old)):
        if old[i] != new[i]:
            return False
    return True


def print_layout(layout):
    for i in range(len(layout)):
        print("".join(layout[i]))


def count_occupied(layout):
    return "".join(["".join(row) for row in layout]).count("#")


dirs = set(itertools.product([-1, 0, 1], [-1, 0, 1])) - {(0, 0)}


def update2(layout):
    new_layout = deepcopy(layout)
    max_i, max_j = len(layout) - 1, len(layout[0]) - 1
    for i in range(max_i + 1):
        for j in range(max_j + 1):
            current = layout[i][j]
            if current == ".":
                continue
            # print(i, j, "==>", current)
            occupied = 0
            for d in dirs:
                loc = (i, j)
                # print(d)
                while True:
                    loc = (loc[0] + d[0], loc[1] + d[1])
                    if loc[0] < 0 or loc[0] > max_i or loc[1] < 0 or loc[1] > max_j:
                        break
                    val = layout[loc[0]][loc[1]]
                    # print(val)
                    if val in {"L", "#"}:
                        occupied += 1 if val == "#" else 0
                        break
                # print(occupied)
            # print(occupied)
            if current == "L" and occupied == 0:
                new_layout[i][j] = "#"
            if current == "#" and occupied >= 5:
                new_layout[i][j] = "L"
    return new_layout


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        seats = [list(line.strip()) for line in f.readlines()]
    layout = deepcopy(seats)
    while True:
        new_layout = update(layout)
        if compare_layout(layout, new_layout):
            break
        else:
            layout = new_layout
    print(count_occupied(new_layout))

    layout = deepcopy(seats)
    # i = 0
    while True:
        # i += 1
        new_layout = update2(layout)
        # print_layout(new_layout)
        if compare_layout(layout, new_layout):
            break
        else:
            layout = new_layout
        # print("="*10)
        # if i > 0:
        #     break
    print(count_occupied(new_layout))
