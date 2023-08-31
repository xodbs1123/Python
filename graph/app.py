from myclass import IpCounter

try:
    ipCounter = IpCounter('access.log.2017-10-13', False)
    
except Exception as e:
    print(e)