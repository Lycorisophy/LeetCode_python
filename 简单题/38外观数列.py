def countAndSay(n: int) -> str:
    res = '1'
    for i in range(n-1):
        res = sayYourSelf(res)
    return res


def sayYourSelf(input: str) -> str:
    output = ''
    j = 0
    before = input[0]
    for i, data in enumerate(input):
        if data != before:
            output += str(j)+str(before)
            before = data
            j = 0
        j += 1
    output += str(j) + str(input[-1])
    return output


if __name__ == "__main__":
    print(countAndSay(30))
