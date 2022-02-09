import random


def minPairSum(nums: [int]) -> int:
    n = nums.__len__()
    nums.sort()
    i = 0
    j = n - 1
    m = nums[i] + nums[j]
    while i < j:
        i += 1
        j -= 1
        m = max(m, nums[i] + nums[j])
    return m

def fuc(arrs, nm, mm):
    random.shuffle(arrs)
    i = 0
    j = 1
    p = []
    while j < nm:
        p.append(arrs[i] + arrs[j])
        i += 2
        j += 2
    m = max(p)
    return m < mm


if __name__ == '__main__':
    print(minPairSum([1,10,27,35,24,40,37,21,9,45,33,40,42,44,48,4,30,50,44,36,26,26,26,26,7,31,41,26,4,13,5,14,29,11,8,22,39,4,7,1,37,10,35,7,24,40,2,5,14,40,25,10,41,17,23,39,24,31,8,8,32,30,31,31,20,6,10,7,48,22,48,17,31,45,11,34,2,14,34,24,10,45,35,2,49,34,20,42,6,45,17,34,24,11,23,50,15,35,35,50]))
    # for _ in range(10000):
    #     arr = []
    #     n = random.randint(2, 10**5)
    #     for _ in range(n):
    #         arr.append(random.randint(1, 10**5))
    #     arr.sort()
    #     i = 0
    #     j = n - 1
    #     p = []
    #     while i < j:
    #         p.append(arr[i]+arr[j])
    #         i += 2
    #         j -= 2
    #     m = max(p)
    #     for _ in range(10000):
    #         b = fuc(arr, n, m)
    #         if b:
    #             print('YES!!!!!!!')
