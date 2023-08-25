def printinfo(a, b, c, d):
    print(a, b, c, d)
    
names = ('김태윤', '김진하', '이혜린', '장한솔')
printinfo(*names) # 튜플, 리스트 언패킹 가능

# def printpersons(man, *persons): # 가변인자 파라미터, 호출 시 주어진 인자를 하나의 tuple로 패킹, 가변인자 파라미터 뒤 일반파라미터가 오면 안됨
#     print(len(persons))
#     print(persons)
#     print('man : ', man)
#     for name in persons:
#         print(name)
        
        
# printpersons("김태윤", "김진하", "이혜린", "장한솔")