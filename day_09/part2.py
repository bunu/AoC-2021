from typing import List
from day_09.part1 import local_min


def calculate_basin(problem: List[str], i: int, j: int) -> set:
    basin = {(i, j)}
    old_points = {(i, j)}
    while len(old_points):
        new_points = set()
        for x, y in old_points:
            if x != 0 and problem[x][y] < problem[x - 1][y] != "9":
                new_points.add((x - 1, y))
            if x != len(problem) - 1 and problem[x][y] < problem[x + 1][y] != "9":
                new_points.add((x + 1, y))
            if y != 0 and problem[x][y] < problem[x][y - 1] != "9":
                new_points.add((x, y - 1))
            if y != len(problem[0]) - 1 and problem[x][y] < problem[x][y + 1] != "9":
                new_points.add((x, y + 1))
        old_points = set(new_points)
        basin = basin.union(old_points)
    return basin


def main():
    problem = [line.strip() for line in open("problem", "r").readlines()]
    basins = []
    for i in range(len(problem)):
        for j in range(len(problem[0])):
            if local_min(problem, i, j):
                basins.append(len(calculate_basin(problem, i, j)))
    basins = sorted(basins, reverse=True)
    print("Part2 Answer: %s" % (basins[0]*basins[1]*basins[2]))


if __name__ == '__main__':
    main()
