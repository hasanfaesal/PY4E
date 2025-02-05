"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

fname = '/home/hasan-faisal/code/PY4E/mbox-short.txt'
fhandle = open(fname)

dict = {}

for line in fhandle:
    if line.startswith('From'):
        words = line.split()

        if len(words) > 2:

            time = words[5]
            time = time.split(':')
            hour = time[0]

            dict[hour] = dict.get(hour,0) + 1
            tuple = dict.items()
            
tuple = sorted(tuple, reverse=False)

for key, value in tuple:
    print (key,value)
