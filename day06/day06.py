import sys


def read_customs_file(filename):
    declarations = []
    with open(filename, "r") as f:
        buff = []
        for line in f.readlines():
            if line.strip() == "" and buff != "":
                declarations.append(buff)
                buff = []
            else:
                separator = " " if buff else ""
                buff += [line.strip()]
        if buff != "":
            declarations.append(buff)
    return declarations


def any_counts(declarations):
    total = 0
    for group in declarations:
        total += len({answer for answer in "".join(group)})
    return total


def all_counts(declarations):
    total = 0
    for group in declarations:
        groupset = []
        for person in group:
            groupset.append({answer for answer in person})
        if len(groupset) > 1:
            overlap = groupset[0]
            for i in range(1, len(groupset)):
                overlap &= groupset[i]
            total += len(overlap)
        else:
            total += len(groupset[0])
    return total


if __name__ == "__main__":
    input_file = sys.argv[1]
    declarations = read_customs_file(input_file)
    result1 = any_counts(declarations)
    print(f"Result1: {result1}")

    result2 = all_counts(declarations)
    print(f"Result2: {result2}")
