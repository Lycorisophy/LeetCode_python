def fullJustify(words: [str], maxWidth: int) -> [str]:
    '''
    很迷，不知道哪里错了，没办法，抄个答案
    res, tmp = list(), list()
    l1, l2 = 0, 0
    c = len(words)
    for j, word in enumerate(words):
        n = len(word)
        m = l2 + n
        if tmp:
            m += 1
        if m < maxWidth:
            tmp.append(word)
            if j == c - 1:
                res.append(' '.join(tmp)+' '*(maxWidth-m))
                return res
            l2 = m
            l1 += 1
        elif m == maxWidth:
            tmp.append(word)
            res.append(' '.join(tmp))
            tmp = list()
            l1, l2 = 0, 0
        else:
            if l1 == 1:
                res.append(tmp[0]+' '*(maxWidth-len(tmp[0])))
            else:
                if (maxWidth-l2)%(l1-1)==0:
                    a = (maxWidth-l2)//(l1-1)
                    b = a
                else:
                    a, b = divmod(maxWidth-l2, l1-2)
                nt = len(tmp)
                ans = ''
                for i, t in enumerate(tmp):
                    ans += t
                    if i < nt-2:
                        for _ in range(a+1):
                            ans += ' '
                    if i == nt-2:
                        for _ in range(b+1):
                            ans += ' '
                res.append(ans)
            if j == c - 1:
                res.append(word+' '*(maxWidth-n))
                return res
            tmp = [word]
            l1, l2 = 1, n
    return res
    '''
    def process(left, right):
        if right == n:
            res = ' '.join(words[left:right])
            res += ' ' * (maxWidth - len(res))
            return res
        spaces = right - left - 1
        if not spaces:
            return words[left] + ' ' * (maxWidth - len(words[left]))
        cur = sum(len(w) for w in words[left:right]) + spaces
        each = [1] * spaces
        j = 0
        while cur < maxWidth:
            each[j] += 1
            j += 1
            if j == spaces:
                j = 0
            cur += 1
        j = 0
        res = ''
        while left < right:
            res += words[left]
            if left < right - 1:
                res += ' ' * each[j]
                j += 1
            left += 1
        return res

    n = len(words)
    idx = 0
    ans = []
    while idx < n:
        i = idx
        curLen = len(words[idx])
        idx += 1
        while idx < n and curLen < maxWidth:
            curLen += 1
            curLen += len(words[idx])
            idx += 1
        if curLen > maxWidth:
            idx -= 1
            curLen -= len(words[idx]) + 1
        ans.append(process(i, idx))
    return ans


if __name__ == '__main__':
    print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
    print(fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                       "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
