def constructArray(n: int, k: int) -> [int]:
    tag = [i for i in range(1, k + 2)]
    ans = []
    for i in range(k + 1):
        if i % 2 == 0:
            ans.append(tag.pop(0))
        else:
            ans.append(tag.pop())
    return ans + [t for t in range(k + 2, n + 1)]


if __name__ == '__main__':
    print(constructArray(3, 1))
    print(constructArray(3, 2))
    print(constructArray(5, 2))
