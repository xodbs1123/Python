# 짝수 값 N이 주어질 때 선두 절반 값과 하위 절반의 값을 출력하는 프로그램 작성

N = int(input("값 입력 : "))
nums = str(N)
center = len(nums) // 2
if N % 2 == 0:
    print ("선두 : ", nums[:center])
    print("후위 : ", nums[center:])
else:
    print("짝수가 아닙니다")