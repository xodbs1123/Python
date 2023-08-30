from myclass import Person
from pickle import load
import os.path  # 경로를 만들어줌

filepath = os.path.join('fileopen', 'data.txt')

persons = []
try:
    with open('filepath', 'rb') as fp:
        while True:
            p = load(fp)
            persons.append(p)
            
except:
    print("모든 객체를 읽었습니다.")
finally:
    print(persons)