# 给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。
#
# (注：分数越高的选手，排名越靠前。)
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/relative-ranks
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def findRelativeRanks(nums: [int]) -> [str]:
    nums2 = nums.copy()
    l = len(nums)
    res = []
    def quick_sort(nums: list, left: int, right: int) -> None:
        if left < right:
            i = left
            j = right
            # 取第一个元素为枢轴量
            pivot = nums[left]
            while i != j:
                # 交替扫描和交换
                # 从右往左找到第一个比枢轴量小的元素，交换位置
                while j > i and nums[j] < pivot:
                    j -= 1
                if j > i:
                    # 如果找到了，进行元素交换
                    nums[i] = nums[j]
                    i += 1
                # 从左往右找到第一个比枢轴量大的元素，交换位置
                while i < j and nums[i] > pivot:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            # 至此完成一趟快速排序，枢轴量的位置已经确定好了，就在i位置上（i和j)值相等
            nums[i] = pivot
            # 以i为枢轴进行子序列元素交换
            quick_sort(nums, left, i - 1)
            quick_sort(nums, i + 1, right)
    quick_sort(nums, 0, l-1)
    for i, num in enumerate(nums2):
        for j in range(l):
            if num == nums[j]:
                if j == 0:
                    res.append("Gold Medal")
                elif j == 1:
                    res.append("Silver Medal")
                elif j == 2:
                    res.append("Bronze Medal")
                else:
                    res.append(str(j+1))
    return res


if __name__ == '__main__':
    print(findRelativeRanks([444, 7, 568, 10000, 8888, 9999, 678, 4444, 4, 2, 1]))