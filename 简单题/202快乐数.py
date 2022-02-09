# 编写一个算法来判断一个数 n 是不是快乐数。
#
# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
#
# 如果 n 是快乐数就返回 True ；不是，则返回 False 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/happy-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def isHappy(n: int) -> bool:
    if n == 1:
        return True
    res = [n]
    while True:
        sum = 0
        for i, data in enumerate(str(n)):
            sum += int(data)**2
        n = sum
        if n in res:
            return False
        res.append(n)
        if n == 1:
            return True


if __name__ == '__main__':
    print(isHappy(20))