from myclass import Person
from pickle import dump
import os.path  # 경로를 만들어줌

filepath = os.path.join('fileopen', 'data.txt')

try: 
    p = Person('홍길동', 26)
    with open('filepath', 'wb') as fp:
        dump(p, fp)
    print("객체 저장이 완료되었습니다")
except Exception as e:
    print(e)