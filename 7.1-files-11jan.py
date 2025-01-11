"""
7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt

"""

import os
print("current working directory: ", os.getcwd())

#/home/hasan-faisal/code/PY4E/words.txt
fname = input("\nEnter file name: ")

try:
    filehandle = open(fname)
except:
    print("File name is incorrect!")
    quit()

for line in filehandle:
    line = line.rstrip()
    print(line.upper())