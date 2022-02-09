# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
#  
#
# 提示：
#
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def addStrings(num1: str, num2: str) -> str:
    l1, l2 = len(num1), len(num2)
    if l1 < l2:
        num3 = [0]*l2
        num1 = '0' * (l2 - l1) + num1
    elif l2 < l1:
        num3 = [0] * l1
        num2 = '0' * (l1 - l2) + num2
    else:
        num3 = [0] * l1
    i, p = 0, 0
    for n1, n2 in zip(num1[::-1], num2[::-1]):
        t = int(n1)+int(n2)
        num3[i] = (t + p) % 10
        p = (t + p) // 10
        i += 1
    res = ''
    if p == 1:
        res = '1'
    for n3 in num3[::-1]:
        res += str(n3)
    return res


if __name__ == '__main__':
    print(addStrings(num1='9999', num2='0'))
