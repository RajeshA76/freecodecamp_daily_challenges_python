def calculate_neigh(arr,i,j,m,n):
    cnt = 0
    pairs = [(0,1),(1,0),(1,1),(-1,1),(1,-1),(0,-1),(-1,-1),(-1,0)]
    for p,r in pairs:
        if (i+p >= 0 and i+p < m )and (j+r >=0 and j+r <n) and arr[i+p][j+r] == 1:
            cnt += 1
    return cnt

def game_of_life(grid):
    m = len(grid)
    n = len(grid[0])
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            neigh = calculate_neigh(grid,i,j,m,n)
            if grid[i][j] == 1:
                if neigh < 2 or neigh > 3:
                    result[i][j] = 0
                else:
                    result[i][j] = 1
            else:
                if neigh == 3:
                    result[i][j] = 1

    return result