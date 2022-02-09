# TODO(LySoY):这是求是否是3的整数倍
def isMultiOfThree(n: int) -> bool:
    if n == 1:
        return True
    else:
        tmp = n
        while True:
            if tmp < 10:
                if tmp in [3,6,9]:
                    return True
                else:
                    return False
            else:
                sum = 0
                for i, data in enumerate(str(n)):
                   sum += int(data)
                tmp = sum



if __name__ == '__main__':
    print(isMultiOfThree(15))
