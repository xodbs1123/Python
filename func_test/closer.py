# def counter(init_count = 0):
#     count= init_count # 글로벌도 local도 아니므로 nonlocal
#     def increase(cnt = 1):
#         nonlocal count
#         count += cnt
#         return count
#     return increase

# mycounter = counter(0)
# print(mycounter())
# print(mycounter())
# print(mycounter())
# new_counter = counter(100)
# print(new_counter())
# print(new_counter())
# print(new_counter())
# del mycounter # mycounter 변수 삭제
# del new_counter
