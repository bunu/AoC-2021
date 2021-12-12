def main():
    problem = [line.strip() for line in open("problem", "r").readlines()]
    points = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }
    incomplete_lines = []
    for line in problem:
        open_brackets = []
        for bracket in line:
            if bracket == "(" or bracket == "[" or bracket == "{" or bracket == "<":
                open_brackets.append(bracket)
            else:
                old_bracket = open_brackets.pop()
                if not ((old_bracket, bracket) == ("(", ")") or (old_bracket, bracket) == ("[", "]") or
                        (old_bracket, bracket) == ("{", "}") or (old_bracket, bracket) == ("<", ">")):
                    open_brackets = []
                    break
        if len(open_brackets) != 0:
            incomplete_lines.append(open_brackets)

    scores = []
    for line in incomplete_lines:
        score = 0
        while len(line) != 0:
            score = score * 5 + points[line.pop()]
        scores.append(score)
    scores.sort()
    print("Part2 Answer: %s" % scores[len(scores) // 2])


if __name__ == '__main__':
    main()
