import fileinput


directions = [(-1,-1),(0,-1),(-1,0),(-1,1),(1,-1),(1,0),(0,1),(1,1)]
grid = []
def read_data():
    for line in fileinput.input('input.txt'):
        line.strip()
        grid.append(line)
    
def get_1():
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            for dy, dx in directions:
                if(0 <= y + 3 *dy < len(grid)) and (0 <= x + 3*dx < len(grid)):
                    if grid [x][y] == 'X' and grid[x + dx][y + dy] == 'M' and grid[x + 2 * dx][y + 2 * dy] == 'A' and grid[x + 3 * dx][y + 3 * dy] == 'S':
                        # [x + dx * 2] [y + dy * 2]
                        count += 1                    
    return count

def get_2():
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid [x] [y] == 'M':
                if(x + 2 < len(grid)) and (y + 2 < len(grid [0])):
                    if grid [x+1] [y+1] == 'A' and grid [x+2] [y+2] == 'S':
                        if (grid [x+2] [y] == 'M' and grid [x] [y+2] == 'S') or (grid [x+2] [y] == 'S' and grid [x] [y+2] == 'M'):
                            count += 1

            if (grid [x] [y] =='S'):
                if (x+2 < len(grid)) and (y+2 < len(grid [0])):
                    if grid [x+1] [y+1] == 'A' and grid [x+2] [y+2] == 'M':
                        if (grid [x+2] [y] == 'S' and grid [x] [y+2] == 'M') or (grid [x+2] [y] == 'M' and grid [x] [y+2] == 'S'):
                            count += 1

    return count
 
if __name__ == "__main__":
    read_data()
    print(get_1())
    print(get_2())
