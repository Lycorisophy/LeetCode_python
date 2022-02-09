# TODO 不对
def islandPerimeter(grid: [[int]]) -> int:
    x = sum(grid[i].count(1) > 0 for i in range(len(grid)))
    y = sum([x[j] for x in grid].count(1) > 0 for j in range(len(grid[0])))
    mx = any(0 < grid[i].count(1) < y for i in range(len(grid)))
    my = any(0 < [x[j] for x in grid].count(1) < x for j in range(len(grid[0])))
    return 4*max(x, y) if (mx and my) else 2*(x+y)


if __name__ == '__main__':
    print(islandPerimeter([[1,1,1],[1,0,0]]))