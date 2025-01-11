"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

"""
import os
print("print working directory: ", os.getcwd())

#/home/hasan-faisal/code/PY4E/mbox-short.txt
fname = input("\nenter the file name with path: ")

try:
    fhandle = open(fname)
except:
    print("Incorrect file name!")
    exit()

count = 0
values = 0

for line in fhandle:

    if line.startswith("X-DSPAM-Confidence:"):

        indicator = line.find(':')
        values = values + float(line[indicator+1:])
        count = count+1


print(values/count)
