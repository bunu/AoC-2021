def main():
    problem = [line.strip().split(" | ") for line in open("problem", "r").readlines()]
    count = 0
    for line in problem:
        digit_lens = [len(s) for s in line[1].split()]
        for digit in digit_lens:
            if digit == 2 or digit == 3 or digit == 4 or digit == 7:
                count += 1

    print("Part1 Answer: %s" % count)


if __name__ == '__main__':
    main()
