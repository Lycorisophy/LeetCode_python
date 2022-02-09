def longestWord(words: [str]) -> str:
    hashmap = {}
    for word in words:
        try:
            hashmap[len(word)].append(word)
        except KeyError:
            hashmap[len(word)] = [word]
    hashmap = sorted(hashmap.items(), key=lambda item:item[0])
    res = hashmap[0][1][0]
    do_remove = True
    do_rm = [[0 for _ in values[1]] for values in hashmap]
    for i, values in enumerate(hashmap):
        if i != 0:
            for j, value in enumerate(values[1]):
                for k, v in enumerate(hashmap[i-1][1]):
                    if value[:-1] == v and do_rm[i-1][k] == 0:
                        do_remove = False
                        if len(value) > len(res):
                            res = value
                        elif len(value) == len(res):
                            if value < res:
                                res = value
                if do_remove:
                    do_rm[i][j] = 1
                do_remove = True
    return res


if __name__ == '__main__':
    print(longestWord(["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]))
