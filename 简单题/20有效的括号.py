def isValid(s: str) -> bool:
    lefts = ['(', '[', '{']
    rights = [')', ']', '}']
    lrs = []
    for d in s:
        if d in lefts:
            lrs.append(d)
        else:
            if not lrs:
                return False
            i = rights.index(d)
            if lefts[i] != lrs[-1]:
                return False
            lrs.pop()
    return False if lrs else True


if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("([)]"))
    print(isValid("{[]}"))