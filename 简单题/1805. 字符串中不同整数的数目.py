def numDifferentIntegers(word: str) -> int:
    nums = set()
    tmp = ''
    for char in word:
        if char.isnumeric():
            tmp += char
        else:
            if tmp:
                nums.add(int(tmp))
            tmp = ''
    if tmp:
        nums.add(int(tmp))
    return nums.__len__()


if __name__ == '__main__':
    print(numDifferentIntegers("a123bc34d8ef34"))
    print(numDifferentIntegers("leet1234code234"))
    print(numDifferentIntegers("a1b01c001"))
