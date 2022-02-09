def numRescueBoats(people: [int], limit: int) -> int:
    people.sort()
    res = 0
    n = len(people)
    light, heavy = 0, n - 1
    while light <= heavy:
        if people[light] + people[heavy] > limit:
            heavy -= 1
        else:
            light += 1
            heavy -= 1
        res += 1
    return res


if __name__ == '__main__':
    print(numRescueBoats(people=[1, 2], limit=3))
    print(numRescueBoats(people=[2, 2], limit=6))
    print(numRescueBoats(people=[3, 5, 3, 4], limit=5))
    print(numRescueBoats(people=[3, 2, 2, 1], limit=3))
