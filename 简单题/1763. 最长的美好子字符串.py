def longestNiceSubstring(s: str) -> str:
    def check(typeNum):
        nonlocal maxPos, maxLen
        lowerCnt = [0] * 26
        upperCnt = [0] * 26
        l, r, total, cnt = 0, 0, 0, 0
        while r < len(s):
            idx = ord(s[r].lower()) - ord('a')
            if s[r].islower():
                lowerCnt[idx] += 1
                if lowerCnt[idx] == 1 and upperCnt[idx] > 0:
                    cnt += 1
            else:
                upperCnt[idx] += 1
                if upperCnt[idx] == 1 and lowerCnt[idx] > 0:
                    cnt += 1
            if lowerCnt[idx] + upperCnt[idx] == 1:
                total += 1

            while total > typeNum:
                idx = ord(s[l].lower()) - ord('a')
                if lowerCnt[idx] + upperCnt[idx] == 1:
                    total -= 1
                if s[l].islower():
                    lowerCnt[idx] -= 1
                    if lowerCnt[idx] == 0 and upperCnt[idx] > 0:
                        cnt -= 1
                else:
                    upperCnt[idx] -= 1
                    if upperCnt[idx] == 0 and lowerCnt[idx] > 0:
                        cnt -= 1
                l += 1
            if cnt == typeNum and r - l + 1 > maxLen:
                maxPos, maxLen = l, r - l + 1
            r += 1

    maxPos, maxLen = 0, 0
    types = len(set(s.lower()))
    for i in range(1, types + 1):
        check(i)
    return s[maxPos: maxPos + maxLen]


if __name__ == '__main__':
    print(longestNiceSubstring("Bb"))
    print(longestNiceSubstring("c"))
    print(longestNiceSubstring("dDzeE"))
