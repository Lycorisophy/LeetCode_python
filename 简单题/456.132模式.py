# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/132-pattern
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def find132pattern(nums: [int]) -> bool:
    l = len(nums)
    for i in range(l-2):
        for j in range(i, l-1):
            for k in range(j, l):
                if nums[i] < nums[k] < nums[j]:
                    return True
    return False


if __name__ == '__main__':
    print(find132pattern([1, 2, 3, 4]))
    print(find132pattern([3, 1, 4, 2]))
    print(find132pattern([-1, 3, 2, 0]))
