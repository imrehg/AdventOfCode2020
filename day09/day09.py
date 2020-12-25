import sys
import itertools


def find_odd_out(nums, preamble_length):
    for i in range(preamble_length, len(nums)):
        preamble = nums[i - preamble_length : i]
        combos = itertools.combinations(preamble, 2)
        valid_codes = {sum(c) for c in combos}
        if nums[i] not in valid_codes:
            return nums[i]


def find_continuous(target, nums):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            candidate = nums[i : j + 1]
            if sum(candidate) == target:
                return min(candidate) + max(candidate)


if __name__ == "__main__":
    input_file = sys.argv[1]
    preamble_length = int(sys.argv[2])
    with open(input_file, "r") as f:
        nums = [int(line.strip()) for line in f.readlines()]

    res = find_odd_out(nums, preamble_length)
    print(res)
    res2 = find_continuous(res, nums)
    print(res2)
