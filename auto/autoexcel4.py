import openpyxl
import os.path


products = [
{'name': 'CPU', 'count': 100, 'price': 350000},
{'name': 'BOARD', 'count': 120, 'price': 125000},
{'name': 'RAM', 'count': 98, 'price': 60000},
{'name': 'SSD', 'count': 85, 'price': 95000},
{'name': 'HDD', 'count': 112, 'price': 80000},
{'name': 'PSU', 'count': 105, 'price': 89000},
{'name': 'MONITOR', 'count': 80, 'price': 280000},
{'name': 'KEYBOARD', 'count': 90, 'price': 23000},
{'name': 'MOUSE', 'count': 110, 'price': 25000}
]

excelFile = os.path.join('.', '제품보유현황.xlsx')
wb = openpyxl.Workbook()
ws = wb.active
headers = ['제품명', '보유수량', '제품단가', '단가총액']
ws.append(headers)

row =2
column = 4
n =3
for item in products:
    
    # item의 value 값을 리스트로 변환합니다.
    values = [v for k, v in item.items()]
    
    # values를 ws의 다음 행에 입력합니다.
    ws.append(values)
    # 단가총액을 계산합니다.
    ws.cell(row, column, value=values[1]*values[2])
    
    row += 1

wb.save(excelFile)
wb.close()