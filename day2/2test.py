count = 0

def safe(levels):
    # Check if the sequence is either all increasing or all decreasing
    if all(levels[i] < levels[i + 1] for i in range(len(levels) - 1)):  # Increasing
        diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    elif all(levels[i] > levels[i + 1] for i in range(len(levels) - 1)):  # Decreasing
        diffs = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]
    else:
        return False  # Mixed increasing and decreasing, not allowed
    
    return all(1 <= x <= 3 for x in diffs)  # Check if diffs are between 1 and 3

# Open and process the input file
with open('input.txt', 'r') as file:
    for report in file:
        levels = list(map(int, report.split()))

        # Check if the report is safe without modification
        if safe(levels):
            count += 1
            continue
        
        # Try removing one level and check if the modified report is safe
        for index in range(len(levels)):
            modified_levels = levels[:index] + levels[index+1:]
            if safe(modified_levels):
                count += 1
                break

print(count)
