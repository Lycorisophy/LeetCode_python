# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def twoSum(numbers: [int], target: int) -> [int]:
    l = len(numbers)
    top = l
    for i in range(l):
        for j in range(i+1, top):
            tmp = numbers[i] + numbers[j]
            if tmp == target:
                return [i+1, j+1]
            if tmp > target:
                top = j
                break
    return [0, 0]


if __name__ == '__main__':
    print(twoSum(numbers=[2, 7, 11, 15], target=9))
