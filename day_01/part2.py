def main():
    problem = [int(s) for s in open("problem", "r").readlines()]
    sum_list = [sum(x) for x in zip(problem[:-2], problem[1:-1], problem[2:])]
    increased = len([y for x,y in zip(sum_list[:-1], sum_list[1:]) if y > x])
    print("Part2 Answer: %s" % increased)


if __name__ == '__main__':
    main()
