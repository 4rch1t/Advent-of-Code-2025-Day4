import sys

grid = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip('\n')
        if line:
            grid.append(line)

n = len(grid)
m = len(grid[0]) if n > 0 else 0

dirs = [(-1,-1),(-1,0),(-1,1),
        (0,-1),        (0,1),
        (1,-1),(1,0),(1,1)]

ans = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] != '@':
            continue
        cnt = 0
        for di, dj in dirs:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '@':
                cnt += 1
        if cnt < 4:
            ans += 1

print(ans)
