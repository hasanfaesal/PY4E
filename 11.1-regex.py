"""
The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

Handling The Data:
The basic outline of this problem is to read the file, look for integers using the re.findall()
Looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.
"""
import re

fname1 = '/home/hasan-faisal/code/PY4E/regex_sum1.txt'
fname2 = '/home/hasan-faisal/code/PY4E/regex_sum2.txt'

try:
    fhandle1 = open(fname1)
    fhandle2 = open(fname2)
except:
    print('Invalid file path.')
    quit()


sum = 0

for line in fhandle2:
    line = line.rstrip()
    numbers = re.findall(r'[0-9]+', line)
    
    for str_number in numbers:
        sum += int(str_number)

print(sum)