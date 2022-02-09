def canConstruct(ransomNote: str, magazine: str) -> bool:
    m = {}
    for i, data in enumerate(magazine):
        try:
            m[data] += 1
        except KeyError:
            m[data] = 1
    for i, data in enumerate(ransomNote):
        try:
            m[data] -= 1
            if m[data] < 0:
                return False
        except KeyError:
            return False
    return True


if __name__ == '__main__':
    print(canConstruct("iaml", "shfkahflkhaskjbvchjcvvjaiwueqjskdahjsbfbncbxmvnbcxmn"))