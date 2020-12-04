import sys
import re

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def basic_validate(passports, required_fields):
    count = 0
    for passport in passports:
        fields = set(passport.keys())
        missing_required_fields = required_fields - fields
        count += 1 if not missing_required_fields else 0
    return count


def extended_validate(passports, required_fields):
    count = 0
    for passport in passports:

        try:
            byr = int(passport["byr"])
            if not 1920 <= byr <= 2002:
                continue
        except:
            continue
        try:
            iyr = int(passport["iyr"])
            if not 2010 <= iyr <= 2020:
                continue
        except:
            continue

        try:
            eyr = int(passport["eyr"])
            if not 2020 <= eyr <= 2030:
                continue
        except:
            continue

        try:
            if passport["hgt"].endswith("cm"):
                if not 150 <= int(passport["hgt"][:-2]) <= 193:
                    continue
            elif passport["hgt"].endswith("in"):
                if not 59 <= int(passport["hgt"][:-2]) <= 76:
                    continue
            else:
                continue
        except:
            continue

        try:
            if not re.match("^#[0-9a-f]{6}$", passport["hcl"]):
                continue
        except:
            continue

        try:
            if passport["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                continue
        except:
            continue

        try:
            if not re.match("^\d{9}$", passport["pid"]):
                continue
        except:
            continue

        # print(passport)
        count += 1
    return count


def read_passports_file(filename):
    passports = []
    with open(filename, "r") as f:
        buff = ""
        for line in f.readlines():
            if line.strip() == "" and buff != "":
                passports.append(buff)
                buff = ""
            else:
                separator = " " if buff else ""
                buff += separator + line.strip()
        if buff != "":
            passports.append(buff)
    passports_parsed = [
        {field.split(":")[0]: field.split(":")[1] for field in passport.split(" ")}
        for passport in passports
    ]
    return passports_parsed


if __name__ == "__main__":
    input_file = sys.argv[1]
    passports = read_passports_file(input_file)
    res1 = basic_validate(passports, required_fields)
    print(f"Result 1: {res1}")
    res2 = extended_validate(passports, required_fields)
    print(f"Result 2: {res2}")
