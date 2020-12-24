import sys
import copy

def execute(ops):
    acc = 0
    runlist = set()
    loc = 0
    loop = True
    while loc not in runlist:
        runlist.add(loc)
        op, arg = ops[loc]
        # print(op, arg)
        if op == 'nop':
            loc += 1
        elif op == 'acc':
            acc += int(arg)
            loc += 1
        elif op == 'jmp':
            loc += int(arg)
        else:
            sys.exit("Segmentation fault")
        if loc == len(ops):
            loop = False
            break
    return acc, loop


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        operations = [line.strip().split(" ") for line in f.readlines()]
    res = execute(operations)
    print(res[0])

    for i, op in enumerate(operations):
        if op[0] in {"nop", "jmp"}:
            reoperations = copy.deepcopy(operations)
            reoperations[i][0] = "nop" if op[0] == "jmp" else "jmp"
            res = execute(reoperations)
            if not res[1]:
                print(res[0])
                break

