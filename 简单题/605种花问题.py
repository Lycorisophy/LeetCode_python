# 假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
#
# 给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/can-place-flowers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def canPlaceFlowers(flowerbed: [int], n: int) -> bool:
    length = len(flowerbed)
    last = 0
    for i in range(length):
        if n == 0:
            return True
        else:
            if 1 <= i <= length-2:
                if flowerbed[i] == 1:
                    last = 1
                else:
                    if last == 0 and flowerbed[i+1] == 0:
                        n -= 1
                        last = 1
                    else:
                        last = 0
            elif i == 0:
                if length == 1:
                    if flowerbed[i] == 1:
                        pass
                    else:
                        n -= 1
                else:
                    if flowerbed[i] == 1:
                        last = 1
                    elif flowerbed[i+1] == 1:
                        pass
                    else:
                        n -= 1
                        last = 1
            else:
                if flowerbed[i] == 0 and last == 0:
                    n -= 1
        if n == 0:
            return True
    return False


if __name__ == "__main__":
    flowerbed = [0]
    n = 1
    print(canPlaceFlowers(flowerbed, n))