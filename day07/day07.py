import sys
import re


def parse_rule(rule):
    bag = re.match("^(.*) bags contain", rule).groups(1)[0]
    return bag, re.findall(r"(\d)+ ([a-z ]*) bag", rule)


def find_all_paths(rules, start_colour, end_colour, path=[]):
    path = path + [start_colour]
    if start_colour == end_colour:
        return [path]
    paths = []
    for colour in rules[start_colour]:
        node = colour[1]
        if node not in path:
            new_paths = find_all_paths(rules, node, end_colour, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def traverse(rules, start_colour, path=[], values=[], multiplier=1):
    path = path + [start_colour]
    if not rules[start_colour]:
        return path

    paths = []
    for colour in rules[start_colour]:
        node = colour[1]
        number = int(colour[0]) * multiplier
        values += [number]
        if node not in path:
            new_paths = traverse(rules, node, path, values, number)
            for new_path in new_paths:
                paths.append(new_path)
    return paths, values


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        written_rules = [line.strip() for line in f.readlines()]
        # print(written_rules)
    rules = {}
    for rule in written_rules:
        bag, contains = parse_rule(rule)
        rules[bag] = contains

    target = "shiny gold"
    count = 0
    for colour in rules:
        if colour == target:
            continue
        x = find_all_paths(rules, colour, target)
        count += 1 if x else 0
    print(count)

    # finals = [colour for colour in rules if not rules[colour]]
    # paths = []
    # for final_colour in finals:
    #     x = find_all_paths(rules, target, final_colour)
    #     paths += x
    # print(paths)

    x, values = traverse(rules, target)
    # print(x)
    print(sum(values))
