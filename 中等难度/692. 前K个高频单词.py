def topKFrequent(words: [str], k: int) -> [str]:
    dic = {}
    for word in words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    res = []
    cnt = 0
    for d in dic:
        res.append(d[0])
        cnt += 1
        if cnt == k:
            return res
    return res


if __name__ == '__main__':
    print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k=2))
    print(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))
