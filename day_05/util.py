from collections import Counter
from itertools import dropwhile
from typing import Tuple, List


def calculate_line_points(line: str, diags=False) -> List[Tuple[int, int]]:
    start, stop = line.split("->")
    startx, starty = [int(x) for x in start.split(",")]
    stopx, stopy = [int(x) for x in stop.split(",")]
    points = []
    if startx == stopx:
        length = stopy - starty
        minv = min(0, length)
        maxv = max(0, length)
        for i in range(minv, maxv+1):
            points.append((startx, starty+i))
    elif starty == stopy:
        length = stopx - startx
        minv = min(0, length)
        maxv = max(0, length)
        for i in range(minv, maxv+1):
            points.append((startx+i, starty))
    elif diags:
        steps = abs(stopx - startx)
        ystep = (stopy - starty) / steps
        xstep = (stopx - startx) / steps
        for i in range(0, steps+1):
            points.append((startx+(xstep * i), starty+(ystep * i)))
    return points


def calculate_doubles(diags=False) -> int:
    problem = [s.strip() for s in open("problem", "r").readlines()]
    points = []
    for line in problem:
        newpoints = calculate_line_points(line, diags)
        if len(newpoints) > 0:
            points.extend(newpoints)
    counts = Counter(points)
    for key, count in dropwhile(lambda key_count: key_count[1] > 1, counts.most_common()):
        del counts[key]
    return len(counts)
