import math
from typing import Tuple, List

costs = [190, 200, 450, 499, 358, 160]
weeks = 3 
# Answer [(190), (200, 450, 499, 358), (160)]

# target 7
# [-100, 2, 5, 1000]
# [190, 200, |450, 499,| 358, 160]

results: List[Tuple[int, int]] = list()

def optimize(costs, weeks):
    return sum(costs)

def minimum_weekly_input(costs, weeks):
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

    # 190
    
    # For each week
    for w in range(0, weeks):

        # for each of the cost
        for i in range(1, n + 1):

            max_cost_in_week = 0

            for k in range(i - 1, -1, -1):
                if w == 2:
                    print(f"i={i}")
                    print("Costs for the next iter", costs[k])
                # Compute the maximum cost within the current subarray being considered for the week
                max_cost_in_week = max(max_cost_in_week, costs[k])

                # Ensure the previous state is valid before using it in the computation
                if dp[k][w] != math.inf:
                    dp[i][w + 1] = min(dp[i][w + 1], dp[k][w] + max_cost_in_week)

    for p in dp[1:]:
        print(f"p={p[1:]}")
    return int(dp[n][weeks])

print(minimum_weekly_input(costs, weeks))
