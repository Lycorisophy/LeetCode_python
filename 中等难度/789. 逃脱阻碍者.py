def escapeGhosts(ghosts: [[int]], target: [int]) -> bool:
    base = abs(0 - target[0]) + abs(0 - target[1])
    for ghost in ghosts:
        if base >= abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]):
            return False
    return True

if __name__ == '__main__':
    print(escapeGhosts(ghosts=[[1, 0], [0, 3]], target=[0, 1]))
    print(escapeGhosts(ghosts=[[1, 0]], target=[2, 0]))
    print(escapeGhosts(ghosts=[[2, 0]], target=[1, 0]))
    print(escapeGhosts(ghosts=[[5, 0], [-10, -2], [0, -5], [-2, -2], [-7, 1]], target=[7, 7]))
    print(escapeGhosts(ghosts=[[-1, 0], [0, 1], [-1, 0], [0, 1], [-1, 0]], target=[0, 0]))
