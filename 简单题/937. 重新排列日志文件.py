def reorderLogFiles(logs: [str]) -> [str]:
    def isNumLog(log: str) -> bool:
        for s in log[::-1]:
            if s == ' ':
                pass
            elif s.isnumeric():
                return True
            return False

    def orderNumAndLetterLogs(ns: [str]) -> [str]:
        numLogs = []
        letterLogs = []
        for n in ns:
            if isNumLog(n):
                numLogs.append(n)
            else:
                letterLogs.append(n)
        n = letterLogs.__len__()
        if n == 1:
            return letterLogs + numLogs
        orderLetterLogs(letterLogs, 0, n-1)
        return letterLogs + numLogs

    def whoIsBigger(str1: str, str2: str) -> int:
        str1, str2 = str1.split(), str2.split()
        n1, n2 = str1.__len__(), str2.__len__()
        for i in range(1, min(n1, n2)):
            tmp1, tmp2 = str1[i], str2[i]
            if tmp1 > tmp2:
                return 1
            elif tmp1 < tmp2:
                return -1
        if n1 != n2:
            if i == n1 - 1:
                return -1
            elif i == n2 - 1:
                return 1
        tmp1, tmp2 = str1[0], str2[0]
        if tmp1 > tmp2:
            return 1
        elif tmp1 < tmp2:
            return -1
        else:
            return 0

    def orderLetterLogs(nums: [str], left: int, right: int) -> None:
        if left < right:
            i = left
            j = right
            pivot = nums[left]
            while i != j:
                while j > i and whoIsBigger(nums[j], pivot) == 1:
                    j -= 1
                if j > i:
                    nums[i] = nums[j]
                    i += 1
                while i < j and whoIsBigger(nums[i], pivot) == -1:
                    i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = pivot
            orderLetterLogs(nums, left, i - 1)
            orderLetterLogs(nums, i + 1, right)

    n = logs.__len__()
    if n == 1:
        return logs
    return orderNumAndLetterLogs(logs)


if __name__ == '__main__':
    print(reorderLogFiles(["dig1 8 1 5 1","let1 art zero can","dig2 3 6","let2 own kit dig","let3 art zero"]))
    print(reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
