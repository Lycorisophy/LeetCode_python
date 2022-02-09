import operator


def maximumPopulation(logs: [[int]]) -> int:
    nums = []
    for log in logs:
        birth_year, death_year = log
        nums.append((birth_year, 1))
        nums.append((death_year, 0))
    nums.sort(key=operator.itemgetter(0, 1))
    res = 1950
    cur = 0
    max_num = 0
    for num in nums:
        year, is_birth = num
        if is_birth == 1:
            cur += 1
            if cur > max_num:
                max_num = cur
                res = year
        else:
            cur -= 1
    return res


if __name__ == '__main__':
    print(maximumPopulation([[2008,2026],[2004,2008],[2034,2035],[1999,2050],[2049,2050],[2011,2035],[1966,2033],[2044,2049]]))

