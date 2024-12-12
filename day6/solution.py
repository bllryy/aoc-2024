import fileinput

grid = []

for line in fileinput.input('in.txt'):
    line.strip()
    grid.append(line)

def find_start():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid [i] [j] == '^':
                return (i,j)



print(find_start())
