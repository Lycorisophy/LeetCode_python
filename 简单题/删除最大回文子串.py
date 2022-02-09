def slice_window(one_str, w=1):
    res_list = []
    for i in range(0, len(one_str) - w + 1):
        res_list.append([one_str[i:i + w], [i, i + w - 1]])
    return res_list


def is_palindrome(l):
    if len(l) == 1:
        return True
    half = len(l) // 2
    if len(l) % 2 == 0:
        first_list = l[:half]
        second_list = l[half:]
    else:
        first_list = l[:half]
        second_list = l[half + 1:]
    if first_list == second_list[::-1]:
        return True
    return False


def removeMaxPalindromeSub(l: [str]):
    all_sub = []
    n = l.__len__()
    for i in range(2, n):
        all_sub += slice_window(l, i)
    all_sub.append([l, [0, n - 1]])
    new_list = []
    for one in all_sub:
        if is_palindrome(list(one[0])):
            new_list.append(one)
    new_list.sort(key=lambda x: x[1][1] - x[1][0], reverse=True)
    maxPalindromeSub = new_list[0][1]
    for _ in range(maxPalindromeSub[1] - maxPalindromeSub[0] + 1):
        l.pop(maxPalindromeSub[0])