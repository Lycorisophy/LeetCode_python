from collections import Counter


def findSubstring(s: str, words: [str]) -> [int]:
    n = s.__len__()
    m = words.__len__()
    w = words[0].__len__()
    a = m * w
    word_counter = {}
    f_set = set()
    for word in words:
        f_set.add(word[0])
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    i = 0
    res = []
    r = n - a + 1
    while i < r:
        f = i
        cnt = 0
        while cnt < m:
            if s[f] in f_set:
                cnt += 1
                f += w
            else:
                break
        if cnt == m:
            window = s[i:i+a]
            cnt = 0
            copy_counter = word_counter.copy()
            while cnt < m:
                ws = cnt*w
                word = window[ws:ws+w]
                if word in word_counter:
                    copy_counter[word] -= 1
                    if copy_counter[word] < 0:
                        break
                    cnt += 1
                else:
                    break
            if cnt == m:
                res.append(i)
                i += 1
            else:
                i += 1
        else:
            i += 1
    return res


if __name__ == '__main__':
    print(findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
    print(findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
    print(findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
