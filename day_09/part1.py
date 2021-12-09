from typing import List


def local_min(problem: List[str], i: int, j: int) -> bool:
    is_min = True
    if i != 0 and problem[i][j] >= problem[i - 1][j]:
        is_min = False
    if i != len(problem) - 1 and problem[i][j] >= problem[i + 1][j]:
        is_min = False
    if j != 0 and problem[i][j] >= problem[i][j - 1]:
        is_min = False
    if j != len(problem) - 1 and problem[i][j] >= problem[i][j + 1]:
        is_min = False
    return is_min


def main():
    problem = [line.strip() for line in open("problem", "r").readlines()]
    count = 0
    for i in range(len(problem)):
        for j in range(len(problem[0])):
            if local_min(problem, i, j):
                count += 1 + int(problem[i][j])
    print("Part1 Answer: %s" % count)


if __name__ == '__main__':
    main()
