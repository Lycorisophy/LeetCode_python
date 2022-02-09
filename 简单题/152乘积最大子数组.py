def maxProduct(nums: [int]) -> int:
    pre = 0
    max = 0
    is_c = 0
    for i, data in enumerate(nums):
        if data == 0:
            pre = 0
            is_c = 0
        elif data < 0:
            if pre < 0:
                is_c = 1


    return max


# TODO 不会
if __name__ == '__main__':
    print(maxProduct([2, 3, -2, 4]))
