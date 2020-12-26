import sys

dirs = ["E", "S", "W", "N"]


class Ship:
    def __init__(self):
        self.loc = [0, 0]
        self.facing = "E"

    def follow_instruction(self, instruction):
        direction = instruction[0]
        value = int(instruction[1:])
        if direction == "F":
            direction = self.facing

        if direction in {"R", "L"}:
            turn = value // 90
            value = 0
            if direction == "L":
                turn *= -1
            self.facing = dirs[(dirs.index(self.facing) + turn) % len(dirs)]

        if direction == "N":
            self.loc[1] += value
        elif direction == "S":
            self.loc[1] -= value
        elif direction == "E":
            self.loc[0] += value
        elif direction == "W":
            self.loc[0] -= value

    def distance(self):
        return abs(self.loc[0]) + abs(self.loc[1])


class Ship2(Ship):
    def __init__(self):
        super().__init__()
        self.waypoint = [10, 1]

    def follow_instruction(self, instruction):
        # print(instruction, self.loc, self.waypoint)
        direction = instruction[0]
        value = int(instruction[1:])

        if direction == "F":
            self.loc = [
                self.loc[0] + self.waypoint[0] * value,
                self.loc[1] + self.waypoint[1] * value,
            ]
        elif direction == "N":
            self.waypoint[1] += value
        elif direction == "S":
            self.waypoint[1] -= value
        elif direction == "E":
            self.waypoint[0] += value
        elif direction == "W":
            self.waypoint[0] -= value
        elif direction in {"R", "L"}:
            turn = value // 90
            if direction == "R":
                turn = 4 - turn
            for i in range(turn):
                self.waypoint = [-self.waypoint[1], self.waypoint[0]]
        # print("==>", self.loc, self.waypoint, self.distance())


if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file, "r") as f:
        directions = [line.strip() for line in f.readlines()]

    ship = Ship()
    for d in directions:
        ship.follow_instruction(d)
        # break
    print(ship.distance())

    ship2 = Ship2()
    for d in directions:
        ship2.follow_instruction(d)
    print(ship2.distance())
