def validateStackSequences(pushed: [int], popped: [int]) -> bool:
    if not popped:
        return True
    if not pushed:
        return False
    stack = []
    i, j, k = 0, 0, 0
    while j < len(popped):
        if i < len(pushed) and pushed[i] == popped[j]:
            i += 1
            j += 1
        else:
            if not stack:
                stack.append(pushed[i])
                i += 1
            else:
                if stack[-1] == popped[j]:
                    stack.pop(-1)
                    j += 1
                else:
                    if i == len(pushed):
                        return False
                    stack.append(pushed[i])
                    i += 1
    return True


if __name__ == '__main__':
    print(validateStackSequences(pushed = [1,2,3,4,5], popped = [3,4,5,1,2]))