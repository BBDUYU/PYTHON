#continue & break
#반복문 내에서 사용가능
absent=[2,5] #결석
no_book=[7] #책이없음
for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue #밑에 문장을 실행하지 않고 반복
    elif student in no_book:
        print('오늘 수업은 여기까지 {0},교무실로'.format(student))
        break
    print('{0},책을 읽어'.format(student))
#--------------------------------------------------
#한줄 for
# 출석번호 1,2,3,4 앞에 100을 붙여야함 -> 101, 102,103,104
students=[1,2,3,4,5]
students=[i+100 for i in students]
print(students)
#학생이름을 길이로 변환
students=['Iron man','Thor','Groot']
students=[len(i) for i in students]
print(students)
#학생이름을 대문자로 변환
students=['Iron man','Thor','Groot']
students=[i.upper() for i in students]
print(students)
#------------------------------------------------------
#quiz
#50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성
#조건1 : 승객별 운행 소여시간은 5~50분 사이의 난수
#조건2 : 당신은 소요시간 5~15분 사이의 승객만 매칭
#출력문 예제
# [o] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [o] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 16분)
# 총 탑승 승객 : 2명
from random import *
cnt=0
for i in range(1,51): #1~50명
    time=randrange(5,51) #5분~50분
    if 5<=time <=15: #5분~15분 이내의 손님, 탑승 승객수 증가 
        print('[o] {0}번째 손님 (소요시간 : {1}분)'.format(i,time))
        cnt +=1
    else: #매칭 실패한 경우
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i,time))
print('총 탑승 승객 : {0}명'.format(cnt))