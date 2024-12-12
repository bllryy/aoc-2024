from operator import mul; import re

"""
from operator import mul; import re
print(eval('+'.join(re.findall(r'mul\(\d+,\d+\)', open('input.txt').read()))))
"""
# part 1 above XDDD

d = open('input.txt').read()
for s in d, re.sub(r'don\'t\(\)[\s\S]*?(do\(\)|$)', '', d):
    print(eval('+'.join(re.findall(r'mul\(\d+,\d+\)', s))))
