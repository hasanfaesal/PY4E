"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""
#/home/hasan-faisal/code/PY4E/mbox-short.txt
fname = input('enter the filepath: ')
fhandle = open(fname)

dict = {}

for line in fhandle:
    if line.startswith('From:'):
        fromline = line.split()
        email = fromline[1]
        
        dict[email] = dict.get(email, 0) + 1

#maximum loop
maxemail = None
maxcount = None

for email,count in dict.items():
    if maxemail == None or maxcount < count:
        maxemail = email
        maxcount = count # or dict[email]

print(maxemail,maxcount)