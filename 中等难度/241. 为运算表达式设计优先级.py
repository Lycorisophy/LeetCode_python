def diffWaysToCompute(expression: str) -> [int]:
    if expression.isdigit():
        return [int(expression)]

    res = []
    for i, char in enumerate(expression):
        if char in ['+', '-', '*']:
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i+1:])
            for L in left:
                for R in right:
                    if char == '+':
                        res.append(L + R)
                    elif char == '-':
                        res.append(L - R)
                    else:
                        res.append(L * R)
    return res


if __name__ == '__main__':
    print(diffWaysToCompute("2-1-1"))
    print(diffWaysToCompute("2*3-4*5"))
