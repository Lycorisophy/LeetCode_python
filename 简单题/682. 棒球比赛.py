def calPoints(ops: [str]) -> int:
    nums = []
    for op in ops:
        if op == 'C':
            nums.pop(-1)
        elif op == 'D':
            nums.append(nums[-1]*2)
        elif op == '+':
            nums.append(nums[-1]+nums[-2])
        else:
            nums.append(int(op))
    return sum(nums)


if __name__ == '__main__':

    print(calPoints(["5","-2","4","C","D","9","+","+"]))

