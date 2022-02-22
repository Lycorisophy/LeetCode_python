# 链接：https://leetcode-cn.com/problems/pancake-sorting
def pancakeSort(arr: [int]) -> [int]:
    ans = []
    for n in range(len(arr), 1, -1):
        index = 0
        for i in range(n):
            if arr[i] > arr[index]:
                index = i
        if index == n - 1:
            continue
        m = index
        for i in range((m + 1) // 2):
            arr[i], arr[m - i] = arr[m - i], arr[i]  # 原地反转
        for i in range(n // 2):
            arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]  # 原地反转
        ans.append(index + 1)
        ans.append(n)
    return ans


if __name__ == '__main__':
    print(pancakeSort([3, 2, 4, 1]))
    print(pancakeSort([1, 2, 3]))
