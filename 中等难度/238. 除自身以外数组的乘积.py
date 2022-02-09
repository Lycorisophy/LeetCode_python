def productExceptSelf(nums: [int]) -> [int]:
    n = nums.__len__()
    output = [1] * n
    for i in range(1, n):
        output[i] = output[i-1] * nums[i-1]
    R = 1
    for i in range(n-2, -1, -1):
        R *= nums[i+1]
        output[i] *= R
    return output


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
