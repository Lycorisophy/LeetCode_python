def minDeletionSize(strs: [str]) -> int:
    n = strs.__len__()
    if n < 2:
        return 0

    def is_de(arrs):
        pre = arrs[0]
        for arr in arrs:
            if arr < pre:
                return True
            pre = arr
        return False

    cnt = 0
    for s in zip(*strs):
        if is_de(s):
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(minDeletionSize(["cba", "daf", "ghi"]))
    print(minDeletionSize(["a", "b"]))
    print(minDeletionSize(["zyx", "wvu", "tsr"]))
