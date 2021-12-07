from collections import Counter


def calculate_fish(file: str, iterations: int) -> int:
    problem = [int(s) for s in open(file, "r").read().strip().split(",")]
    fish_counts = Counter(problem)
    for _ in range(0, iterations):
        next_iteration = {}
        for fish, num in fish_counts.items():
            if fish > 0:
                next_iteration[(fish-1)] = next_iteration.get(fish-1, 0) + num
            else:
                next_iteration[6] = next_iteration.get(6, 0) + num
                next_iteration[8] = next_iteration.get(8, 0) + num
        fish_counts = next_iteration

    return sum(fish_counts.values())
