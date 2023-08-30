import os
for key, value in os.environ.items():
    print("{:<30} : {}".format(key, value))

print(os.environ['PATH'])

try:
    print(os.environ['AAA'])
except:
    pass