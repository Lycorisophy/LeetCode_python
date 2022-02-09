def groupAnagrams(strs: [str]) -> [[str]]:
    n = strs.__len__()
    vis = [False]*n
    res, tmp = [], []
    for i in range(n-1):
        if not vis[i]:
            astring = strs[i]
            m = astring.__len__()
            agram = {}
            for char in astring:
                if char in agram:
                    agram[char] += 1
                else:
                    agram[char] = 1
            vis[i] = True
            tmp = [astring]
            for j in range(i+1, n):
                if not vis[i]:
                    continue
                bstring = strs[j]
                if bstring.__len__() == m:
                    bgram = agram.copy()
                    is_True = True
                    for char in bstring:
                        if char not in bgram:
                            is_True = False
                            break
                        else:
                            bgram[char] -= 1
                            if bgram[char] < 0:
                                is_True = False
                                break
                    if is_True:
                        tmp.append(bstring)
                        vis[j] = True
            res.append(tmp.copy())
    if not vis[-1]:
        res.append([strs[-1]])
    return res


if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

