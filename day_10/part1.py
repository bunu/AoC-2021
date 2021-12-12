def main():
    problem = [line.strip() for line in open("problem", "r").readlines()]
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    total = 0
    for line in problem:
        open_brackets = []
        for bracket in line:
            if bracket == "(" or bracket == "[" or bracket == "{" or bracket == "<":
                open_brackets.append(bracket)
            else:
                old_bracket = open_brackets.pop()
                if not ((old_bracket, bracket) == ("(", ")") or (old_bracket, bracket) == ("[", "]") or
                        (old_bracket, bracket) == ("{", "}") or (old_bracket, bracket) == ("<", ">")):
                    total += points[bracket]
                    break
    print("Part1 Answer: %s" % total)


if __name__ == '__main__':
    main()
