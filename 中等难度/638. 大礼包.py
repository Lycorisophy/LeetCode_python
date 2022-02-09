def shoppingOffers(price: [int], special: [[int]], needs: [int]) -> int:
    def dfs(need, memo):
        if not any(need):
            return 0
        if str(need) in memo:
            return memo[str(need)]
        n = len(need)
        cost = sum([p * n for p, n in zip(price, need)])
        for sp in special:
            new_need = []
            for i in range(n):
                if need[i] - sp[i] < 0:
                    break
                else:
                    new_need.append(need[i] - sp[i])
            if n == len(new_need):
                cost = min(cost, sp[-1] + dfs(new_need, memo))
        memo[str(need)] = cost
        return cost

    return dfs(needs, {})


if __name__ == '__main__':
    print(shoppingOffers(price=[2, 5], special=[[3, 0, 5], [1, 2, 10]], needs=[3, 2]))
    print(shoppingOffers(price=[2, 3, 4], special=[[1, 1, 0, 4], [2, 2, 1, 9]], needs=[1, 2, 1]))
