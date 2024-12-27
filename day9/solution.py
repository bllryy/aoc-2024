disk = []
fid = 0

for i, char in enumerate(input()):
    X = int(char)
    if i % 2 == 0:
        disk += [fid] * X
        fid += 1
    else:
        disk += [-1] * X

print(disk)
