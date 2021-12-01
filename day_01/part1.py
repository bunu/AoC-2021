def main():
    problem = [int(s) for s in open("problem", "r").readlines()]
    increased = len([y for x,y in zip(problem[:-1], problem[1:]) if y > x])
    print("Part1 Answer: %s" % increased)


if __name__ == '__main__':
    main()
