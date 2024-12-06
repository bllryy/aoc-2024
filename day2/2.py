"""
Each line contains a sequence of integers
A sequence is "safe" if it's either strictly increasing or decreasing and if the difference between two subsequent numbers is between 1 and 3
How many "safe" sequences are there
"""
"""
Define two range objects named increasing and decreasing
define the diffrence ranges between two ints of increasing and decreasing
make a function is_safe to check if takes in a sequence of numbers seq and a safe_rangetakes in a sequence of numbers seq and a safe_range
return a vlue if its safe or not
Iterate the lines of the puzzle input, extract the number sequence and feed it into the is_safe function twice: once with the increasing and once with the decreasing safe range
one of them returns True increment the return value by one
Once the loop is over return the total number of safe sequences
"""

"""
assume that levels is a array of integers
increasing and decreasing like above
zip levels with the first element 
then diffrences between each adjecent pairs
"""



count = 0

def safe(levels): # determine weather or not if it is safe
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)


# Open and process the input file
with open('input.txt', 'r') as file:
    for report in file:  # Each report is a line in the file 
        levels = list(map(int, report.split()))

    for index in range(len(levels)):
        modified_levels = levels[:index] + [levels[index] + 1]
        if safe(modified_levels):
            count += 1
        break

    print(count)







