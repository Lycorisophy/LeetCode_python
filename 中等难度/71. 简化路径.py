def simplifyPath(path: str) -> str:
    stack = []
    for p in path.split('/'):
        if p not in ['.', '..', '']:
            stack.append(p)
        elif p == '..' and stack:
            stack.pop()
    return f"/{'/'.join(stack)}"


if __name__ == '__main__':
    print(simplifyPath(path="/home/"))
    print(simplifyPath(path="/home//foo/"))
    print(simplifyPath(path="/../"))
    print(simplifyPath("/a/./b/../../c/"))
