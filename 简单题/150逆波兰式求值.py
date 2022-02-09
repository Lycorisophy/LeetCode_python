def evalRPN(tokens: [str]) -> int:
    nums = []
    for i, data in enumerate(tokens):
        if data not in ['+', '-', '*', '/']:
            nums.append(int(data))
        else:
            tmp1 = nums.pop()
            tmp2 = nums.pop()
            if data == '+':
                tmp = tmp2 + tmp1
            if data == '-':
                tmp = tmp2 - tmp1
            if data == '*':
                tmp = tmp2 * tmp1
            if data == '/':
                tmp = int(tmp2 / tmp1)
            nums.append(tmp)
    return nums.pop()


if __name__ == "__main__":
    print(evalRPN(["2", "1", "+", "3", "*"]))