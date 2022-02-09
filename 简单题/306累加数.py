# 累加数是一个字符串，组成它的数字可以形成累加序列。
#
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
#
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
#
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/additive-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# TODO 不会
def isAdditiveNumber(num: str) -> bool:
    for i, data in enumerate(num):
        return False
    return True


if __name__ == '__main__':
    print(isAdditiveNumber(199100199))
