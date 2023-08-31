import os.path
import re
import openpyxl
import sys
import datetime
import matplotlib.pyplot as plt

IP_PATTERN = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' # 정규식 패턴으로 IP 주소를 정의합니다.

class IpCounter:
    def __init__(self, file, asc=False):
        try:
            file = os.path.join('graph', file) # 파일 경로를 지정합니다.
            with open(file, 'r') as fp:
                logData = fp.read() # 로그 파일을 읽습니다.
            ips = re.findall(IP_PATTERN, logData) # 정규식을 사용하여 IP 주소를 추출합니다.
            ip_counter = {}
            for ip in ips:
                if ip in ip_counter:
                    ip_counter[ip] += 1 # IP 주소의 출현 횟수를 계산합니다.
                else:
                    ip_counter[ip] = 1
            key = lambda x : x[1]
            self.__value = sorted(ip_counter.items(), key=key, reverse=not asc) # IP 주소와 출현 횟수를 정렬합니다.
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
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S') # 현재 날짜와 시간을 문자열로 반환합니다.

def save_excel(data, file=None):
    try:
        if not file:
            raise Exception('파일이름이 지정되지 않았습니다.')
        wb = openpyxl.Workbook() # 워크북을 생성합니다.
        ws = wb.active 
        title = get_date_string()
        ws.title = title
        for elem in data:
            ws.append(elem) # 워크시트에 데이터를 추가합니다.
        wb.save(file) # 지정된 파일 이름으로 저장합니다.
        wb.close()
        print(f'{title}.xlsx 파일로 저장하였습니다.')
    except:
        print("파일 저장에 실패하였습니다.", file=sys.stderr)

class StatusCounter:
    def __init__(self, file, ascending='asc'):
        try:
            status_counter = {}
            file = os.path.join('graph', file) # 파일 경로를 지정합니다.
            with open(file, 'r') as fp:
                for line in fp:
                    status = line.split(' ')[8] # 문자열 분할을 사용하여 상태 코드를 추출합니다.
                    if status in status_counter:
                        status_counter[status] += 1 # 상태 코드의 출현 횟수를 계산합니다.
                    else:
                        status_counter[status] = 1
            args = {
                'key': lambda x: x[1],
                'reverse': False if ascending.upper() == 'ASC' else True
            }
            self.__value = sorted(status_counter.items(), **args) # 상태 코드와 출현 횟수를 정렬합니다.
            self.__current = 0
        except:
            e = sys.exc_info()
            raise Exception(str(e))
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__current >= len(self.__value):
            raise StopIteration
        self.__current += 1
        return  self.__value[self.__current - 1]

def save_image(data, file):
    try:
        plt.title('Status Statics')
        plt.bar([n for n, m in data], [m for n, m in data]) # 막대 그래프를 생성합니다.
        plt.xlabel('Status Code')
        plt.ylabel('Status Count')
        plt.savefig(f"{file}.jpg") # 지정된 파일 이름으로 이미지를 저장합니다.
        plt.close()
    except Exception as e:
        print("이미지 저장 실패", file = sys.stderr)
    else:
        print("이미지 저장 성공")

if __name__ == '__main__':
    # ipCounter = IpCounter('access.log.2017-10-13')
    # save_excel([e for e in ipCounter], file='log.xlsx')
    # statusCounter = StatusCounter('access.log.2017-10-13', 'desc')
    # save_image([item for item in statusCounter], 'statics.jpg')
    pass