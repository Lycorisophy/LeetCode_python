def findRestaurant(list1: [str], list2: [str]) -> [str]:
    d = {}
    for list in set(list1) & set(list2):
        for i, l1 in enumerate(list1):
            if l1 == list:
                break
        for j, l2 in enumerate(list2):
            if l2 == list:
                break
        d[list] = i+j
    min_value = min(d.values())
    return [k for k in d if d[k] == min_value]


if __name__ == '__main__':
    print(findRestaurant(["Shogun", "KFC", "Burger King", "M"],
                         ["KFC", "Shogun", "Burger King"]))

