from collections import Counter


def uniqueOccurrences(arr: [int]) -> bool:
    occurrences = {}
    for a in arr:
        if a in occurrences:
            occurrences[a] += 1
        else:
            occurrences[a] = 1
    occurrences = [v for v in occurrences.values()]
    return set(occurrences).__len__() == occurrences.__len__()


if __name__ == '__main__':
    print(uniqueOccurrences([1,2,2,1,1,3]))
    print(uniqueOccurrences([1,2]))
    print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
