import os.path

logFile = os.path.join('auto', 'access.log.2017-10-13')
codecnt = {}

try:
    
    with open(logFile, 'r') as fp:
        for line in fp:
            code = line.split(' ')[8]
        
            if code in codecnt:
                codecnt[code] += 1
            else:
                codecnt[code] = 1
    sortedcnt = sorted(codecnt.items(), key=lambda x: x[1], reverse=True)[:10]
    print(codecnt)
    
    for code in sortedcnt:
        print(code)
except:
    print("예외 발생")