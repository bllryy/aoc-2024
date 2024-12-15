grid = list(map(list,open(0).read().splitlines()))

# find the guard

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid [r][c] == "^":
            break
    else:
        continue
    break

# determine if the guard will loop or not
def loops(grid, r,c):
# decreasce row by 1 and change collum by nothing
    dr = -1
    dc = 0

# determine pos
    seen = set()

# guard

    while True:
        seen.add((r,c,dr,dc))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols: return False
        if grid[r + dr][c + dc] == "#":
        # getting the guard to move after hitting # just changing for ex: -1,0 to 1,0 for the turn on the grid
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc
        # if the new pos and direction are already seen we have found a loop
        if (r,c,dr,dc) in seen:
            return True 
count = 0

# bruete force
for cr in range(rows):
    for cc in range(cols):
        if grid [cr][cc] != ".": continue
        grid [cr][cc] = "#"
        if loops(grid, r, c):
            count += 1 
        grid[cr][cc] = "."

print(count)

