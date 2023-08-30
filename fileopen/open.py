# try:
#     with open('data.txt', 'a', encoding='utf-8') as fp: # with문 탈출하는 순간 자동으로 fp 닫게 해줌
#     # fp = open("data.txt", "a", encoding="utf-8")
#     # # fp 사용 (핸들링)
#         fp.writelines("데이터를 입력합니다\n")
#         subject = '파이썬'
#         print(f"{subject}은 프로그래밍 언어입니다.", file=fp)
#     # print()
#     # fp.close
# except Exception as e:
#     print(e) 







# try:
#     with open('data.txt', 'r', encoding='utf-8') as fp: # with문 탈출하는 순간 자동으로 fp 닫게 해줌
#         print(fp.read())
# except Exception as e:
#     print(e)    






# lines = []
# try:
#     with open('data.txt', 'r', encoding='utf-8') as fp: # with문 탈출하는 순간 자동으로 fp 닫게 해줌
#         for line in fp: #fp로부터 fp.readline을 수행하고 읽어들인 데이터가 있으면 line에 저장하고 for 블럭 수행
#           lines.append(line)
#         print(lines)
# except Exception as e:
#     print(e)    
    
    
    
    
    
