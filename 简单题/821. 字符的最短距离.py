def shortestToChar(s: str, c: str) -> [int]:
    ans = [0] * len(s)
    pos = [i for i, letter in enumerate(s) if letter == c]
    lp = len(pos)

    def binarySearch(arr, l, r, x):
        if r >= l:
            mid = int(l + (r - l) / 2)
            if arr[mid] == x:
                return -1
            elif arr[mid] > x:
                return binarySearch(arr, l, mid - 1, x)
            else:
                return binarySearch(arr, mid + 1, r, x)
        else:
            return l

    for i, letter in enumerate(s):
        if letter != c:
            p = binarySearch(pos, 0, lp-1, i)
            if p != 0 and p < lp:
                ans[i] = min(pos[p]-i, i-pos[p-1])
            elif p == lp:
                ans[i] = i-pos[p-1]
            else:
                ans[i] = pos[p]-i
    return ans


if __name__ == '__main__':
    print(shortestToChar(s = "aaba", c = "b"))


