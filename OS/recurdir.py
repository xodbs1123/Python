# from os import walk
# from os.path import isfile, getsize, abspath, join

# dir = join('.')
# files = walk(dir)
# for root, dirs, files in files:
#     print(abspath(join(root)))
#     for file in files:
#         print(abspath(join(root, file)))





import os
import os.path

dir = os.path.join('.', 'Class')
# if not os.path.exists(dir):
try:
    os.mkdir(dir)
except:
    pass