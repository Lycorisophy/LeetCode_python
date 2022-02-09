from collections import Counter


def minCostToMoveChips(position: [int]) -> int:
    a = sum(p % 2 for p in position)
    return min(a, position.__len__()-a)


if __name__ == '__main__':
    print(minCostToMoveChips([1,2,3]))
    print(minCostToMoveChips([2,2,2,3,3]))

