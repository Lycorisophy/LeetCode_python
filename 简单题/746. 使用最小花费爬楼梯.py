def minCostClimbingStairs(cost: [int]) -> int:
    for i in range(2, len(cost)):
        cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
    return min(cost[-2], cost[-1])
    # minCost0, minCost1 = 0, min(cost[0], cost[1])
    # for i in range(2, len(cost)):
    #     minCost = min(minCost1 + cost[i], minCost0 + cost[i - 1])
    #     minCost0, minCost1 = minCost1, minCost;
    # return minCost


if __name__ == '__main__':
    print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
