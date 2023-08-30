import os.path
import re

logFile = os.path.join('auto', 'access.log.2017-10-13')
ipPattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
ip_counter = {}

try:
    with open(logFile) as fp:
        logData = fp.read()
    ips = re.findall(ipPattern, logData)

    for ip in ips:
        if ip in ip_counter:
            ip_counter[ip] += 1
        else: 
            ip_counter[ip] = 1
    sortedcnt = (sorted(ip_counter.items(), key = lambda x: x[1], reverse=True))[:10]

    for info in sortedcnt:
        print(info)
except:
    print("예외 발생")