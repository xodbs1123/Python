'''
재귀호출 함수는 변수의 사용을 최소한으로 제한할 수 있음
기본부분 : 재귀호출을 종료하기 위한 부분
유도부분 : 부분적 문제 해결을 위한 재귀호출 부분
재귀함수 호출은 동일한 함수가 호출되지만 사용 메모리 영역은 구분되므로 다른 함수를 호출하는 것과 같음

ex)

f(n,k):
    if 종료조건:
        기본부분
    else:
        [전반부]
        재귀부분
        [후반부]
    
'''

def func(n, k):
    if n >= k:
        return
    else:
        print(n, "번째 실행")
        func(n+1, k)
        
func(0, 10)

# import time
# cnt = 0

# def func(): # 재귀 함수가 무제한 (defualt 약 1000번)동안 돌다가 오류 발생
#     global cnt
#     cnt += 1
#     print("메시지를 처리합니다")
#     time.sleep(1)
#     func()

# func()
# print("재귀호출 휫수 : ", cnt)
# print("프로그램을 종료합니다")    

