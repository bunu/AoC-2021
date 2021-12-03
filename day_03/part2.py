from typing import List


def most_common(problem: List[str], position: int, string: str) -> int:
    values = [s[position] for s in problem if s[position] == string]
    return len(values) >= (len(problem) - len(values))


def main():
    problem = [s.strip() for s in open("problem", "r").readlines()]
    oxygen = problem
    co2 = problem
    for i in range(0, len(problem[0])):
        if most_common(oxygen, i, "1"):
            oxygen = [s for s in oxygen if s[i] == "1"]
        else:
            oxygen = [s for s in oxygen if s[i] == "0"]
        if len(oxygen) == 1:
            break

    for i in range(0, len(problem[0])):
        if not most_common(co2, i, "1"):
            co2 = [s for s in co2 if s[i] == "1"]
        else:
            co2 = [s for s in co2 if s[i] == "0"]
        if len(co2) == 1:
            break

    print("Part2 Answer: %s" % (int(oxygen[0], 2) * int(co2[0], 2)))


if __name__ == '__main__':
    main()
