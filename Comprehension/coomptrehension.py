'''
파이썬에서 list, dict, set과 같은 자료 구조를 생성, 추출, 검색할 때
간결하고 이해하기 쉽게 표현하기 위한 문법
'''

# A = [i * 10 for i in range(1, 11)]
# print(A)



# A = [i for i in range(1, 20) if i % 2 == 0]

# print(A)



# keys = ['name', 'age', 'major']
# values = ['홍길동', 20, '전산학과']
# person = {keys[i]:values[i] for i in range(len(keys))}
# print(person)



# person = {'name': '홍길동', 'age':20, 'major':'전산학과'}
# # keys = [key for key, value in person.items()]
# keys = [key for key in person]
# print(keys)