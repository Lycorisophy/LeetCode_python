# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#
# 进阶：
#
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/is-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def isSubsequence(s: str, t: str) -> bool:
    l1, l2 = len(s), len(t)
    i, j = 0, 0
    if l1 == 0:
        return True
    if l2 == 0:
        return False
    while True:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
        if i == l1:
            return True
        if j == l2:
            return False



if __name__ == '__main__':
    print(isSubsequence(s = "abc", t = "ahbgdc"))