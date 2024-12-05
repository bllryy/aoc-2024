from collections import Counter
import math 

a, b = [], []

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()  # remove leading/trailing whitespace
        if line:  # skip empty lines
            try:
                x, y = (int(z) for z in line.split())
                a.append(x)
                b.append(y)
            except ValueError:
                print(f"ssskipping invalid line: {line}")

a.sort()
b.sort()
n = len(a)

# Part 1
print(sum(abs(a[i] - b[i]) for i in range(n)))

# Part 2
c = Counter(b)
print(sum(a[i] * c[a[i]] for i in range(n)))
