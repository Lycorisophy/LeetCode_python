def makeGood(s: str) -> str:
    stack = []
    for c in s:
        if stack:
            tmp = abs(ord(c) - ord(stack[-1]))
            if tmp == 32:
                stack.pop(-1)
            else:
                stack.append(c)
        else:
            stack.append(c)
    return ''.join(stack)


if __name__ == '__main__':
    print(makeGood("leEeetcode"))
    print(makeGood("abBAcC"))
    print(makeGood("s"))
