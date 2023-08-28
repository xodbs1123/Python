# Python에서의 이진법 동작 방식
BIT_FOR_BYTE = 8
door = 65


op = 1 << BIT_FOR_BYTE - 1
for i in range(BIT_FOR_BYTE):
    if door & op >> i > 0:
        print(1, end='')
    else:
        print(0, end='')
            
   