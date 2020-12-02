#!/usr/bin/env python
"""
[...], the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
"""
from math import prod


def double_complement(expenses, target=2020):
    expenses = set(expenses)
    complements = {target - expense for expense in expenses}
    assert sum(expenses & complements) == target
    return prod(expenses & complements)


def triple_complement(expenses, target=2020):
    expenses = set(expenses)
    complements = {
        target - expense1 - expense2 for expense1 in expenses for expense2 in expenses
    }
    assert sum(expenses & complements) == target
    return prod(expenses & complements)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input = [int(value) for value in f.readlines()]
    result1 = double_complement(input)
    print(f"Part 1: {result1}")
    result2 = triple_complement(input)
    print(f"Part 2: {result2}")
