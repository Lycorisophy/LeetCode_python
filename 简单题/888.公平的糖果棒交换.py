def fairCandySwap(A: [int], B: [int]) -> [int]:
    gap = (sum(A) - sum(B))//2
    set_a = set(A)
    for b in B:
        t = b + gap
        if t in set_a:
            return [t, b]


if __name__ == '__main__':
    print(fairCandySwap([1, 2, 5], [2, 4]))
