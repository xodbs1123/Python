from datetime import datetime

today = datetime.now()
today.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')
print(today)