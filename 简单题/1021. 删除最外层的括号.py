def removeOuterParentheses(S: str) -> str:
    res = ''
    cnt = 0
    for s in S:
        if s == '(':
            if cnt > 0:
                res += '('
            cnt += 1
        else:
            cnt -= 1
            if cnt > 0:
                res += ')'
    return res


if __name__ == '__main__':
    print(removeOuterParentheses("(()())(())"))
    print(removeOuterParentheses("(()())(())(()(()))"))
    print(removeOuterParentheses("()()"))
