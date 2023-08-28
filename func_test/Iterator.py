'''
이터레이터는 순서대로 값을 반환하는 객체
이터레이터 내부에 값을 참조할 수 있는 위치 지정자가 있음
이터레이터 내의 모든 값을 읽어 내면 해당 이터레이터는 사용 불가능
'''
# for i in [1, 3, 5, 2, 4]: # sequency를 가지는 것은 다 iterator 타입
#     print(i)


# nums = [10, 20, 30, 40] #iterator 요소 참조
# iter_nums = iter(nums)
# try:
#         print(iter_nums.__next__()) 
#         print(iter_nums.__next__())
#         print(next(iter_nums))
#         print(iter_nums.__next__())
#         print(next(iter_nums))
# except:
#         print("모든 요소를 읽어 들였습니다")





# nums = [10, 20, 30, 40] #iterator 요소 참조
# iter_nums = iter(nums)
# while True:
#     try:
#         print(iter_nums.__next__()) 
#     except:
#         print("모든 요소를 읽어 들였습니다")
#         break





