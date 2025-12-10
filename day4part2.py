import sys
from collections import deque

grid = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip('\n')
        if line:
            grid.append(list(line))

n = len(grid)
m = len(grid[0]) if n > 0 else 0

dirs = [(-1,-1),(-1,0),(-1,1),
        (0,-1),        (0,1),
        (1,-1),(1,0),(1,1)]

deg = [[0]*m for _ in range(n)]
active = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '@':
            active[i][j] = True

for i in range(n):
    for j in range(m):
        if not active[i][j]:
            continue
        c = 0
        for di, dj in dirs:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and active[ni][nj]:
                c += 1
        deg[i][j] = c

q = deque()
for i in range(n):
    for j in range(m):
        if active[i][j] and deg[i][j] < 4:
            q.append((i, j))

removed = 0

while q:
    i, j = q.popleft()
    if not active[i][j]:
        continue
    active[i][j] = False
    removed += 1
    for di, dj in dirs:
        ni = i + di
        nj = j + dj
        if 0 <= ni < n and 0 <= nj < m and active[ni][nj]:
            deg[ni][nj] -= 1
            if deg[ni][nj] == 3:
                q.append((ni, nj))

print(removed)
