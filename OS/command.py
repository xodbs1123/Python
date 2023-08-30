import os

linenum = 1
with os.popen('ls -l', 'r') as pp:
   for line in pp:
     print("{:>3} : {}".format(linenum, line))
     linenum += 1