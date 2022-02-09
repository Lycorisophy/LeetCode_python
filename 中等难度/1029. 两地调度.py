def twoCitySchedCost(costs: [[int]]) -> int:
    m = len(costs)
    n = m // 2
    costs.sort(key=lambda x: x[0] - x[1])
    res = 0
    for i in range(n):
        res += costs[i][0] + costs[i + n][1]
    return res


if __name__ == '__main__':
    print(twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
    print(twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]]))
    print(twoCitySchedCost(
        [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]]))
