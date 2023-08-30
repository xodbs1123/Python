import os 
import os.path

dir = os.path.join('.')

files = os.listdir(dir)
for file in files:
     cur = os.path.join(dir, file)
     typename = 'FILE' if os.path.isfile(cur) else 'DIR'
  
    # typename = "FILE"
    # if not os.path.isfile(os.path.join(dir, file)):
    #     typename = "DIR"    
     size = str(os.path.getsize(cur)) + 'byte'
     abspath = os.path.abspath(cur)
     print("{:<4} {:>10} {}".format(typename, size, abspath))