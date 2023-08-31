import os.path
import re
import openpyxl
import sys
import datetime

IP_PATTERN = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

class IpCounter:
    def __init__(self, file, asc=False):
        try:
            logFile = os.path.join('.', file)
            with open(logFile, 'r') as fp:
                logData = fp.read()
            ips = re.findall(IP_PATTERN, logData)
            ip_counter = {}
            for ip in ips:
                if ip in ip_counter:
                    ip_counter[ip] += 1
                else:
                    ip_counter[ip] = 1
            key = lambda x : x[1]
            self.__value = sorted(ip_counter.items(), key=key, reverse=not asc)
            self.__current = 0
        except Exception as e:
            raise Exception(str(e))
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__current >= len(self.__value):
            raise StopIteration
        self.__current += 1
        return self.__value[self.__current - 1]

def get_date_string():
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

def save_excel(data, file=None):
    try:
        if not file:
            raise Exception('파일이름이 지정되지 않았습니다.')
        wb = openpyxl.Workbook()
        ws = wb.active 
        title = get_date_string()
        ws.title = title
        for elem in data:
            ws.append(elem)
        wb.save(file)
        wb.close()
        print(f'{title}.xlsx 파일로 저장하였습니다.')
    except:
        print("파일 저장에 실패하였습니다.", file=sys.stderr)

if __name__ == '__main__':
    ipCounter = IpCounter('access.log.2017-10-13')
    save_excel([e for e in ipCounter], file='log.xlsx')