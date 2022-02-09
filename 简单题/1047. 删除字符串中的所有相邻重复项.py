def removeDuplicates(S: str) -> str:
    ss = ['']
    for s in S:
        if s == ss[-1]:
            ss.pop(-1)
        else:
            ss.append(s)
    return ''.join(ss)


if __name__ == '__main__':
    print(removeDuplicates('abbaca'))

