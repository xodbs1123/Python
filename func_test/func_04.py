# 딕셔너리 언패킹
def printpersons(name, age, major):
    print(name, age, major)
    
person = {'name' : '김태윤', 'age' : 20, 'major' : '응컴'}
printpersons(**person)



# def printpersons(**kwargs): #키워드 가변인수 파라미터
#     print(f"이름 : {kwargs['name']}")
#     print(f"나이 : {kwargs['age']}")
#     print(f"전공 : {kwargs['major']}")
    
# printpersons(name = '김태윤', age = 26, major = '응컴')    