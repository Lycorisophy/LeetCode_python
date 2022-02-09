# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-peak-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def findPeakElement(nums: [int]) -> int:
    l = len(nums)
    if l == 1:
        return nums[0]
    if l == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    top = nums[l//2]
    if nums[0] > nums[l-1]:
        top = findPeakElement(nums[0:l // 2])
    else:
        top = findPeakElement(nums[l // 2:l])
    return top


if __name__ == "__main__":
    print(findPeakElement([1,4,3,1]))
