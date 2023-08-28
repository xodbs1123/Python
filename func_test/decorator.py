# # 데코레이터 사용 전
# def work():
#     print("함수가 호출되었음")

# def decorator(func):
#     def wrapper():
#         print("함수 실행 전 코드 작성")
#         func()
#         print("함수 실행 후 코드 작성") 
#     return wrapper

# work = decorator(work)
# work()



# 데코레이터 사용 후
def decorator(func):
    def wrapper(*args, **kwargs): # 가변 파라미터를 사용함으로써 함수 입력 수가 얼마나 많던 상관 없어짐
        print("함수 실행 전 코드 작성")
        func(*args, **kwargs)
        print("함수 실행 후 코드 작성") 
    return wrapper

@decorator # 데코레이터
def work(msg, num, num2):
    print(msg, num, num2)

work('Hello', 10, 12)