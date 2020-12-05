def seat_decode(seat):
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + column


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        ids = {seat_decode(line.strip()) for line in f.readlines()}
        result1 = max(ids)
    print(f"Result 1: {result1}")

    for seat in range(min(ids), max(ids)):
        if seat - 1 in ids and seat - 1 in ids and seat not in ids:
            result2 = seat
            break
    print(f"Result 2: {result2}")
