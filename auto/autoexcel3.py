import openpyxl
import os.path


products = [ 
            {'Name':'cpu', 'price':200000, 'stock':10},
            {'Name':'ram', 'price':300000, 'stock':20},
            {'Name':'ssd', 'price':400000, 'stock':30}
        ]

excelFile = os.path.join('.', 'data.xlsx')
wb = openpyxl.Workbook()
ws = wb.active

# products의 key 값을 리스트로 변환합니다.
keys = [k for k, v in products[0].items()]

# 1행에 products의 key 값을 입력합니다.
ws.append(keys)

for item in products:
    # item의 value 값을 리스트로 변환합니다.
    values = [v for k, v in item.items()]
    
    # values를 ws의 다음 행에 입력합니다.
    ws.append(values)

wb.save(excelFile)
wb.close()