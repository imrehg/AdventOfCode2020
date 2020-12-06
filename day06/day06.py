import sys


def read_customs_file(filename):
    declarations = []
    with open(filename, "r") as f:
        buff = []
        for line in f.readlines():
            if line.strip() == "" and buff:
                declarations.append(buff)
                buff = []
            else:
                buff += [{answer for answer in line.strip()}]
        if buff:
            declarations.append(buff)
    return declarations


def any_counts(declarations):
    return sum([len(set.union(*group)) for group in declarations])


def all_counts(declarations):
    return sum([len(set.intersection(*group)) for group in declarations])


if __name__ == "__main__":
    input_file = sys.argv[1]
    declarations = read_customs_file(input_file)
    result1 = any_counts(declarations)
    print(f"Result1: {result1}")

    result2 = all_counts(declarations)
    print(f"Result2: {result2}")
