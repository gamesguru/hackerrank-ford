"""
Solve 3rd problem
"""

import math
from typing import Dict, List, Tuple

# COSTS = [190, 200, 450, 499, 358, 160]
# WEEKS = 3
# Answer [(190), (200, 450, 499, 358), (160)]

COSTS = [190, 200, 450, 870, 110, 499, 358, 160]
WEEKS = 4
# Solution: ('1,2,7', 1420)

# EXAMPLE PROBLEMS
# 3 weeks
# [190 | 200 | 450 499 358 160]
# [190 | 200 450 | 499 358 160]
# [190 | 200 450 499 | 358 160]
# [190 | 200 450 499 358 | 160]

# [190 200 | 450 | 499 358 160]
# [190 200 | 450 499 | 358 160]
# [190 200 | 450 499 358 | 160]

# [190 200 450 | 499 | 358 160]
# [190 200 450 | 499 358 | 160]

# [190 200 450 499 | 358 | 160]

# 4 weeks
# [190 | 200 | 450 | 870 110 499 358 160]
# [190 | 200 | 450 870 | 110 499 358 160]
# [190 | 200 | 450 870 110 | 499 358 160]
# [190 | 200 | 450 870 110 499 | 358 160]
# [190 | 200 | 450 870 110 499 358 | 160]

# [190 | 200 450 | 870 | 110 499 358 160]
# [190 | 200 450 | 870 110 | 499 358 160]
# [190 | 200 450 | 870 110 499 | 358 160]
# [190 | 200 450 | 870 110 499 358 | 160]

# [190 | 200 450 870 | 110 | 499 358 160]
# [190 | 200 450 870 | 110 499 | 358 160]
# [190 | 200 450 870 | 110 499 358 | 160]

# [190 | 200 450 870 110 | 499 | 358 160]
# [190 | 200 450 870 110 | 499 358 | 160]

# [190 | 200 450 870 110 499 | 358 | 160]

# [190 200 | 450 | 870 | 110 499 358 160]
# [190 200 | 450 | 870 110 | 499 358 160]
# [190 200 | 450 | 870 110 499 | 358 160]
# [190 200 | 450 | 870 110 499 358 | 160]


def calculate_sum(bars: List[int]) -> int:
    """Sums the maxes of each partition for a given set of separators"""
    summ = 0
    for i in range(len(bars) - 1):
        summ += max(COSTS[bars[i] : bars[i + 1]])
    return summ


def optimize() -> Tuple[str, int]:
    """Main solution method"""
    limits: List[int] = [len(COSTS) - (WEEKS - x) + 1 for x in range(WEEKS - 1)]
    bars = [x + 1 for x in range(WEEKS - 1)]
    bars.insert(0, 0)
    bars.append(len(COSTS))

    print("Limits  ", limits)
    print("Bars ", bars)
    print("Costs", COSTS)
    print()

    results: Dict[str, int] = {}
    # i.e., {'1,2,3': 470, '1,2,4': 570, ... '6,7,8': 492}

    # Main loop
    while True:
        # Calculate sum, add to results
        results[",".join(str(x) for x in bars[1:-1])] = calculate_sum(bars)
        # Move bars
        finished = move_next(bars, limits)

        if finished:
            break

    print("Results:")
    for k, v in results.items():
        print(f"    {k}: {v}")

    _min_partition = min(results, key=results.get)  # type: ignore
    return _min_partition, results[_min_partition]


def move_next(bars: List[int], limits: List[int]) -> bool:
    """Advance a couple bars. Can also use itertools.combination()"""
    for x in range(len(bars) - 2, 0, -1):
        # print(f"Curr index: {x}")
        if bars[x] != limits[x - 1]:
            bars[x] += 1
            for y in range(x + 1, len(bars) - 1):
                bars[y] = bars[y - 1] + 1
            return False
    return True


def optimize_official_dynamic_programming_solution():
    """
    Main solution.  Answer from:
    https://leetcode.com/discuss/interview-question/5876966/LinkedIn-OA-2025-Summer-Intern
    """
    n = len(COSTS)
    print(f"n{WEEKS}")
    print(f"costs={COSTS}")

    # Initialize dp array
    dp = [[math.inf] * (WEEKS + 1) for _ in range(n + 1)]
    # dp2 = [[math.inf] * (weeks + 1)] * (n + 1)
    # print(dp)
    # print(dp2)
    # print(dp == dp2)
    # [inf, inf, inf, inf] for 190
    dp[0][0] = 0
    #   ? w0 w1 w2
    # [ 0 _  _  _ ] ?
    # [ _ _  _  _ ] 190
    # [ _ _  _  _ ] 200
    # [ _ _  _  _ ] 450
    # [ _ _  _  _ ] 499
    # [ _ _  _  _ ] 358
    # [ _ _  _  _ ] 160

    # For each week
    for w in range(0, WEEKS):
        print(f"w={w}")
        # for each of the cost
        for i in range(1, n + 1):
            print(f"  i={i}")
            max_cost_in_week = 0

            for k in range(i - 1, -1, -1):
                # Compute the maximum cost within the current subarray
                # being considered for the week
                max_cost_in_week = max(max_cost_in_week, COSTS[k])
                print(f"    k={k}, c={COSTS[k]}, maxc={max_cost_in_week}", end="")

                # Ensure the previous state is valid before using it in the computation
                if dp[k][w] != math.inf:
                    dp[i][w + 1] = min(dp[i][w + 1], dp[k][w] + max_cost_in_week)
                    print(f", dp={dp[i]}")
                else:
                    print()

    for p in dp:
        print(f"p={p}")
    return int(dp[n][WEEKS])


print()

print(f"Solution: {optimize()}")
# print(optimize_official_dynamic_programming_solution())
