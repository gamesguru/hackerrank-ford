"""
Solve 3rd problem
"""
import math
from typing import List, Tuple, Dict

# costs = [190, 200, 450, 499, 358, 160]
# weeks = 3
# Answer [(190), (200, 450, 499, 358), (160)]

costs = [190, 200, 450, 870, 110, 499, 358, 160]
weeks = 4


def optimize():
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
    limits: List[int] = [len(costs) - (weeks - x) for x in range(weeks)]
    bars = [x for x in range(weeks)]
    bars.insert(0, 0)
    bars.append(len(costs))
    # hard-coded test case
    # bars = [1, 2, 3]
    # bars.insert(0, 0)
    # bars.append(len(costs))

    results: Dict[Tuple, int] = {}
        # {
        #     (1, 2, 3): 470,
        #     (1, 2, 4): 570,
        #     ...
        #     (6, 7, 8): 492
        # }
    print(bars)
    print(limits)
    summ = 0

    print(costs)
    print()
    summ = 0
    for i in range(len(bars) - 1):
        summ += max(costs[bars[i]:bars[i + 1]])

    while True:
        i = bars[-1]
        while True:
            break
        break
    return sum(costs)


def minimum_weekly_input():
    n = len(costs)
    print(f"n{weeks}")
    print(f"costs={costs}")

    # Initialize dp array
    dp = [[math.inf] * (weeks + 1) for _ in range(n + 1)]
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
    for w in range(0, weeks):
        print(f"w={w}")
        # for each of the cost
        for i in range(1, n + 1):
            print(f"  i={i}")
            max_cost_in_week = 0

            for k in range(i - 1, -1, -1):
                # Compute the maximum cost within the current subarray being considered for the week
                max_cost_in_week = max(max_cost_in_week, costs[k])
                print(f"    k={k}, c={costs[k]}, maxc={max_cost_in_week}", end="")

                # Ensure the previous state is valid before using it in the computation
                if dp[k][w] != math.inf:
                    dp[i][w + 1] = min(dp[i][w + 1], dp[k][w] + max_cost_in_week)
                    print(f", dp={dp[i]}")
                else:
                    print()

    for p in dp:
        print(f"p={p}")
    return int(dp[n][weeks])


print(optimize())
