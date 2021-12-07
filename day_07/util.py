def calculate_level(problem: str, triangles=False) -> int:
    problem = [int(s) for s in open(problem, "r").read().strip().split(",")]
    fuels = []
    for level in range(max(problem)):
        fuel = 0
        for crab in problem:
            change = abs(level - crab)
            if triangles:
                change = (change * (change+1)) // 2
            fuel += change
        fuels.append(fuel)
    return min(fuels)
