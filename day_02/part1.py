def main():
    problem = [s.strip().split(" ") for s in open("problem", "r").readlines()]
    x = 0
    z = 0
    for direction, number in problem:
        number = int(number)
        if direction == "forward":
            x += number
        elif direction == "down":
            z += number
        elif direction == "up":
            z -= number
    print("Part1 Answer: %s" % (x*z))


if __name__ == '__main__':
    main()
