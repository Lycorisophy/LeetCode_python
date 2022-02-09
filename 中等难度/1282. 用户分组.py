def groupThePeople(groupSizes: [int]) -> [[int]]:
    cnt = dict()
    res = list()
    for i, groupSize in enumerate(groupSizes):
        if groupSize == 1:
            res.append([i])
        elif groupSize not in cnt or cnt[groupSize][0] == 0:
            cnt[groupSize] = [groupSize-1, [i]]
        else:
            cnt[groupSize][0] -= 1
            cnt[groupSize][1].append(i)
            if cnt[groupSize][0] == 0:
                res.append(cnt[groupSize][1])
                cnt[groupSize] = [0, []]
    return res


if __name__ == '__main__':
    print(groupThePeople([3, 3, 3, 3, 3, 1, 3]))
    print(groupThePeople([2, 1, 3, 3, 3, 2]))
