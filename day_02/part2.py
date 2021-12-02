def main():
    problem = [[k, int(v)] for k, v in [s.strip().split() for s in open("problem", "r").readlines()]]
    x = 0
    z = 0
    aim = 0
    for direction, number in problem:
        if direction == "forward":
            x += number
            z += number * aim
        elif direction == "down":
            aim += number
        elif direction == "up":
            aim -= number
    print("Part2 Answer: %s" % (x*z))


if __name__ == '__main__':
    main()
