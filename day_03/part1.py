from typing import List


def most_common(problem: List, position: int, string: str) -> int:
    values = [s[position] for s in problem if s[position] == string]
    return len(values) > (len(problem) - len(values))


def main():
    problem = [s.strip() for s in open("problem", "r").readlines()]
    gamma = ""
    epsilon = ""
    for i in range(0, len(problem[0])-1):
        if most_common(problem, i, "1"):
            gamma += "1"
        else:
            gamma += "0"

        if most_common(problem, i, "0"):
            epsilon += "1"
        else:
            epsilon += "0"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print("Part1 Answer: %s" % (gamma * epsilon))


if __name__ == '__main__':
    main()
