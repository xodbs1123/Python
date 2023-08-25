def printPerson(name, age, major='응컴'): # Default 값을 가지는 파라미터는 항상 마지막에 나와야함
    print(f"이름 : {name}, 연령 : {age}, 전공 : {major}")
    
printPerson('김태윤', 26)
printPerson('박채현', 26, '화공')
printPerson(age = 26, major = '응컴', name = '장경호') # 키워드 파라미터