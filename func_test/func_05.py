# def adult(age):
    
#     if age >= 19:
#         print('성인입니다')
#         return True
#         print() # 죽은 코드, return 뒤에는 코드가 있어도 의미 없음
#     else:
#         print('미성년자입니다')
#         return False
    
# age = int(input('나이 : '))
# result = adult(age)
# print(result)

def printpersons(person):
    
    '''
    함수명 : printperson
    파라미터 : person 리스트 또는 튜플..
    printperson() 함수는 ...
    주석은 들여쓰기하고 작성해야함...
    '''
    
    print(f"이름 : {person['name']}")
    
print(printpersons.__doc__)