#===========
# PART 1
#===========

with open('input.txt') as grid:
    grid = [row[:-1] for row in grid.readlines()]

dirs = [(1,0), (-1,0), (0,1), (0,-1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
n = len(grid)
m = len(grid[0])
res = 0

for r in range(n):
    for c in range(m):
        if grid[r][c] == '.':
            continue

        rolls = 0
        for dir in dirs:
            dr, dc = dir

            if (r + dr) < 0 or (r + dr) >= n:
                continue

            if (c + dc) < 0 or (c + dc) >= m:
                continue

            if grid[r + dr][c + dc] == '@':
                rolls += 1

        if rolls < 4:
            res += 1

print(res)

#===========
# PART 2
#===========

with open('input.txt') as grid:
    grid = [list(row[:-1]) for row in grid.readlines()]

dirs = [(1,0), (-1,0), (0,1), (0,-1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

n = len(grid)
m = len(grid[0])

res = 0

def count_rolls(r, c):
    rolls = 0
    for dir in dirs:
        dr, dc = dir

        if (r + dr) < 0 or (r + dr) >= n:
            continue

        if (c + dc) < 0 or (c + dc) >= m:
            continue

        if grid[r + dr][c + dc] == '@':
            rolls += 1

    return rolls

while True:
    marked = set()
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '.':
                continue

            if count_rolls(r, c) < 4:
                marked.add((r, c))

    if not marked:
        break

    for mr, mc in marked:
        grid[mr][mc] = '.'
        res += 1

print(res)

