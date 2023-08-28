N = int(input('N : ')) # 주어진 수
cnt = 0 # 박수 친 횟수

# 리스트 생성 1 부터 N까지
for i in range(1, N+1):
    tmp = i
    while tmp > 0:
        if (tmp % 10) % 3 == 0: # 마지막 자리가 3의 배수면 cnt + 1
            cnt += 1
        tmp //= 10 # 마지막 자리를 제외한 자리수 구하기
        
            
print(cnt)

